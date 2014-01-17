#! /usr/bin/env python
from __future__ import print_function
import os, sys

if len(sys.argv) < 2:
    build_type = 'html'
else:
    build_type = sys.argv[1]

os.system('make %s' % build_type)

os.chdir('./build/%s' % build_type)

if sys.version_info[0] < 3:
    import SimpleHTTPServer as server
    import SocketServer as socketserver
else:
    from http import server
    import socketserver

HOST = 'localhost'
PORT = 8000

Handler = server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer((HOST, PORT), Handler)

print("serving at http://%s:%d" % (HOST, PORT))
httpd.serve_forever()
