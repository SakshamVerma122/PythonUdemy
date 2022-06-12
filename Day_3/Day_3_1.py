############ ODD EVEN ############
number = int(input())

if(number % 2 == 0):
  print("This is an even number.")
else:
  print("This is an odd number.")
############## BMI ###############
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight/(height**2))

weight_string=''
if BMI<18.5:
  weight_string = "underweight"
elif BMI>=18.5 and BMI<25:
  weight_string = "normal weight"
elif BMI>=25 and BMI<30:
  weight_string = "slightly overweight"
elif BMI>=30 and BMI<35:
  weight_string = "obese"
else:
  weight_string = "clinically obese"
print(f"Your BMI is {BMI}, you are {weight_string}.")
########### LEAP YEAR ##############

year = int(input("Which year do you want to check? "))

if year%4==0 and ((year%100!=0) or (year%100==0 and year%400==0)):
  print("Leap year")
else:
  print("Not leap year")
  
################ Roller coster ###############

print("Welcome to the roller coaster!")

height = int(input("What is your height in cm??"))

if height >= 120:
    print("You can ride")
    age = int(input("What's your age? "))
    if age < 12:
        print("Please pay $5. ")
    elif age <= 18:
        print("please pay $7.")
    else:
        print("please pay $12.")
else:
    print("Sorry! You can't ride...")
    
"""

    Multiple if used when we need to implement the below written condition 
                even if the previous condition is true or not

if(condition)
.
.
.
if(condition)
.
.
.
if(condition)
.
.
.

Implements the below written condition only when the previous condition is false
 
 if(condition)
 ...
 elif(condition)
 ...
 else
 ...
 
"""
print("Welcome to the roller coaster!")
bill = 0
height = int(input("What is your height in cm??"))

if height >= 120:
    print("You can ride")
    age = int(input("What's your age? "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12
        
    wants_photo = input("Do you want a photo taken? Y or N. ")
    
    # if wants_photo == 'Y':
    #     print(f"please pay ${bill+3}")
    # else:
    #     print(f"please pay ${bill}.")
    if wants_photo == 'Y':
        bill += 3
    
    print("please pay ${bill}.")
else:
    print("Sorry! You can't ride...")

