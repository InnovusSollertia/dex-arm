# dex-arm-book

1. Введение
  
  Rotrics Dex ARM - модульный мультифункционыльный робот с точностью выполнения операций до 0,05 мм. С помощью модульной платформы может использоваться как 3D-принтер, лазерный станок, гравер, манипулятор, а также может использовать вместе с конвеером и двумя и более роботами одновременно в одной сети. 

![home1](https://github.com/AndreM07/dex-arm-book/blob/main/pic/home1.jpg)

2. Установка
  
  + Шаг 1 - Системные требования:
    + ОС - Windows, MacOS, Linux
    + Python - [3.10](https://www.python.org/downloads/)
    + Git - [любая версия](https://git-scm.com/downloads)
  
  + Шаг 2 - Установка:
    + После установки Python и IDE, установите следующие пакеты через утилиту `pip`:
      ```bash
      python get-pip.py
      ```
      а также:
      ```bash
      pip install opencv-python
      pip install pyyaml
      pip install pyserial
      ```
    + Скопируйте репозиторий: 
      ```bash
      git clone https://github.com/AndreM07/dex-arm-book
      ```
    + Открываем любую IDE для Python
    + Открываем в IDE загруженный репозиторий
    + Отобразится два файла:
      + "example.py" - содержит пример для запуска робота
      + "pydexarm.py" - содержит библиотеку-интерфейса для общения с роботом на языке Gcode

3. "Hello world"



