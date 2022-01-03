from __future__ import division
import cv2
import numpy as np
import time
import sys
import os
icol1 = (89, 0, 0, 125, 255, 255)  # Blue
icol2 = (0, 100, 80, 10, 255, 255)   # Red
from pydexarm import Dexarm
dexarm = Dexarm("COM8") 

cap = cv2.VideoCapture(0) # Вебкамера № 1 используется для захвата кадров
while(1):  # Это приводит программу в бесконечный цикл     
    _, frame1 = cap.read() # Захватывает прямую трансляцию покадрово
    _, frame2 = cap.read() # Захватывает прямую трансляцию покадрово

    hsv1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV) # Преобразует изображения из BGR в HSV (синий)
    hsv2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV) # Преобразует изображения из BGR в HSV (красный)
    
    lower_red = np.array([110,50,50])
    upper_red = np.array([130,255,255])

    lower_green = np.array([89,0,0])
    upper_green = np.array([125,255,255])

# Здесь мы определяем диапазон синего цвета в HSV
# Это создает маску синего цвета
# объекты найдены в кадре.

mask1 = cv2.inRange(hsv1, lower_red, upper_red)
mask2 = cv2.inRange(hsv2, lower_blue, upper_blue)
  
# Битовая и рама и маска делается так
# что подсвечены только синие объекты
# и хранится в Res

res1 = cv2.bitwise_and(frame1,frame1, mask= mask1)
res2 = cv2.bitwise_and(frame2,frame2, mask= mask1)

cv2.imshow('frame',frame1)
cv2.imshow('frame',frame2)

cv2.imshow('mask',mask1)
cv2.imshow('mask',mask2)

cv2.imshow('res',res1)
cv2.imshow('res',res2)
  
# Это отображает рамку, маску
# и res, которые мы создали в 3 отдельных окнах.




cap.release() # освободить захваченный кадр