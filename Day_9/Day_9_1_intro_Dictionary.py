#                      Dictionary in python
#                 Dictionary has keys and values
#    {Key_1:value_1 , Key_2:value_2 , Key_3:value_3 , Key_4:value_4}

programming_dictionary = {
    "Bug":"An error in the programme",
   "Function":"piece of that remove redundancy",
   "Loops":"The action taht can be repeated again and again",
}

# It's a good practice to put ',' at the last of the dictionary


# Retrieving item from dictionary.
print(programming_dictionary["Bug"])

# Adding new items to dictionary.
programming_dictionary["Lists"] = "Similary to linked lists in C++"


# empty dictionary
empty_dictionary=[]

# Wipe an entire dictionary
# programming_dictionary = {}
# print(programming_dictionary)


# Edit a key inside a dictionary
# if not able to find anything like that inside the dictionary similar to Line 18
programming_dictionary["Lists"] = "linked lists"

#Looping through a dictionary
# this gives keys
for keys in programming_dictionary:
    print(keys)
    print(programming_dictionary[keys])