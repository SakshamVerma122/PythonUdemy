#https://www.geeksforgeeks.org/type-conversion-python/

# String integers float boolean

print(len(str(678678))) # to get the length of the number 

#Subscripting
print("Hello"[0]) #print first character of a string
print("Hello"[len("Hello")-1])#print last character of a string

#"123"--> #is string and not a number

street_name = "Abbey Road"
print(street_name[4] + street_name[7])


#concatenation
print("123"+"456")

#large numbers
342_456_678#-->computer removes _ Its only for us as to help us dealing with large numbers
mystery = 7_34_529.678
# Can write in both the formats... Indian as well as International
print(mystery)

#float
3.14159

#Boolean
True
False


# len(4567)
print(len(str(4567)))
# as len(int)

num_char = len(input("What's your name??"))
#print("Your name has "+ num_char +"characters.")# This will give TypeError
print("Your name has ",num_char,"characters.")# This will not give any error

#type function
type(num_char)

#type casting
print("Your name has "+ str(num_char) +"characters.")

#Type conversion
a = float("123")#expilcit type conversion
x=70
print(type(70),' ',x+float(100.5))
print(type(x))#impilcit type conversion


#############################################################################
         ########Sum of digits of a 2 digit number#########
two_digit_number = input("Type a two digit number: ")

####################################
#Write your code below this line 👇

sum = int(two_digit_number[0]) + int(two_digit_number[1])

print(sum)

#Operators

3+5
7-4
3 * 2

# Division Operator always give floating point number for answer
print(7/3)
print(type(6/3))

#power
print("Power of operator ",2**3)

#PEMDAS
# ()
# **
# * /
# + -

########################## BMI CALCULATOR ##############################

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

######## ERROR ########
#height = int(height)
#weight = int(weight)


height_float = float(height)
weight_float = float(weight)

print(int(weight_float/(height_float**2)))

################ ROUND OFF #################
print(round(8/3,2))  #this rounds off to 2 decimal places
print(8//3)# int instead of float 

################## fstring################
string="age"
age=12
#print(f"Your {} is {}",string,age)#######ERROR
print(f"Your {string} is {age}")

################### BILL_CALCULATOR ######################
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))

tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

number_people_spilt = int(input("How many people to split the bill? "))

print(f"Each person should pay: ${round((bill+((bill*tip_percentage)/100))/number_people_spilt,2)}")