"""!
Project Euler
James Munns
"""

import sys, time

GOOD_SOLN = []
SIZE_TRVS = ( 10 ) + 1 #n steps requires n+1 nodes


class path( object ):
    xpos = 1
    ypos = 1
    path = ''
    ident = -1

    def __init__( self, UIN ):
        self.ident = UIN
#        print "NEW!"
 #       print self.xpos
  #      print self.ypos
   #     print self.path
    #    print "-----"
     #   raw_input( '...' )

    def __del__( self ):
        pass
#        print "Bye!"
 #       print self.xpos
  #      print self.ypos
   #     print self.path
    #    print "-----"

def recMove( boat ):

    if( ( boat.xpos == SIZE_TRVS ) and ( boat.ypos == SIZE_TRVS ) ):
        for soln in GOOD_SOLN:
            if boat.path in soln:
                return False

        GOOD_SOLN.append( boat.path )
        print boat.path
        return True

    #if( ( boat.xpos == SIZE_TRVS ) or ( boat.ypos == SIZE_TRVS ) ):


    #Rightward movement
    if( boat.xpos < SIZE_TRVS ):
        boat.xpos += 1
        boat.path = boat.path + 'r'
        if( recMove( boat ) ):
            return True
        else:
            boat.xpos -= 1
            boat.path = boat.path[:-1]

    #Downward movement
    if( boat.ypos < SIZE_TRVS ):
        boat.ypos += 1
        boat.path = boat.path + 'd'
        if( recMove( boat ) ):
            return True
        else:
            boat.ypos -= 1
            boat.path = boat.path[:-1]


    #print boat.path
    return False

#=====================================================================
def prjEuler():
    """!
    James Munns
    [ DATE ]
    Project Euler #n:

    Submitted N/A - N/A
    """
    ret_val = True
    l_UIN = 0
    while( ret_val ):
        l_UIN += 1
        ret_val = recMove( path(l_UIN) )

    #print GOOD_SOLN
    print len(GOOD_SOLN)
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