# Code intelligence for spyder
# installing Thony for see how the code is executed....


#Setting the variable type explicitly
my_city = str("New York")
print(type(my_city))

# "String manipulation"--> Use geeks
# https://www.freecodecamp.org/news/python-string-manipulation-handbook/
# https://www.programiz.com/python-programming/string
print("Hello World!\nHello World!\nHello World!\n")

print("print('Saksham')")
print('print("Saksham")')

#String concatenation
# Concatenation is when you have two or more strings and you want to join them into one.
print("Hello"+" "+"Saksham")

# Indentation Error
#    print("Hello"+" "+"Saksham")

# Syntax_Error
# print("Saksham Verma)"


##############################input()#####################################


input("What is your name?")

print("Hello"+input("What is your name?"))

######################Showing size of the input string####################
print( len( input() ) )
# This will not store input instead will directly give len as output
##########################################################################

                            #######SWAPPING#######
                            
a =  input()
b =  input()

a,b = b,a

            ###################### NAMING VARIABLE ################

nama ="Jack"
#  print(name)  #NameError: name 'name' is not defined

##########################################################################

                            #check wh it's valid
input = "Saksham"

print(input)

# But after the above 
# >>> s = input()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object is not callable
##########################################################################

print("Welcome to the Band Name Generator.")

street = input("What's name of the city you grew up in?")
pet = input("What's your pet's name?")
print("Your band name could be " + street + " " + pet)

# print() automatically sends the cursor to the new line


# Replace Part of a String
'Rio de Janeiro'.replace('Rio', 'Mar')
# you can replace substring with string of any size whether smaller or bigger

# How to Count
word = "Rio de Janeiro"
print(word.count(' '))
# counting how many spaces exist in

# How to Repeat a String
words = "Tokyo" * 3 
print(words)

# Split a String in Python
my_phrase = "let's go to the beach"
my_words = my_phrase.split(" ")

# by default, the split() method uses any consecutive number of whitespaces as delimiters.
for word in my_words:
    print(word)

print(my_words)

# spliting on the basis of ";"
my_csv = "mary;32;australia;mary@email.com"
my_data = my_csv.split(";")

for data in my_data:
    print(data)

# Remove All White Spaces in a String in Python
# \s represents not only space ' ', but also form feed \f, line feed \n, carriage return \r, tab \t, and vertical tab \v.

# In summary, \s = [ \f\n\r\t\v]

