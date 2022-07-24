from pydexarm import Dexarm
dexarm = Dexarm("COM10") # Подключение к Windows

dexarm.go_home()
dexarm.move_to(135, 225, 0) # A

dexarm.air_picker_place()
dexarm.air_picker_pick() # вдох
dexarm.dealy_ms(1000)

dexarm.go_home()

dexarm.air_picker_place() # выдох
dexarm.dealy_ms(1000)

dexarm.air_picker_stop() # остановка подачи воздуха


