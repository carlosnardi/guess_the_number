'''

Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': 

easy
You have 10 attempts remaining to guess the number.
hard: 5

Make a guess: 
50
Too high.
Guess again.

Make a guess: 
1
Too low.
Guess again.
You have 8 attempts remaining to guess the number. 
'''
import random
import art

print(art.logo2)

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

numbers = []
number = 0
for i in range(100):
  number += 1
  numbers.append(number)

guessing_number = random.choice(numbers)

# print(guessing_number)
  
if difficulty == "easy":
  attempts = 10
elif difficulty == "hard":
  attempts = 5

print(f"You have {attempts} attempts remaining to guess the number.")

guess = int(input('Make a guess: '))

if guess > guessing_number:
  ptint("")



