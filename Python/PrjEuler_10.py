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
    Project Euler #10:
        The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

        Find the sum of all the primes below two million.
    Submitted N/A - N/A
    """
    MAX_VAL = 2000000
    sum = 2
    iter = 3
    primes = [ 2 ]

    while( iter < MAX_VAL ):
        if( largestFactor( iter ) == 1 ):
            sum += iter
            primes.append( iter )
            if( ( len( primes ) % 10000 ) == 0 ):
                print iter
        iter += 2

    print "Write all primes to a file for posterity"
    fOUT = file( "2mPrimes.txt", 'w' )
    for pIter in primes:
        fOUT.write( pIter )
    fOUT.close()

    print "The sum of all primes is %d" % sum
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

    if( (num % 2 ) == 0 ):
        return (num/2)

    end = int( num / 2 )

    while( start < end ):
        start += 2
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