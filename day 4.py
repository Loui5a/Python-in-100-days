rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
players_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
random_number = random.randint(0,2)

choices = [rock, paper, scissors]
if int(players_choice) > 3 or int(players_choice) < 0:
    print("number out of bounds, you lose")
else:    
    print(choices[int(players_choice)])
    print("Computer chose:")
    print(choices[int(random_number)])

    if int(players_choice) == 0 and int(random_number) == 0:
        print("it's a draw")
    elif int(players_choice) == 0 and int(random_number) == 1:
        print("You lose")
    elif int(players_choice) == 0 and int(random_number) == 2:
        print("You win")
    
    elif int(players_choice) == 1 and int(random_number) == 1:
        print("it's a draw")
    elif int(players_choice) == 1 and int(random_number) == 2:
        print("You lose")
    elif int(players_choice) == 1 and int(random_number) == 0:
        print("You win")
    
    elif int(players_choice) == 2 and int(random_number) == 2:
        print("it's a draw")
    elif int(players_choice) == 2 and int(random_number) == 0:
        print("You lose")
    elif int(players_choice) == 2 and int(random_number) == 1:
        print("You win")