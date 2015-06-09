'''
Created on Jun 9, 2015

@author: Debanjan Mahata
'''
"""
Compute the sign of an integer
"""

import sys

def sign_of_an_integer(x):
    """Takes an integer, returns -1 if the sign of the integer
    is negative else returns 0"""
    assert type(x) == type(1)
    return (x >> sys.getsizeof(x)-1)

        
        
    

if __name__ == "__main__":
    print sign_of_an_integer(-100.0)
    print sign_of_an_integer(2)
    print sign_of_an_integer(-3)