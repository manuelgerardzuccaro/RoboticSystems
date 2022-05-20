#
#

from phidias.Types import *
from phidias.Lib import *
from phidias.Main import *

class new_object(Procedure): pass
class empty(Procedure): pass
class tank(Belief): pass
class max_weight(Belief): pass

def_vars('W','X','T','TempW','TempTank', 'Max')

new_object(W) / tank(T, X) >> [ new_object(W, T, X) ]
new_object(W, TempTank, TempW) / (tank(T, X) & lt(X, TempW)) >> [ new_object(W, T, X) ]
new_object(W, TempTank, TempW) >> \
  [ show_line("Selected tank ", TempTank),
        -tank(TempTank, TempW), "TempW = TempW + W", +tank(TempTank, TempW), empty(TempTank)  ]

empty(T) / (tank(T,W) & max_weight(Max) &gt(W, Max) ) >> [ show_line("emptying tank ", T),
                                                               -tank(T,W), +tank(T,0) ]

PHIDIAS.assert_belief(tank('A', 0))
PHIDIAS.assert_belief(tank('B', 0))
PHIDIAS.assert_belief(tank('C', 0))
PHIDIAS.assert_belief(max_weight(20))



PHIDIAS.run()
PHIDIAS.shell(globals())

