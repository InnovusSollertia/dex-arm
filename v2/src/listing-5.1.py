from pydexarm import Dexarm
dexarm = Dexarm("COM8") # Подключение к Windows
# device = Dexarm("/dev/tty.usbmodem3086337A34381") # Подключение к MacOS/Linux

dexarm.go_home()
dexarm.move_to(135, 225, -15) # A

dexarm.air_picker_pick() # вдох
dexarm.dealy_ms(1000)

dexarm.go_home()

dexarm.air_picker_place() # выдох
dexarm.dealy_ms(1000)

dexarm.air_picker_stop() # остановка подачи воздуха
