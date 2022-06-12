# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random as rm
from datetime import datetime

rm.seed(datetime.now())

mem_pay = names[rm.randint(0,len(names)-1)]

print(f"{mem_pay} is going to buy the meal today!")