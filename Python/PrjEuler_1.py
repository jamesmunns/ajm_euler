"""!
iop_dis System Test

PEST system test for iop_dis
"""

import sys, time

#=====================================================================
def prjEuler():
    """!
    James Munns
    July 30th 2012
    Project Euler #1:
        If we list all the natural numbers below 10 that are multiples
        of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

        Find the sum of all the multiples of 3 or 5 below 1000.
        
    Submitted 7/30/12 - Pass
    """
    MAX_VAL   = 1000
    MULT_LIST = [ 3, 5 ]
    
    sum = 0
    
    for valIter in range( MAX_VAL ):
        for multIter in MULT_LIST:
            if ( not ( valIter % multIter ) ):
                sum += valIter
                break

    print "The sum is %d" % sum
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