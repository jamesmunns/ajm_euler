"""!
Project Euler
James Munns
"""

import sys, time
from EulerLibs import biny

#=====================================================================
CTBTS_LUT = {   0x0 : 0,
                0x1 : 1,
                0x2 : 1,
                0x3 : 2,
                0x4 : 1,
                0x5 : 2,
                0x6 : 2,
                0x7 : 3,
                0x8 : 1,
                0x9 : 2,
                0xA : 2,
                0xB : 3,
                0xC : 2,
                0xD : 3,
                0xE : 3,
                0xF : 4 }

def ctbits( num ):
    sum = 0
    while( num ):
        sum += CTBTS_LUT[ num & 0xF ]
        if( sum > 20 ):
            return -1
        num = num >> 4
    return sum

def prjEuler():
    """!
    James Munns
    [ DATE ]
    Project Euler #n:

    Submitted N/A - N/A
    """
    goodpaths = 0
    for i in range( 0x00000FFFFF, 0xFFFFF00001 ):
        if ctbits( i ) == 20:
            #print bin(i)
            #goodpaths.append( i )
            goodpaths += 1
            if ( ( goodpaths % 100000 ) == 0 ):
                print biny( i, 40 )
    print goodpaths
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