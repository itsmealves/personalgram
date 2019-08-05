import os
from abc import ABC


class Resource(ABC):
	route = '/'

	def __init__(self, api):
		api.add_route(self.route, self)


class ResourceManager(object):
	__resources = []

	@staticmethod
	def load_resources(api):
		ResourceManager.__import_resources()
		for ResourceDefinition in Resource.__subclasses__():
			instance = ResourceDefinition(api)
			ResourceManager.__resources.append(instance)

	@staticmethod
	def __import_resources():
		root = 'resources'
		for file_name in os.listdir(root):
			if not file_name.startswith('__'):
				name, ext = os.path.splitext(file_name)
				__import__('{}.{}'.format(root, name))

        