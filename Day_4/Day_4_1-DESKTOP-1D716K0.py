# Mersenne twister-> https://en.wikipedia.org/wiki/Mersenne_Twister

# Pseudo random number generator-> https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators

# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

import random

import Day_4_2_module #This is a file that is defined in the same file

random_integer = random.randint(1,10)
print(random_integer)

print(Day_4_2_module.pi)# This is a variable that is defined in the same file and imported via use of module

