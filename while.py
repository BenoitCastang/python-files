#!/usr/bin/env python3

def multiplyInput():
    while 1:
        num = input('Enter number (or q to leave): ') 
        if num == 'exit' or num == 'leave' or num == 'quit' or num == 'q':
            break
        else:
            num = int(num)
            howManyTimes = int(input('How many times to multiply: '))
            i = 1
            while i <= howManyTimes :
                print(num, 'x', i, '=', num * i)
                i += 1

multiplyInput()
