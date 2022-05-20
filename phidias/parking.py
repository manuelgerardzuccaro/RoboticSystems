#
#

from phidias.Types import *
from phidias.Lib import *
from phidias.Main import *

class stalls(Belief): pass
class busy(Belief): pass
class arrival(Procedure): pass
class leave(Procedure): pass

def_vars('Floor','Place', 'Total')

arrival() >> [ arrival(1) ]

arrival(Floor) / gt(Floor, 5) >> [ show_line("No places available") ]
arrival(Floor) >> [ arrival(Floor, 1) ]

arrival(Floor, Place) / (stalls(Floor, Total) & gt(Place, Total)) >>  [ "Floor = Floor + 1", arrival(Floor) ]
arrival(Floor, Place) / busy(Floor, Place) >> [ "Place = Place + 1", arrival(Floor, Place) ]
arrival(Floor, Place) >> [ show_line("Postion ", Floor, " ", Place), +busy(Floor, Place) ]

leave(Floor, Place) / busy(Floor, Place) >> [ -busy(Floor, Place) ]

PHIDIAS.assert_belief(stalls(1, 7))
PHIDIAS.assert_belief(stalls(2, 4))
PHIDIAS.assert_belief(stalls(3, 8))
PHIDIAS.assert_belief(stalls(4, 5))
PHIDIAS.assert_belief(stalls(5, 2))



PHIDIAS.run()
PHIDIAS.shell(globals())

