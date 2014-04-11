#!/usr/bin/env python
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("rip", "ripper", "/home/rip", perm="elradfmw")
authorizer.add_anonymous("/tmp")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()