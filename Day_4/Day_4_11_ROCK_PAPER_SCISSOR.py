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
rock_paper_scissor=[rock,paper,scissors]

import random as rm
from datetime import datetime

rm.seed(datetime.now())

comp_move = rm.randint(0, 2)

user_move = int(input("Enter what you want: rock = 0 , paper = 1 , scissors = 2: "))
print("USER MOVE:")
print(rock_paper_scissor[user_move])

print("COMPUTER MOVE:")
print(rock_paper_scissor[comp_move])

if(comp_move == user_move):
    print("MATCH DRAW")
elif(comp_move == 0):
    if(user_move ==1):
        print("USER_WINS")
    else:
        print("COMP_WINS")
elif(comp_move == 1):
    if(user_move ==2):
        print("USER_WINS")
    else:
        print("COMP_WINS")
else:
    if(user_move == 0):
        print("USER_WINS")
    else:
        print("COMP_WINS")
    