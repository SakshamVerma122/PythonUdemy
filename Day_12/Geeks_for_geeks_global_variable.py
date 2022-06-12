# https://www.geeksforgeeks.org/global-local-variables-python/
# This function uses global variable s
def f():
	print(s)

f()

# Global scope
s = "I love Geeksforgeeks"

# Here you will see an error as s is defined after f() is being called
#########################################

def f():
	print(s)

# Global scope
s = "I love Geeksforgeeks"

f()

##################################3#######

def f():
    print(s)
 
    # This program will NOT show error
    # if we comment below line.
    s = "Me too."
 
    print(s)
 
# Global scope
s = "I love Geeksforgeeks"
f()
print(s)

# We only need to use the global keyword in a function if we want to do assignments
#  / change them. global is not needed for printing and accessing.