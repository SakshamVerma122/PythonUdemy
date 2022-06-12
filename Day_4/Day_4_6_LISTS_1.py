#https://docs.python.org/3/tutorial/datastructures.html

#  lists->datastructure
#  Organising and storing piece of data

friuts = ["Saksham","Shubham"]

a = 10
b = 20

num=[a,b]

############# STORING STATES OF US #############

states_of_us = ["New york","California"]

print(*states_of_us)

print(states_of_us[0])
print(states_of_us[1])

print(states_of_us[-1]) # last item / First item from the end
print(states_of_us[-2]) # Second item from the end

########### Altering item from the list #########

states_of_us[0] = "Saksham_land"

##################################################

states_of_us.append("Shubham_land")

##################################################

states_of_us.extend(["Neelam","Sanjay"])

print(*states_of_us)
################ Concatenation of lists###########
a = [1, 2]
b = [3, 4]

a += b

print(a)

############# The list slicing syntax ##############

a[len(a):] = b

# Output: [1, 2, 3, 4]
print('a =', a)