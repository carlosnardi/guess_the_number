
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
number_to_hit = random.choice(numbers)

print(number_to_hit)
  
if difficulty == "easy":
  attempts = 10
elif difficulty == "hard":
  attempts = 5

print(f"You have {attempts} attempts remaining to guess the number.")

while attempts > 0:
  guess = int(input('Make a guess: '))
  if guess > number_to_hit:
    print("Too high.\nGuess again.")
    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess the number.")

  elif guess < number_to_hit:
    print("Too low.\nGuess again.")
    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess the number.")
  
  elif guess == number_to_hit:
    print("Nice work!")
    break
  



