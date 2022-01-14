import random
from art import logo
print(logo)
number=random.randint(1,100)
intro=input('''Welcome to the Number Guessing Game!
I'm thinking of a number from 1 to 100.
Choose a difficulty. Type 'easy' or 'hard':''')


def number_guess(intro):
  if intro=='easy':
    lives=10
  else:
    lives=5  
  print(f'You have {lives} attempts remaining to guess the number.')
  your_guess=int(input('Make a guess:'))
  while not number==your_guess:
    if lives>1:
      lives-=1
      if your_guess>number:
        print('''
Too high.
Guess again.''')
        print(f'You have {lives} attempts remaining to guess the number.')

      else:
        print('''
Too low.
Guess again.''')
        print(f'You have {lives} attempts remaining to guess the number.')
      your_guess=int(input('Make a guess:'))
    else:
      return print("You've run out of guesses, you lose.")
          
  if number==your_guess:
    print(f'You got it! The answer was {number}.') 
number_guess(intro)


