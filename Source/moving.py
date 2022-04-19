from pydexarm import Dexarm
dexarm = Dexarm("COM10") # Подключение к Windows
# device = Dexarm("/dev/tty.usbmodem3086337A34381") # Подключение к MacOS/Linux

dexarm.go_home()

dexarm.move_to(135, 225, 40) # A
dexarm.move_to(120, 210, 40) # B
dexarm.move_to(105, 225, 40) # C
dexarm.move_to(120, 240, 40) # D
dexarm.move_to(135, 225, 40) # D to A

dexarm.go_home()