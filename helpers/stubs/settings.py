import yaml


class Settings(object):
	class __Iterator(object):
		def __init__(self, settings):
			self.__current_key = 0
			self.__settings = settings
			self.__keys = [key for key in settings]

		def __iter__(self):
			return self

		def __next__(self):
			if self.__current_key >= len(self.__keys):
				raise StopIteration()

			name = self.__keys[self.__current_key]
			content = self.__settings[name]

			self.__current_key = self.__current_key + 1
			return name, Settings(content)


	def __init__(self, settings):
		if type(settings) is not str:
			self.__settings = settings
			return

		with open(settings, 'r+') as settings_file:
			self.__settings = yaml.load(settings_file, Loader=yaml.Loader)

	def __getattr__(self, name):
		target = self.__settings[name]

		if type(target) is dict:
			return Settings(target)
		return target

	def __iter__(self):
		return Settings.__Iterator(self.__settings)

	def __str__(self):
		return json.dumps(self.__settings, indent=4)