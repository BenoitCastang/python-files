#!/usr/bin/env python3

i = 1
print('i =', i)

while i < 20:
    if i % 3 == 0:
        i += 4
        print('i =', i)
        continue
    else:
        i += 1
        print('i =', i)
