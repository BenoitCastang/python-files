#!usr/bin/env python3

import subprocess

output = subprocess.check_output(['ls', '-la'])
print(output)
