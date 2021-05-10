> a client establishes a TCP session to the SOCKS server, it must send a greeting message.

> message consists of 3 fields:
* version	
* nmethods	
* methods

> According to the RFC 1928, the supported values of methods field defined as follows:
* '00' NO AUTHENTICATION REQUIRED
* '01' GSSAPI
* '02' USERNAME/PASSWORD
* '03' to X'7F' IANA ASSIGNED
* '80' to X'FE' RESERVED FOR PRIVATE METHODS
* 'FF' NO ACCEPTABLE METHODS



> Once the client has received the server choice, it responds with username and password credentials.
* version
* ulen
* uname
* plen
* passwd

> server '02' response:
* version
* method

> The status field of 0 indicates a successful authorization

