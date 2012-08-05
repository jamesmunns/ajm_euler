"""!
Project Euler
James Munns
"""

import sys, time

useSTR = 0

#=====================================================================
def prjEuler():
    """!
    James Munns
    July 30th, 2012
    Project Euler #4:
        A palindromic number reads the same both ways. The largest 
        palindrome made from the product of two 2-digit numbers is 
        9009 = 91 99.

        Find the largest palindrome made from the product of two 3-digit numbers.
    Submitted July 30th, 2012 - Pass
    (2.01s - Macbook Air)
    (0.98s Work PC)
    """
    palindromes = []
    for aIter in reversed( range( 100, 1000 ) ):
        for bIter in reversed( range( 100, 1000 ) ):
            if strPalin( aIter * bIter ):
                palindromes.append( aIter*bIter )
    palindromes.sort()
    print "The largest palindrome is %d" % palindromes[-1]
    return

def strPalin(number):
    base = "%d" % number
    for cIter in range( ((len(base)-1)/2) + 1):
        if base[cIter] != base[-1*(cIter+1)]:
            return False
    return True
#=====================================================================
def main():
    time_start = time.clock()
    prjEuler()
    print "Time taken: %.2fms" % ((time.clock() - time_start) * 1000)
    return 0

#=====================================================================
if( __name__ == "__main__" ):
    sys.exit( main() )
