#Number Guessing Game Objectives:
import random

def random_number():
  """Returns a random number between 1 and 100"""
  return random.randint(1,100)

def check_guess(guess, number):
  """""Checks the guess against the number and returns a a boolean whether the game is over or not"""
  game_over = False
  if(guess == number):
    print(f"You got it! The answer was {number}")
    game_over = True 
    return game_over
  elif(guess > number):
    print("Too high.")
    return game_over
  elif(guess < number):
    print("Too low.")
    return game_over

def attempts(difficulty):
  """Returns the number of attempts based on the difficulty"""
  if(difficulty.lower() == "easy"):
    return 10
  else:
    return 5

def game():
  """The main game function"""
  number = random_number()
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  number_of_attempts = attempts(difficulty)
  
  while(number_of_attempts > 0):
    print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    guess = input("Make a guess: ")
    game_over = check_guess(int(guess), number)
    if(game_over == True):
      break
    number_of_attempts -= 1
  print("You have no more attempts, you lose!")

game()