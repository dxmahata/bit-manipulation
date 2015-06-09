'''
Created on Jun 9, 2015

@author: Debanjan Mahata
'''
"""
Detect if two integeres have opposite signs
"""

def detect_integer_opposite_signs(x,y):
    """Takes two integers x and y. Returns True if they have opposite signs
    else returns False"""
    assert type(x) == type(y) and type(x) == type(1)
    return (x ^ y) < 0

if __name__ == "__main__":
    print detect_integer_opposite_signs(2,3)
    print detect_integer_opposite_signs(2,-1)
    
    
