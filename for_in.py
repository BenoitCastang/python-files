#!/usr/bin/env python3

def letter_type():
    string = 'Le loup a faim'
    for letter in string :
        if letter in 'AEIOUYaeiouy' :
            print(letter, 'est une voyelle')
        elif letter in ' ' :
            print('*')
        else : 
            print(letter, 'est une consonne')

def print_random_range():
    import random
    counter = random.randint(1,10)
    number = 1
    for i in range(counter):
        print(number)
        number += 1

# letter_type()
print_random_range()
