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
    sum = 0
    big_num = 2 ** 1000
    for cIter in str( big_num ):
        sum += int(cIter)
    print sum
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