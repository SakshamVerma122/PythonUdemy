#https://replit.com/@SakshamVerma1/day-8-2-exercise#main.py

#Write your code below this line 👇

import math
def prime_checker(number):
  boolean = True
  
  if(number ==2):
    print("It's a prime number.")
  else:
    for i in range(2,math.ceil(math.sqrt(number)+1)):
    
      if(number % i == 0):
        print("It's not a prime number.")
        boolean = False
        break 

    if(boolean):
      print("It's a prime number.")  

      




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)