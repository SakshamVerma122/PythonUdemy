import os
#HINT: You can call clear() to clear the output in the console.

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program.")

command_user = 'yes'

max_dict = {"name":'',"bid":0}

bidders_list = []
while(command_user == 'yes'):
    
  os.system('cls')
  
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  command_user = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  
  bidders_dict = {}
  bidders_dict["name"] = name
  bidders_dict["bid"] = bid
  
  if(max_dict["bid"] < bidders_dict["bid"]):
    max_dict = {}
    max_dict["name"] = name
    max_dict["bid"] = bid

  bidders_list.append(bidders_dict)

print(f""""The winner is {max_dict["name"]} with a bid of ${max_dict["bid"]}.""")