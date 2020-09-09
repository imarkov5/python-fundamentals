# If no arguments are provided, the function should return a random integer between 0 and 100.
# If only a max number is provided, the function should return a random integer between 0 and the max number.
# If only a min number is provided, the function should return a random integer between the min number and 100
# If both a min and max number are provided, the function should return a random integer between those 2 values.

import random
def randInt(min=0, max=100):
    if min > max:
        return False
    if max < 0:
        return False
    num = round(random.random()*(max-min) +min)
    return num
print(randInt(min=990,max=90))
#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

#from solution file
import random

def randint(min=0, max=100):
  possible_range = max - min
  return round(random.random() * possible_range + min)

print(randint())
print(randint(max=50))
print(randint(min=50))
print(randint(min=50, max=150))

# '''
# This is mostly just a math problem.
# First, we start by getting the possible range of numbers.
# The range will be used to multiply the number created by random, which is between 0 and 1.
# Multiplying this number will give us a number that is no greater than the range, but no less than 0.
# For instance, if we're given 20 and 70, the range is 50, so we'll first start by getting a number between 0 and 50.
# If the minimum is greater than 0, we have to make sure the number cannot be less than the minimum, so we must add the minimum value to our calculated random number.
# Since we've already accounted for the range, if we add 20 (our min from the example) to a number between 0 and 50, then mathematically it cannot be lower than 20 or higher than 70.
# Then we just round to get an integer instead of a float.
# '''