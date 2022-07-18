from pydexarm import Dexarm
dexarm = Dexarm("COM6") # Подключение к Windows
# device = Dexarm("/dev/tty.usbmodem3086337A34381") # Подключение к MacOS/Linux

dexarm.go_home()
dexarm.move_to(45, 205, -20) # A
dexarm.go_home()
