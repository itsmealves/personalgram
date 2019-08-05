import falcon
import dotenv
import argparse
from gevent import pywsgi
from resources import ResourceManager

dotenv.load_dotenv()
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', type=int, default=8080,
					help='Defines a port to which the server should listen')
parser.add_argument('-o', '--host', default='',
					help='Defines the host to which the server should respond')


if __name__ == '__main__':
	args = parser.parse_args()
	interface = (args.host, args.port)
	print('Listening to {}:{}'.format(*interface))

	api = falcon.API()
	ResourceManager.load_resources(api)

	server = pywsgi.WSGIServer(interface, api)
	server.serve_forever()
