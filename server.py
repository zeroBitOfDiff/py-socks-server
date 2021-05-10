# https://github.com/rushter/socks5
import logging
import select
import socket
import struct
from socketserver import ThreadingMixIn, TCPServer, StreamRequestHandler

logging.basicConfig(level=logging.DEBUG)
SOCKS_VERSION = 5

# creates a threading version of TCP server and listens for incoming connections 
# on a specified address and port
# Every time there is a new incoming TCP connection (session) the server spawns 
# a new thread with SocksProxy
class ThreadingTCPServer(ThreadingMixIn, TCPServer):
    pass


class SocksProxy(StreamRequestHandler):
    username = 'zero'
    password = 'password'

    def handle(self):

        # Greating header
        # read and unpack 2 bytes from a client

        header = self.connection.recv(2)
        version, nmethods = struct.unpack("!BB", header)

        # socks 5
        assert version == SOCKS_VERSION
        assert nmethods > 0

        # Get available methods
        methods = self.get_available_methods(nmethods)

        # accept only USERNAME/PASSWORD auth
        if 2 not in set(methods):
            # close connection
            self.connection.sendall(struct.pack("!BB", SOCKS_VERSION, 255))
            self.server.close_request(self.request)
            return

        # Send server choice
        self.connection.sendall(struct.pack("!BB", SOCKS_VERSION, 2))

    def get_available_methods(self, n):
        methods = []
        for i in range(n):
            methods.append(ord(self.connection.recv(1)))
        return methods

    def verify_credentials(self):
        version = ord(self.connection.recv(1))
        assert version == 1

        username_len = ord(self.connection.recv(1))
        username = self.connection.recv(username_len).decode('utf-8')

        password_len = ord(self.connection.recv(1))
        password = self.connection.recv(password_len).decode('utf-8')

        if username == self.username and password == self.password:
            # Success, status = 0
            response = struct.pack("!BB", version, 0)
            self.connection.sendall(response)
            return True


        # Failure, status != 0
        response = struct.pack("!BB", version, 0xFF)
        self.connection.sendall(response)
        self.server.close_request(self.request)
        return False



if __name__ == '__main__':
    with ThreadingTCPServer(('127.0.0.1', 9011), SocksProxy) as server:
        server.serve_forever()