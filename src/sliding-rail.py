from pydexarm import Dexarm
import time
dexarm = Dexarm(port="COM6")

dexarm.go_home()
dexarm.sliding_rail_init()
dexarm.move_to(0,100,300,0)
dexarm.move_to(0,150,300,100)
dexarm.move_to(10,100,275,50)
dexarm.move_to(0,100,250,200)

