import importlib
from abc import ABC
from abc import abstractmethod


class StreamStrategy(ABC):
	@abstractmethod
	def read(self):
		pass

	@abstractmethod
	def read_bytes(self):
		pass

	@abstractmethod
	def release(self):
		pass


class Stream(object):
	__instance = None
	__package = 'stream.webcam'
	__class_id = 'WebcamStream'

	@staticmethod
	def get_instance():
		if Stream.__instance is None:
			module = importlib.import_module(Stream.__package)
			DefaultStream = getattr(module, Stream.__class_id)
			Stream.__instance = DefaultStream()
		return Stream.__instance

	@staticmethod
	def release():
		if Stream.__instance is not None:
			Stream.__instance.release()
