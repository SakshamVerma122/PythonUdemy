"""
1. random.seed() 
    
    a>sets the seed for random number generation.
    
    b>To generate a new random sequence, a seed must be set depending on the 
     current system time{reason: as system time keeps on changing hence 
     random number keeps on changing }.

2. getstate()
    
    a>Returns an object containing the current state of the generator. 
    
    b>To restore the state, pass the object to setstate()

3. setstate(state_obj)

    a> This restores the state of the generator at the point when getstate() 
       was called, by passing the state object.

4. getrandbits(k)
   
   a> This returns a Python integer with k random bits. 
   b> Useful for methods like randrange() to handle 
      arbitrary large ranges for random number generation.
      
"""
# >>> import random
# >>> random.getrandbits(100) # Get a random integer having 100 bits
# 802952130840845478288641107953



import random
from datetime import datetime 

random.seed(datetime.now())
 
# Get the state of the generator
state = random.getstate()
 
print('Generating a random sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))
 
# Restore the state to a point before the sequence was generated
random.setstate(state)
print('Generating the same identical sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))