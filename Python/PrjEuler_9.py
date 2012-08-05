"""!
Project Euler
James Munns
"""

import sys, time
from math import sqrt

#=====================================================================
def prjEuler():
    """!
    James Munns
    July 31st, 2012
    Project Euler #9:
        http://projecteuler.net/problem=9
    ( 51.4ms - Work PC )
    """
    a = 1
    for a in range( 1, 1000 ):
        for b in range( 1, 1000 ):
            if( ( sqrt( ( a ** 2 ) + ( b ** 2 ) ) % 1 ) == 0 ):
                if( ( a + b + ( sqrt( ( a ** 2 ) + ( b ** 2 ) ) ) ) == 1000 ):
                    print "The product is %d" % ( a * b * ( sqrt( ( a ** 2 ) + ( b ** 2 ) ) ) )
                    return
        
    return

#=====================================================================
def main():
    time_start = time.clock()
    prjEuler()
    print "Time taken: %.2fms" % ((time.clock() - time_start) * 1000)
    return 0

#=====================================================================
if( __name__ == "__main__" ):
    sys.exit( main() )