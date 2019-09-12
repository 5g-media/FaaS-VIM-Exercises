import os
import requests
import subprocess
import sys
from gevent.pywsgi import WSGIServer

import flask

proxy = flask.Flask('__main__')
proxy.debug = False

name = None

@proxy.route('/hello', methods=['GET'])
def hello():
    return ("\n\nHello %s, from my first FaaS VNF!\n\n" % name)

def main(args):
    global name
    name = args.get('name', 'stranger')
    port = int('5000')
    server = WSGIServer(('', port), proxy, log=None)
    server.serve_forever()

