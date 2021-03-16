import random
from sys import argv

answer = random.randint(1, 10)

while True:
    try:
        guess = int(input('Guess a number 1~10:'))
        if 0 < guess < 11:
            if guess == answer:
                print('You\'re a genius')
                break
        else:
            print('Please try again between 1~10')
    except ValueError:
        print('Please enter a number')
        continue