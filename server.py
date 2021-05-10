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

    def handle(self):
        # Our main logic will be here
        pass



if __name__ == '__main__':
    with ThreadingTCPServer(('127.0.0.1', 9011), SocksProxy) as server:
        server.serve_forever()