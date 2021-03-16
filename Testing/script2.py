import random

answer = random.randint(1, 10)

def randg(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('You\'re a genius')
            return True

    else:
        print('Please try again between 1~10')
        return False

if __name__=='__main__':
    while True:
        try:
            guess = int(input('Guess a number 1~10:'))
            if(randg(guess, answer)):
                break
        except ValueError:
            print('Please enter a number')
            continue

