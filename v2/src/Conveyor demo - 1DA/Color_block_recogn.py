import cv2
import numpy as np
import math
from numpy import *
from Cam_dev import *
from collections import Counter
from Serial_tool import *

global Com_dev1
global Com_dev2

color = {
    "red" :   {"pos":[-330,80],"num":0,"min":0,"max":10},
    "green" : {"pos":[-270,80],"num":0,"min":35,"max":77},
    "blue" :  {"pos":[-210,80],"num":0,"min":100,"max":124},
    "yellow" :  {"pos":[-270,130],"num":0,"min":24,"max":34},
    # "purple" :  {"pos":[-270,130],"num":0,"min":125,"max":155}
    }    

# Grab blocks from the slide
get_color_block = [-105,233,50]
# Block starting position
obj_start_pos=[38,225]


'''Mark the image to assist in calibration'''
def draw_pos(img):
    size = 15
    line_w = 2
    img_half_w = 320
    img_half_h = 240

    # Draw a cross with an offset from the center
    
    diff=[220,220]
    cv2.line(img,(img_half_w-size-diff[0],img_half_h), (img_half_w+size-diff[0],img_half_h), (0, 0, 0), line_w)
    cv2.line(img,(img_half_w-diff[1],img_half_h-size), (img_half_w-diff[1],img_half_h+size), (0, 0, 0), line_w)    

    diff=[-220,-220]
    cv2.line(img,(img_half_w-size-diff[0],img_half_h), (img_half_w+size-diff[0],img_half_h), (0, 0, 0), line_w)
    cv2.line(img,(img_half_w-diff[1],img_half_h-size), (img_half_w-diff[1],img_half_h+size), (0, 0, 0), line_w)    

    diff=[220,220]
    cv2.line(img,(img_half_w-size,img_half_h-diff[0]), (img_half_w+size,img_half_h-diff[0]), (0, 0, 0), line_w)
    cv2.line(img,(img_half_w,img_half_h-size-diff[1]), (img_half_w,img_half_h+size-diff[1]), (0, 0, 0), line_w)    

    diff=[-220,-220]
    cv2.line(img,(img_half_w-size,img_half_h-diff[0]), (img_half_w+size,img_half_h-diff[0]), (0, 0, 0), line_w)
    cv2.line(img,(img_half_w,img_half_h-size-diff[1]), (img_half_w,img_half_h+size-diff[1]), (0, 0, 0), line_w)    
    pass

'''Identify the hsv value of a certain area'''
'''The area is represented by a cross'''
def recogn_area_hsv(img):

    size = 20
    img_half_w = 240
    img_half_h = 320
   
    hsv_h=[]
    hsv_s=[]

    num = 0
    for i in range(img_half_w - size,img_half_w + size):
        num = num+1 
        hsv_h.insert(num,(img[img_half_h,i][0]))  # [y,x]    
        cv2.circle(img, (img_half_h,i), 1, (0, 0, 255), 2)
    # print(hsv_h)

    num = 0
    for i in range(img_half_h - size,img_half_h + size):
        num = num+1 
        hsv_s.insert(num,(img[i,img_half_w][0]))  # [y,x]    
        cv2.circle(img, (i,img_half_w), 1, (0, 0, 255), 2)
    # print(hsv_s)

    hsv = hsv_h + hsv_s
    # print(hsv)

    h_data = {  'aver_val' : mean(hsv),
                'max_val' : max(hsv),
                'min_val' : min(hsv),
                'mid_val' : median(hsv),
                'mum_val' : int(np.argmax(np.bincount(hsv))),
                'data_group' : Counter(hsv),
                'len' : len(Counter(hsv))
                }
    # print(h_data)
    return h_data


def find_color(data):
    
    if data['mum_val'] >= color["red"]["min"] and data['mum_val'] <= color["red"]["max"] :
        # print("red")
        return "red"
    elif data['mum_val'] >= color["green"]["min"] and data['mum_val'] <= color["green"]["max"] :
        # print("green")
        return "green"
    elif data['mum_val'] >= color["blue"]["min"] and data['mum_val'] <= color["blue"]["max"] :
        # print("blue")
        return "blue"
    elif data['mum_val'] >= color["yellow"]["min"] and data['mum_val'] <= color["yellow"]["max"] :
        # print("yellow")
        return "yellow" 
    # elif data['mum_val'] >= color["purple"]["min"] and data['mum_val'] <= color["purple"]["max"] :
    #     print("purple")
    #     return "purple"  
    return None              


''' demo '''
def recogn_main():
    status = True
    while status:
        img = video.get_img(0)
        # img = cv2.flip(img,0,dst=None) 
        draw_pos(img)
        
        cv2.imshow("src_img", img)     
        # hsv
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        data = recogn_area_hsv(hsv)
        cv2.imshow("hsv_img", hsv)   
        cv2.waitKey(30) 

        tar_key = find_color(data)
        # Determine whether there is a single-tone block according to the type of color gamut
        if(data['len'] <= 8 ) and (data['data_group'][data['mum_val']]>=25) and (tar_key is not None):
            print(data)
            print(tar_key)

            Com_dev1.send(gcode.slide(0))

            color[tar_key]["num"] = color[tar_key]["num"] + 1 
            i = color[tar_key]["num"]
            # The location of the wooden block on the slide
            temp = get_color_block
            Com_dev1.send(gcode.XYZ(temp[0],temp[1],temp[2])) 
            # Z
            Com_dev1.send(gcode.Z(temp[2]-10)) 
            # Inhale
            Com_dev1.send(gcode.M100x(0))     
            # Z
            Com_dev1.send(gcode.Z(temp[2]+30))
            # tar pos
            pos = color[tar_key]["pos"]
            Com_dev1.send(gcode.XYZ(pos[0],pos[1],-25+30*i+20))           
            #Z
            Com_dev1.send(gcode.Z(-30-40+30*i))
            #Air leak
            Com_dev1.send(gcode.M100x(2))
            # Rise, avoid hitting
            Com_dev1.send(gcode.Z(-25+30*i+20))
            # Back to the predicted position
            Com_dev1.send(gcode.XYZ(temp[0],temp[1],temp[2]))            
            status = False
            img = video.get_img(0)

        # print("Tonal type "+str(data['len']))

        cv2.waitKey(30) 


    pass

global obj_num
obj_num = 0

global status
status = True


def place_pos():
    global obj_num
    global status
    integer = 0
    remainder = 0
    integer = obj_num // 4   
    remainder = obj_num % 4 
    # print([integer,remainder])
    pos_x = obj_start_pos[0] - remainder * 30
    pox_y= obj_start_pos[1] + integer * 30
    obj_num = obj_num + 1
    if obj_num > 15:
        obj_num = 0
        status = False
    return [pos_x,pox_y]


def move_obj():
    global Com_dev1
    global Com_dev2    
    global status


    skip_num = 30
    while skip_num:
        img = video.get_img(0)
        img = cv2.flip(img,0,dst=None) 
        draw_pos(img)
        cv2.imshow("src_img", img)    
        skip_num = skip_num - 1
        cv2.waitKey(30) 

    while status:
        
        # open slide
        Com_dev1.send(gcode.slide(0))

        # temp = place_pos()
        # print(temp)
        # Com_dev2.send(gcode.XYZ(temp[0],temp[1],0))
        # # Z
        # Com_dev2.send(gcode.Z(-37))
        # # Inhale
        # Com_dev2.send(gcode.M100x(0))#
        # # line mode
        # Com_dev2.send(gcode.line_mode())
        # # Z
        # Com_dev2.send(gcode.Z(60)) 
        # # quick mode       
        # Com_dev2.send(gcode.quick_mode())                            
        # # Place on the conveyor belt
        # Com_dev2.send(gcode.XYZ(160,170,45)) 
        # # discouraged
        # Com_dev2.send(gcode.M100x(2))     
        # # Z
        # Com_dev2.send(gcode.Z(100))
        # # M1111
        # Com_dev2.send(gcode.XYZ(0,300,0))
        # open slide
        Com_dev1.send(gcode.slide(1))   

        recogn_main()  

    Com_dev1.send(gcode.init())
    # Com_dev2.send(gcode.init())

    
    pass

if __name__ == "__main__":
    global Com_dev1
    # global Com_dev2

    video.open(1,640,480)

    Com_dev1 = Serial_dev()
    Com_dev1.set_com("COM59")
    Com_dev1.set_bps(115200)

    # Com_dev2 = Serial_dev()
    # Com_dev2.set_com("COM14")
    # Com_dev2.set_bps(115200)   

    Com_dev1.open()
    Com_dev1.send(gcode.init())
    Com_dev1.send("M204S1000\n")

    # Com_dev2.open()
    # Com_dev2.send(gcode.init())

    move_obj()
    print("Game Over!!!")

    pass
