"""!
Project Euler
James Munns
"""

import sys

def biny( num, width = 32 ):
    temp_str = bin( num )[2:]
    while len( temp_str ) < width:
        temp_str = '0' + temp_str
    return '0b' + temp_str


#=====================================================================
def num_factors( num ):
    """!
    Counts the number of factors a number has.
    """
    sum = 0
    last_factor = None

    while( last_factor != 1 ):
        last_factor = largestFactor( num, last_factor )
        sum += 1
    return sum

#=====================================================================
def largestFactor( num, start = None ):
    """!
    Returns the largest factor of a number

    Meh efficiency
    """
    if ( start == None ):
        start = 2
    else:
        start = ( ( num / start ) + 1 )

    end = int( num / 2 )

    while( start < end ):
        if( ( num % start ) == 0 ):
            return ( num / start )
        start += 1

    return 1

#=====================================================================
if( __name__ == "__main__" ):
    sys.exit( )