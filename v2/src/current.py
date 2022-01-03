from pydexarm import Dexarm
import time
dexarm = Dexarm("COM8") # Подключение к Windows

# B  = 0 300 25
# A  = -260 0 0 // or 220
# A- = -260 0 -30 // or 220

dexarm.go_home()

dexarm.move_to(-260, 0, 0) #  to A

dexarm.conveyor_belt_backward(2500) # speed in mm/sec 
time.sleep(4) # 1 sec = 2.5 cm
dexarm.conveyor_belt_stop() # stop the conveyor

dexarm.soft_gripper_place() # разжать
dexarm.dealy_ms(1000)

dexarm.move_to(-260, 0, -30) # down to A

dexarm.soft_gripper_pick() # зажать
dexarm.dealy_ms(2000)

dexarm.move_to(-260, 0, 30) # up from A

dexarm.move_to(0, 300, 25) # to B

dexarm.soft_gripper_place() # разжать
dexarm.dealy_ms(1000)
dexarm.soft_gripper_stop()

dexarm.go_home() 

# speed conveyor - 100 to 5000

# dexarm.conveyor_belt_forward(2500) # speed in mm/sec 
# time.sleep(5) # time in sec
# dexarm.conveyor_belt_backward(2500) # speed in mm/sec
# time.sleep(5) # time in sec
# dexarm.conveyor_belt_stop() # stop the conveyor




