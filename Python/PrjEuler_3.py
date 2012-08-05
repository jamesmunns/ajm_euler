"""!
Project Euler
James Munns
"""

import sys, time

#=====================================================================
def prjEuler():
    """!
    James Munns
    July 30th, 2012
    Project Euler #3:
        The prime factors of 13195 are 5, 7, 13 and 29.

        What is the largest prime factor of the number 600851475143 ?
    Submitted July 30th, 2012 - Pass
    (38.1s - Macbook Air)
    (55.3s - Work PC)
    """
    #Constants
    BIG_NUM = 600851475143
    
    cur_num = BIG_NUM
    
    while( cur_num is not 1 ):
        cur_num = largestFactor( BIG_NUM, cur_num )
        print "Attempting %d" % cur_num
        if( largestFactor( cur_num ) == 1 ):
            print "The largest prime factor is %d" % cur_num
            break
    
    
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
        
    if( ( num % 2 ) == 0 ):
        return ( num / 2 )
        
    while( start < int( num / 2 ) ):
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
