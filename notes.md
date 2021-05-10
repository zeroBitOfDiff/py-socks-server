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

> Once the authorization has completed the client can send request details.
* version
* cmd
* rsv
* atyp
* dst.addr
* dst.port

> VERSION protocol version: 
* '05'
> CMD
* CONNECT '01'
* BIND '02'
* UDP ASSOCIATE '03'
> RSV 
* RESERVED
> ATYP address type of following address
* IP V4 address: '01'
* DOMAINNAME: '03'
* IP V6 address: '04'
> DST.ADDR 
* desired destination address
> DST.PORT 
* desired destination port in network octet order

> As soon as server establishes a connection to the desired destination it should reply with a status and remote address.
* version
* rep 
* rsv
* atyp
* bnd.addr
* bnd.port

> VER protocol version: 
* X'05'
> REP Reply field:
* '00' succeeded
* '01' general SOCKS server failure
* '02' connection not allowed by ruleset
* '03' Network unreachable
* '04' Host unreachable
* '05' Connection refused
* '06' TTL expired
* '07' Command not supported
* '08' Address type not supported
* '09' to X'FF' unassigned
> RSV 
* RESERVED
> ATYP address type of following address
* IP V4 address: '01'
* DOMAINNAME: '03'
* IP V6 address: '04'
> BND.ADDR 
* server bound address
> BND.PORT 
* server bound port in network octet order