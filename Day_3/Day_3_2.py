################### PIZZA #############################
print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

#https://replit.com/@SakshamVerma1/day-3-4-test-your-code#main.py
extra_cheese = input("Do you want extra cheese? Y or N ")

price = 0 
if(size == "S"):
  price += 15
  if(add_pepperoni == "Y"):
    price += 2
else:
  if(size == "M"):
    price += 20
  else:
    price += 25
  
  if(add_pepperoni == "Y"):
    price += 3

if(extra_cheese == "Y"):
  price +=1
 
print(f"Your final bill is: ${price}.")

