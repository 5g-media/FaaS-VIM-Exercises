#!/usr/bin/env python

from gevent.wsgi import WSGIServer

import flask

proxy = flask.Flask('__main__')
proxy.debug = False

@proxy.route('/hello', methods=['GET'])
def hello():
    return ("\n\nHello World from my black-box FaaS VNF!\n\n")

port = int('5000')
server = WSGIServer(('', port), proxy, log=None)
server.serve_forever()

