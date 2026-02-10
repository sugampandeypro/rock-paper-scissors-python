import random

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

game_images = [rock, paper, scissors]

# Asking player for their choice
player_choice = int(input(
    "What do you choose? Type 0 for rock 1 for paper or 2 for scissors?...\n"
))

if player_choice >= 0 and player_choice <= 2:
    print("Player chose:")
    print(game_images[player_choice])

# Computer randomly chooses
computer_choice = random.randint(0, 2)

print("Computer chose:")
print(game_images[computer_choice])

if player_choice == computer_choice:
    print("It is a draw")

elif (player_choice == 0 and computer_choice == 2) or \
     (player_choice == 1 and computer_choice == 0) or \
     (player_choice == 2 and computer_choice == 1):
    print("Player wins")

else:
    print("Computer Wins")
