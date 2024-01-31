#!/usr/bin/env python3

def hello_world():
    global message
    message = 'Hello, world!'
    print(message)

hello_world()

print(message)
