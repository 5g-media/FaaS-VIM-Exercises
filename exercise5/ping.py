import requests
import subprocess
from gevent.pywsgi import WSGIServer

import flask


proxy = flask.Flask('__main__')
proxy.debug = False


def _get_conf(param_name):
    value = ''
    try:
        with open('/conf/%s' % param_name, 'r') as f:
            value = f.read()
    except:
        pass

    return value


@proxy.route('/ping/<num>', methods=['GET'])
def ping(num):
    target_ip = _get_conf('target_ip')
    if not target_ip:
        return ("\n\nI don't know the target I should ping to :( \n\n")

    r = requests.get('http://%s:5001/pong/%s' % (target_ip.strip(), num),
                     verify=False)
    r.raise_for_status()
    return ("\n\n%s\n\n" % r.text)


def main(args):
    port = int('5000')
    server = WSGIServer(('', port), proxy, log=None)
    server.serve_forever()
