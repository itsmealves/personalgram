import os
import grpc
import protocols
import importlib


class ServiceManager(object):
	__connections = {}

	class __ServiceInstance(object):
		def __init__(self, name, port):
			self.__messages = importlib.import_module('protocols.{}_pb2'.format(name))
			self.__services = importlib.import_module('protocols.{}_pb2_grpc'.format(name))
			self.__channel = grpc.insecure_channel('localhost:{}'.format(port))
			self.__stub_class = getattr(self.__services, '{}Stub'.format(name.capitalize()))

			self.__stub = self.__stub_class(self.__channel)

		def release(self):
			self.__channel.close()

		def __getattr__(self, name):
			return getattr(self.__stub, name)

		@property
		def messages(self):
			return self.__messages

		@property
		def services(self):
			return self.__services

	@staticmethod
	def get(name):
		if name not in ServiceManager.__connections:
			env_key = '{}_PORT'.format(name.upper())
			
			port = os.environ.get(env_key)
			ServiceManager.__connect(name, port)
		return ServiceManager.__connections[name]


	@staticmethod
	def __connect(name, port):
		instance = ServiceManager.__ServiceInstance(name, port)
		ServiceManager.__connections[name] = instance

	@staticmethod
	def release():
		for name in ServiceManager.__connections:
			instance = ServiceManager.__connections[name]
			instance.release()

