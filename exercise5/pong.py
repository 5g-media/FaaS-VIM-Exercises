from gevent.pywsgi import WSGIServer

import flask


proxy = flask.Flask('__main__')
proxy.debug = False


@proxy.route('/pong/<num>', methods=['GET'])
def pong(num):
    return ('pong'*int(num), 200)


def main(args):
    port = int('5001')
    server = WSGIServer(('', port), proxy, log=None)
    server.serve_forever()
