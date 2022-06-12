SUM = 0

for i in range(1,101):
    SUM += i

print(SUM)

############ SUM OF EVEN TILL 100 ########

sum=0

for i in range(2,101,2):
  sum += i

print(sum)

################# FIZZ BUZZ #########
for i in range(1,101):
  if( i % 3 == 0):
    print("Fizz")
    if( i % 5 == 0):
      print("Buzz")
  elif ( i % 5 == 0):
      print("Buzz")
  else:
    print(i)
#####################################

for number in range(1,101):
    if(number % 3 ==0 and number % 5 ==0):
        print("FizzBuzz")
    elif(number % 3 == 0):
        print("Fizz")
    elif(number % 5 == 0):
        print("Buzz")
    else:
        print(i)