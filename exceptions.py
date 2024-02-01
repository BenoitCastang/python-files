#!/usr/bin/env python3

import subprocess
import os

def check_if_service_is_running(service):
    return subprocess.call(['ps', '-C', service])

# service = input('Enter a service: ')

# if check_if_service_is_running(service) == 0:
#     print('{service} is running\nstopping {service}...'.format(service=service))
#     subprocess.call(['sudo', 'systemctl', 'stop', service])
# else:
#     print('{service} is not running\nstarting {service}'.format(service=service))
#     subprocess.call(['sudo', 'systemctl', 'start', service])

# try:
#     subprocess.call(['systectl', 'status', service])
# except:
#     print('Displaying status failed.')

def function():
    exit(34)

print(function())
# result = subprocess.call(['echo', '$?'])
# print(result)
# os.system('echo $?')
