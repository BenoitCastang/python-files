#!/usr/bin/env python3

import subprocess

def check_if_service_is_running(service):
    return subprocess.call(['ps', '-C', service])

service = input('Enter a service: ')
if check_if_service_is_running(service) == 0:
    print('{service} is running\nstopping {service}...'.format(service=service))
    subprocess.call(['sudo', 'systemctl', 'stop', service])
else:
    print('{service} is not running\nstarting {service}'.format(service=service))
    subprocess.call(['sudo', 'systemctl', 'start', service])
subprocess.call(['systemctl', 'status', service])
