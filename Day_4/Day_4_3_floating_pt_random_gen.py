"""
            Generating Random floating point numbers

Similar to generating integers, there are functions that generate random floating 
                        point sequences.

random.random() -> 
    
    a>Returns the next random floating point number between [0.0 to 1.0)
    
    b> To get the range from 0 - 5  -->5 * random.random()
                                                         
random.uniform(a, b) -> 

    a>Returns a random floating point N such that a <= N <= b if a <= b and 
    
    b <= N <= a if b < a.

random.expovariate(lambda) -> 

    a>Returns a number corresponding to an exponential distribution.

random.gauss(mu, sigma) -> 

    a>Returns a number corresponding to a gaussian distribution.
    
    b>There are similar functions for other distributions, 
    such as Normal Distribution, Gamma Distribution, etc.
 
 """

import random
 
print('Random number from 0 to 1 :', random.random())
print('Uniform Distribution between [1,5] :', random.uniform(1, 5))
print('Gaussian Distribution with mean = 0 and standard deviation = 1 :', random.gauss(0, 1))
print('Exponential Distribution with lambda = 0.1 :', random.expovariate(0.1))
print('Normal Distribution with mean = 1 and standard deviation = 2:', random.normalvariate(1, 5))
