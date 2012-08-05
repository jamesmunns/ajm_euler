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
    Project Euler #5:
        2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

        What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?   
    Submitted July 30th, 2012 - Pass
    (4.8s Macbook Air)
    (2.8s Work PC)
    """
    HIGHEST_MULT = 20
    
    num = HIGHEST_MULT
    while( not recMult( num, HIGHEST_MULT-1 ) ):
        num += HIGHEST_MULT
    
    print "The smallest number is %d" % num
        
    return

#=====================================================================
def recMult( num, mult ):

    if( mult == 1 ):
        return True

    if( (num % mult) == 0 ):
        return recMult( num, mult-1 )
    else:
        return False
    
#=====================================================================
def main():
    time_start = time.clock()
    prjEuler()
    print "Time taken: %.2fms" % ((time.clock() - time_start) * 1000)
    return 0

#=====================================================================
if( __name__ == "__main__" ):
    sys.exit( main() )
