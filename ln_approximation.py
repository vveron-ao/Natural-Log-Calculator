# import math functions for exact log calculation
from math import *

# take user input for x value
x = float(input("Enter a value for x: "))

# while statement to evaluate if x is within the range of calculation
while x <= 0 or x > 2:
    x = float(input("Out of range! Try again: "))
print("")

# input for the tolernce from user console
tolerance = float(input("Enter the tolerance: "))
expon_divisor = 1

# use the log function to compute the exact log
exact = float(log(x))
print("")
totequation = 0

# set the equation for log expansion as a variable
equation = (x - 1) ** expon_divisor / expon_divisor

# while statement to calculate repeat the equation until it is equal to the tolerance or greater
while abs(equation) >= tolerance:
    if (expon_divisor % 2) == 0:
        totequation -= equation
    else:
        totequation += equation
        # add one to the exponent and demoninator each time the equation repeats.
    expon_divisor += 1
    equation = (x - 1) ** expon_divisor / expon_divisor
    #reseting the value of operation

print(f'ln({x}) is approximately {float(totequation)}')
print(f'ln({x}) is exactly {exact}')

# calculate the difference 
diff = totequation - exact
# if statement to evaluate if there is more than four zeros past the decimal point, in which case the difference is displayed
# in scientific notation.
if diff < 0:
    diff = diff * -1
if diff > 0.00001 or diff == 0:
    print(f'The difference is {diff}')
else:
    print(f'The difference is {diff:e}')
