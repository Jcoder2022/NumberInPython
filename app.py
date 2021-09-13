# Number
print(10*3)
print(10+3)
print(10-3)
# Two types of division
print(10/3) # returns floating point number
print(10//3) # returns int
print(10%3)# mod return remainder
# exponent ** 10 raised to the power of 3
print (10 ** 3) # will return 1000

# Augmented assignment operator += and x=x=3 are same
x = 10 # let us say we want to add 3
x = x+3
print(x) # o/p will be 13
x += 3
print(x) # o/p will be 16

# we can also multiply,divide and subtract
y=10
print(y)
y*=3
print(y)
y/=3
print(y)
y-=1
print(y)

# Operator precedence

# order of precedence
# parenthesis
# exponentiation  2 ** 3
# multiplication or division
# addition or subtraction

x = 10 + 3 *2 ** 2 # o/p will be 22 because exponentiation will be computed first
print(x)

x = (1+3) *10 -3
print(x)

# Math Functions
# round function
x = 2.9
print(round(x))
# absolute function - Always returns positive representation of value
x = -3
print(abs(x))

# math is module, we need to import it to use its functions
import math
print(math.exp(2))
print(math.ceil(2.9) ) # o/p will be 3
print(math.floor(2.9) ) # o/p will be 2
# google python 3 math module
print(math.factorial(5))

