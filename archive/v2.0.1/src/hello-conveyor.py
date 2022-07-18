from pydexarm import Dexarm
import time
dexarm = Dexarm("COM8") # Подключение к Windows
# device = Dexarm("/dev/tty.usbmodem3086337A34381") # Подключение к MacOS/Linux

# dexarm.move_to(0,240,25)

# speed conveyor - 100 to 5000

dexarm.conveyor_belt_forward(5000) # speed in mm/sec 
time.sleep(5) # time in sec
dexarm.conveyor_belt_backward(5000) # speed in mm/sec
time.sleep(5) # time in sec
dexarm.conveyor_belt_stop() # stop the conveyor




