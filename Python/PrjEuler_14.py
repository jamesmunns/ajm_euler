"""!
Project Euler
James Munns
"""

import sys, time

COLL_DICT = {}

#=====================================================================
def prjEuler():
    """!
    James Munns
    [ DATE ]
    Project Euler #n:

    Submitted N/A - N/A
    """
    max_len = 1
    res_num = 0

    for cIter in range( 1, 1000000 ):
        temp_len = recColl( cIter )
        if temp_len > max_len:
            max_len = temp_len
            res_num = cIter
    print res_num

    return

def recColl( num ):
    temp_val = None

    #print num
    #raw_input('...')

    if num == 1:
        return 1

    if num in COLL_DICT:
        return COLL_DICT[num]
    else:
        if ( ( num % 2 ) == 0 ):
            temp_val = recColl( num / 2 )
        else:
            temp_val = recColl( 3*num + 1 )
        COLL_DICT[ num ] = temp_val + 1

        return ( temp_val + 1 )

    raise Exception( "Shouldnt get here! - %d", num )



#=====================================================================
def main():
    time_start = time.clock()
    prjEuler()
    print "Time taken: %.2fms" % ((time.clock() - time_start) * 1000)
    return 0

#=====================================================================
if( __name__ == "__main__" ):
    sys.exit( main() )