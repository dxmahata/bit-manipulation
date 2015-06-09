'''
Created on Jun 9, 2015

@author: Debanjan
'''

"""
Compute the integer absolute value (abs) without branching
"""

"""
Comments from http://www.geeksforgeeks.org/compute-the-integer-absolute-value-abs-without-branching/
We need not to do anything if a number is positive. 
We want to change only negative numbers. Since negative numbers are stored in 2s complement form, 
to get the absolute value of a negative number we have to toggle bits of the number and add 1 to the result.

For example -2 in a 8 bit system is stored as follows 1 1 1 1 1 1 1 0 where leftmost bit is the sign bit. 
To get the absolute value of a negative number, we have to toggle all bits and add 1 to the toggled number 
i.e, 0 0 0 0 0 0 0 1 + 1 will give the absolute value of 1 1 1 1 1 1 1 0. 
Also remember, we need to do these operations only if the number is negative (sign bit is set).

Method 1
1) Set the mask as right shift of integer by 31 (assuming integers are stored using 32 bits).

 mask = n>>31 
2) For negative numbers, above step sets mask as 1 1 1 1 1 1 1 1 and 0 0 0 0 0 0 0 0 for positive numbers. 
Add the mask to the given number.

 mask + n
  
3) XOR of mask +n and mask gives the absolute value.

 (mask + n)^mask
"""

import sys


def sign_of_an_integer(x):
    """Takes an integer, returns -1 if the sign of the integer
    is negative else returns 0"""
    assert type(x) == type(1)
    return (x >> sys.getsizeof(x)-1)


def abs_val_of_int_1(x):
    """Takes an integer and returns its absolute value"""
    assert type(x) == type(1)
    if sign_of_an_integer(x) == 0:
        return x
    else:
        mask = x >> sys.getsizeof(x)-1
        return (mask + x) ^ mask
    


"""
Method 2:
1) Set the mask as right shift of integer by 31 (assuming integers are stored using 32 bits).

 mask = n>>31 
2) XOR the mask with number

 mask ^ n 
3) Subtract mask from result of step 2 and return the result.

 (mask ^ n) - mask 
"""

def abs_val_of_int_2(x):
    """Takes an integer and returns its absolute value"""
    assert type(x) == type(1)
    if sign_of_an_integer(x) == 0:
        return x
    else:
        mask = x >> sys.getsizeof(x)-1
        return (mask ^ x) - mask


if __name__ == "__main__":
    print abs_val_of_int_1(-2)
    #print abs_val_of_int_1(-2.00)
    print abs_val_of_int_1(-100)
    print abs_val_of_int_1(300)
    
    print abs_val_of_int_2(-2)
    #print abs_val_of_int_2(-2.00)
    print abs_val_of_int_2(-100)
    print abs_val_of_int_2(200)
    

    