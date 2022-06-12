# https://www.geeksforgeeks.org/mutable-vs-immutable-objects-in-python/
# Every variable in python holds an instance of an object.
# There are two types of objects in python i.e.
#
# * Mutable Objects : These are of type list, dict, set . Custom classes are generally mutable.
# * Immutable Objects : These are of in-built types like int, float, bool, string, unicode, tuple. In simple words, an immutable object can’t be changed after it is created.
#
# Whenever an object is instantiated, it is assigned a unique **object id.**
#
# The `type of the object` is defined at the `runtime` and it `can’t be changed afterwards`. However, it’s `state` can be `changed` if it is a `mutable object`.

x = 10
# Here 10 is an object of type int and 10's datatype can't be changed afterwards

y = x
y += 1
print("y: ",y)

y = [1,2,3,4,5,6]
# Here [1,2,3,4,5,6] is an object of type list and [1,2,3,4,5,6]'s datatype can't be changed further

print("y: ",y)
y = "Saksham"
print(type(y))

print("y: ",y)
print("x: ",x)

print(type([1,2,3,4,5,6]))

x = []
y = x
y.append(10)

print(y)
print(x)
"""There are two factors that produce this result:

Variables are simply names that refer to objects. Doing y = x doesn’t create a copy of the list – it creates a new variable y that refers to the same object x refers to. This means that there is only one object (the list), and both x and y refer to it.

Lists are mutable, which means that you can change their content.

After the call to append(), the content of the mutable object has changed from [] to [10]. Since both the variables refer to the same object, using either name accesses the modified value [10]."""

x = 5  # ints are immutable
y = x
x = x + 1  # 5 can't be mutated, we are creating a new object here
print(x)
print(y)