from pydexarm import Dexarm
dexarm = Dexarm("COM10") # Подключение к Windows

dexarm.go_home()
dexarm.fast_move_to(135, 225, -40) # A
dexarm.soft_gripper_place() # разжать щупальцу

dexarm.dealy_ms(1000)
dexarm.soft_gripper_pick() # зажать щупальцу

dexarm.dealy_ms(1000)
dexarm.go_home()

dexarm.soft_gripper_place() # разжать щупальцу
dexarm.dealy_ms(1000)

dexarm.soft_gripper_stop() # остановка подачи воздуха

