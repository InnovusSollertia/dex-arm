import cv2
import yaml
import numpy as np


class Cam_dev():
    port_list = []  

    cameraMatrix = np.array([
                            [ 7.9641507015667764e+02, 0., 3.1577913194699374e+02], 
                            [0.,7.9661307355876215e+02, 2.1453452136833957e+02], 
                            [0., 0., 1. ]
                            ])

    distCoeffs = np.array([
                        [ -1.1949335317713690e+00,
                        1.8078010700662486e+00,
                        4.9410258870084744e-03, 
                        2.8036176641915598e-03,
                        -2.0575845684235938e+00]
                        ])  


    def __init__(self):
        self.scan()
        # self.open(dev_id,cap_w,cap_h)
        pass

    def open(self,dev_id,cap_w,cap_h):
        self.cap = cv2.VideoCapture(dev_id)

        if self.cap.isOpened():
            print("Open success")
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, cap_w)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cap_h)

            self.print_info()

            # self.set_cam_info()     
            # self.print_info()       
            
            print("The camera parameters are set successfully")
        else:
            print("Failed to open camera")  
        pass
    

    def print_info(self):

        print("Width : "+str(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
        print("High degree : "+str(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        print("frames : "+str(self.cap.get(cv2.CAP_PROP_FPS)))        
        print("Contrast : "+str(self.cap.get(cv2.CAP_PROP_CONTRAST)))
        print("saturation : "+str(self.cap.get(cv2.CAP_PROP_SATURATION)))
        print("Color tone : "+str(self.cap.get(cv2.CAP_PROP_HUE)))
        print("Exposure : "+str(self.cap.get(cv2.CAP_PROP_EXPOSURE)))

        pass
    
    def set_cam_info(self):
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.cap.set(cv2.CAP_PROP_FPS,30)
        self.cap.set(cv2.CAP_PROP_CONTRAST,135)
        self.cap.set(cv2.CAP_PROP_SATURATION,75)
        self.cap.set(cv2.CAP_PROP_HUE,0)
        self.cap.set(cv2.CAP_PROP_EXPOSURE,50)
        pass


    def scan(self):
        self.dev_list = []
        num = 0
        for i in range(10):
            try:
                temp_cap = cv2.VideoCapture(i)
                if temp_cap.isOpened():
                    self.dev_list.append(num)
                    num = num + 1
                    temp_cap.release()
            except:
                pass

        print("cam dev："+str(self.dev_list))
        pass

    def close(self):
        self.cap.release()  
        pass

    def get_img(self,img_type):
        if img_type==0:
            ret, img = self.cap.read()
        elif img_type==1:
            ret, img = self.cap.read()
            img = cv2.undistort(img, self.cameraMatrix, self.distCoeffs, None)
        return img
    
    pass

video = Cam_dev()                

def nothing(x):

    pass

'''camera demo'''
def cam_main():
    video.scan()

    # print("matrix:\n",str(video.cameraMatrix))
    # print("Coeffs:\n", str(video.distCoeffs))
    # cv2.namedWindow('src_img')


    dev_id = input("please input ID:")
    video.open(int(dev_id),640,480)
    cv2.namedWindow('src_img')
    cv2.createTrackbar('CONTRAST','src_img',0,255,nothing)
    cv2.createTrackbar('SATURATION','src_img',0,255,nothing)    

    num =100
    while num:

        # cv2.imshow("dis_img", video.get_img(1))
        horizontal = cv2.flip(video.get_img(0),0,dst=None) 
        cv2.imshow("src_img", horizontal)
        
        CONTRAST = cv2.getTrackbarPos('CONTRAST','src_img')
        SATURATION = cv2.getTrackbarPos('SATURATION','src_img')

        # video.cap.set(cv2.CAP_PROP_CONTRAST,CONTRAST)
        # video.cap.set(cv2.CAP_PROP_SATURATION,SATURATION)

        video.cap.set(cv2.CAP_PROP_CONTRAST,135)
        video.cap.set(cv2.CAP_PROP_SATURATION,75)

        # num =num -1
        cv2.waitKey(1)
        
    video.close()
    pass

'''
horizontal = cv.flip(img,1,dst=None) 
vertical = cv.flip(img,0,dst=None) 
cross = cv.flip(img,-1,dst=None) 
'''

'''main'''
if __name__ == "__main__":
    cam_main()
    pass