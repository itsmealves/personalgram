import os
import argparse
import subprocess

from helpers.stubs import settings

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--settings', default='application.toml')

def install(name, build_type, target):
	target_path = os.path.join('packages', target)
	protocol_path = os.path.join('protocols', name)
	
	command_body = 'python -m grpc.tools.protoc -I . ' + \
		'--{0}_out={1} --grpc_{0}_out={1} {2}.proto'

	command = command_body.format(build_type, target_path, protocol_path)
	subprocess.run(command.strip().split(' '))

def install_environment(name, environment):
	environment_path = os.path.join('packages', name, '.env')
	with open(environment_path, 'w+') as f:
		for key in environment:
			f.write('{}={}'.format(key, environment[key]))
			f.write('\n')

def clean_build_location(target):
	protocol_path = os.path.join('packages', target, 'protocols')
	env_path = os.path.join('packages', target, '.env')
	
	subprocess.run(['rm', '-rf', protocol_path])
	subprocess.run(['rm', '-rf', env_path])

def add_port(env, name, settings):
	port_key = '{}_PORT'.format(name.upper())
	env[port_key] = getattr(settings.package, name).port


def build(settings):
	for package_name, package_data in settings.package:
		environment = {}
		add_port(environment, package_name, settings)
		clean_build_location(package_name)

		for dependency in package_data.dependencies:
			add_port(environment, dependency, settings)
			install(dependency, package_data.type, package_name)

		if package_data.available is None or package_data.available:
			install(package_name, package_data.type, package_name)
		install_environment(package_name, environment)
		

if __name__ == '__main__':
	args = parser.parse_args()
	settings = settings.Settings(args.settings)
	
	build(settings)
