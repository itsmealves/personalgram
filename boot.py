import os
import argparse
import subprocess

from helpers.stubs import settings

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--settings', default='application.toml')


def build(settings):
	def install(name, build_type, target):
		target_path = os.path.join('packages', target)
		protocol_path = os.path.join('protocols', name)
		
		command_body = 'python -m grpc.tools.protoc -I . ' + \
			'--{0}_out={1} --grpc_{0}_out={1} {2}.proto'

		command = command_body.format(build_type, target_path, protocol_path)
		subprocess.run(command.strip().split(' '))

	def clean_build_location(target):
		path = os.path.join('packages', target, 'protocols')
		subprocess.run(['rm', '-rf', path])

	for package_name, package_data in settings.package:
		clean_build_location(package_name)

		for dependency in package_data.dependencies:
			dependency_type = getattr(settings.package, dependency).type
			install(dependency, dependency_type, package_name)

		if package_data.type is not None:
			install(package_name, package_data.type, package_name)
		

if __name__ == '__main__':
	args = parser.parse_args()
	settings = settings.Settings(args.settings)
	
	build(settings)
