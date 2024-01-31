#!/usr/bin/env python3

import os

file = input('Enter a file: ')

if os.path.isfile(file):
    print("The file exists.")
else:
    print("The file does not exist.\nCreating the file...")
    os.system("touch {}".format(file))
    os.system("ls -l {}".format(file))
