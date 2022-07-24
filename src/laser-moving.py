from pydexarm import Dexarm
dexarm = Dexarm("COM8") # Подключение к Windows

dexarm.go_home()

dexarm.move_to(135, 225, -70) # точка A
dexarm.laser_on(255) # включение лазера
dexarm.move_to(120, 210, -70) # точка B
dexarm.move_to(105, 225, -70) # точка C
dexarm.move_to(120, 240, -70) # точка D
dexarm.move_to(135, 225, -70) # от точки D к точки A
dexarm.laser_off() # выключение лазера

dexarm.go_home()


