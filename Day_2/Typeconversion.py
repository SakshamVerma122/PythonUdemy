# Python code to demonstrate Type conversion
# using  ord(), hex(), oct()
  
# initializing integer
s = '4'
  
# printing character converting to integer
c = ord(s)
print ("After converting character to integer : ",end="")
print (c)

# printing ASCII code converting to char
print("Converting ASCII code back to real form")
print(chr(52))
  
# printing integer converting to hexadecimal string
c = hex(56)
print ("After converting 56 to hexadecimal string : ",end="")
print (c)

# printing hexadecimal string converting to integer
cint = int(c,16)
print("Converting hex {} to int {}.".format(c,cint))

# printing integer converting to octal string
c = oct(56)
print ("After converting 56 to octal string : ",end="")
print (c)

# printing octal string converting to integer
cint = int(c,8)
print("Converting octal {} to int {}.".format(c,cint))