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
    Project Euler #7:
        By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
        we can see that the 6th prime is 13.

        What is the 10 001st prime number?
    Submitted N/A - N/A
    ( 49.4s Work PC )
    """
    MAX_ARRAY_LEN = 10001
    primes = [ 2 ]
    iter = 3
    
    while( len(primes) < MAX_ARRAY_LEN ):
        if( largestFactor( iter ) == 1 ):
            primes.append( iter )
        iter += 2
        
    print "The 10,001th prime is %d" % primes[ MAX_ARRAY_LEN - 1]
    return

#=====================================================================
def largestFactor( num, start = None ):
    """!
    Returns the largest factor of a number
    
    Not very efficent
    """
    if ( start == None ):
        start = 1
    else:
        start = ( num / start )
        
    while( start < int( num / 2 ) ):
        start += 1
        if( ( num % start ) == 0 ):
            return ( num / start )
    
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