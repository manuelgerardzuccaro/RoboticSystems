#
#

from phidias.Types import *
from phidias.Lib import *
from phidias.Main import *

class link(Belief): pass
class path(Procedure): pass

#
def_vars('Src', 'Dest', 'Next', 'Cost', 'P', 'Total', 'CurrentMin', 'CurrentMinCost')

path(Src, Dest) / link(Src, Next, Cost)  >> [ show_line("Next node is ", Src), path(Src, Dest, Next, Cost) ]
path(Dest, Dest)  >> [ show_line("End node is ", Dest) ]

path(Src, Dest, CurrentMin, CurrentMinCost) / (link(Src, Next, Cost) & lt(Cost, CurrentMinCost)) >> \
  [ path(Src, Dest, Next, Cost) ]

path(Src, Dest, CurrentMin, CurrentMinCost)  >> \
  [ path(CurrentMin, Dest) ]


PHIDIAS.assert_belief(link('A', 'B', 3))
PHIDIAS.assert_belief(link('A', 'C', 2))
PHIDIAS.assert_belief(link('A', 'D', 1))

PHIDIAS.assert_belief(link('B', 'F', 2))

PHIDIAS.assert_belief(link('C', 'F', 1))
PHIDIAS.assert_belief(link('C', 'G', 4))

PHIDIAS.assert_belief(link('D', 'E', 2))

PHIDIAS.assert_belief(link('E', 'C', 2))
PHIDIAS.assert_belief(link('E', 'G', 4))

PHIDIAS.assert_belief(link('F', 'G', 2))

PHIDIAS.run()
PHIDIAS.shell(globals())

