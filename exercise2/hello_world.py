#!/usr/bin/env python

import os
import requests
import subprocess
import sys
from gevent.wsgi import WSGIServer

import flask

proxy = flask.Flask('__main__')
proxy.debug = False

@proxy.route('/hello', methods=['GET'])
def hello():
    return ("Hello World from my black-box FaaS VNF! ")

port = int('5000')
server = WSGIServer(('', port), proxy, log=None)
server.serve_forever()

