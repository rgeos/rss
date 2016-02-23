#!/usr/bin/env python

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from main import app

# running the web server
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(8081)
IOLoop.instance().start()