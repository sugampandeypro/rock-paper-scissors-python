import random

#Asking player for their choice
player = int(input
             ("What do you choose? Type 0 for ""rock"
                   " 1 for paper or 2 for scissors\n"))

if player==0:
    print("You choose a rock")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif player==1:
    print("You choose a paper")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif player==2:
    print("You choose a scissors")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
else:
    print("You made a invalid chooice.Please choose 0,1 or 2")

#computer randomly chooses
computer=random.randint(0,2)
if computer==0:
    print("Computer choose a rock")
    print('''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''')
elif computer==1:
        print("Computer choose a paper")
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif computer==2:
    print("Computer chooses a scissors")
    print('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')

if player==computer:
    print("It is a draw")

elif ( player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1):
    print("Player wins")

else:
    print("Computer Wins")


