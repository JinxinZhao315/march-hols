import random
number = random.randint(0,100)

guess = int(input('Guess an integer from 0 to 100. You have 7 guesses.'))
guess_no = 0


while True:
    if guess > 100:
        print('Hey! Between 0 and 100.')
        guess = int(input('Guess again'))
        continue
    if guess>number:
        print('Too high')
    elif guess<number:
        print('Too low')
    else:
        print('You got it!')
        break
    guess_no += 1
    if guess_no > 7:
        print('You run out of guesses!')
        break
    guess = int(input('Guess again'))

    