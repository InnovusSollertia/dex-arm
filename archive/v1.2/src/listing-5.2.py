from pydexarm import Dexarm
dexarm = Dexarm("COM8") # Подключение к Windows
# device = Dexarm("/dev/tty.usbmodem3086337A34381") # Подключение к MacOS/Linux

dexarm.go_home()

dexarm.fast_move_to(135, 225, -40) # A

dexarm.soft_gripper_place() # выдох
dexarm.dealy_ms(1000)

dexarm.soft_gripper_pick() # вдох
dexarm.dealy_ms(1000)

dexarm.go_home()

dexarm.soft_gripper_place() # выдох
dexarm.dealy_ms(1000)

dexarm.soft_gripper_stop() # остановка подачи воздуха
