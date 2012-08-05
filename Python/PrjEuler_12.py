"""!
Project Euler
James Munns
"""

import sys, time

#=====================================================================
def prjEuler():
    """!
    James Munns
    [ DATE ]
    Project Euler #n:

    Submitted N/A - N/A
    """
    NUM_DIVISORS = 500

    iter_position = 1
    sum = 1

    while( num_factors( sum ) <= NUM_DIVISORS ):
        iter_position += 1
        sum += iter_position

        if( ( iter_position > 2000 ) ):
            print iter_position

    print "Triangle number %d (sum: %d)" % (iter_position, sum )

    return

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

    Somewhat efficient
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
def main():
    time_start = time.clock()
    prjEuler()
    print "Time taken: %.2fms" % ((time.clock() - time_start) * 1000)
    return 0

#=====================================================================
if( __name__ == "__main__" ):
    sys.exit( main() )