import yaml
import json
import argparse
import subprocess

from helpers.stubs import settings

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--settings', default='application.yaml')


def build(settings):
	def install(name, target):
		build_type = getattr(settings.application.packages, name).type
		command_body = 'python -m grpc.tools.protoc -I protocols ' + \
			'--{type}_out=packages/{target} ' + \
			'--grpc_{type}_out=packages/{target} ' + \
			'protocols/{name}.proto'

		command = command_body.format(type=build_type, target=target, name=name)
		subprocess.run(command.strip().split(' '))

	for build_target, content in settings.application.build:
		for dependency in content.depends:
			install(dependency, build_target)
		install(build_target, build_target)
		

if __name__ == '__main__':
	args = parser.parse_args()
	settings = settings.Settings(args.settings)
	
	build(settings)
