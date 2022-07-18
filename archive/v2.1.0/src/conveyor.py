from pydexarm import Dexarm
import time
dexarm = Dexarm("COM8") # Подключение к Windows

dexarm.conveyor_belt_backward(2500) # speed in mm/sec 
time.sleep(4) # 1 sec = 2.5 cm
dexarm.conveyor_belt_backward(2500) # speed in mm/sec
time.sleep(5) # time in sec
dexarm.conveyor_belt_stop() # stop the conveyor