from pydexarm import Dexarm
dexarm = Dexarm("COM8") # Подключение к Windows
# device = Dexarm("/dev/tty.usbmodem3086337A34381") # Подключение к MacOS/Linux

dexarm.go_home()

dexarm.move_to(135, 225, -70) # A
dexarm.laser_on(1000)
dexarm.move_to(120, 210, -70) # B
dexarm.move_to(105, 225, -70) # C
dexarm.move_to(120, 240, -70) # D
dexarm.move_to(135, 225, -70) # D to A
dexarm.laser_off()

dexarm.go_home()
