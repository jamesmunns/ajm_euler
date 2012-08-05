"""!
Project Euler
James Munns
"""

import sys, time

#=====================================================================
def prjEuler():
    """!
    James Munns
    July 31st, 2012
    Project Euler #6:
        The sum of the squares of the first ten natural numbers is,
        1^2 + 2^2 + ... + 10^2 = 385
        
        The square of the sum of the first ten natural numbers is,
        (1 + 2 + ... + 10)^2 = 552 = 3025
        
        Hence the difference between the sum of the squares of the 
        first ten natural numbers and the square of the sum is 
        3025 - 385 = 2640.
        
        Find the difference between the sum of the squares of the 
        first one hundred natural numbers and the square of the sum.
    Submitted July 31st, 2012 - Pass
    (0.46ms - Work PC)
    """
    #Constants
    UPPER_LIMIT = 100
    
    sum_sq = 0
    sq_sum = 0
    
    for i in range(1, UPPER_LIMIT+1):
        sum_sq += (i**2)
        sq_sum += i
    sq_sum = ( sq_sum ** 2 )
    
    print "The difference between the sums is %d" % ( sq_sum - sum_sq )
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