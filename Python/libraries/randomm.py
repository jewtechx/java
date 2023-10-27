#random
from random import choice
from random import randint
from random import shuffle


i = 0
while i < 5:
    result = choice(["heads","tails"])
    print(result)
    i+=1

"""
A guessing game that asks a user to guess a number between 1 and 10
"""
while True:
    def get_int(game):
        while True:
            try:
                return int(input(game))
            except ValueError:
                print("Enter a number only")
                continue
            
    value = get_int('Guess a number between 1 and 10 ')
    correctValue = randint(1,10)
    if value == correctValue:
        print("Nice Buddy! You\'re right")
        break
    else:
        print("Nope. Try again")
        continue

# shuffle
cards = ['King', 'Queen', 'Jack']
shuffle(cards)
for card in cards:
    print(card)


