import serial,time
import serial.tools.list_ports
import threading
from time import sleep

class Serial_dev(object):

    status = False
    bps = 115200
    def __init__(self):
        self.scan()
        pass
    
    def scan(self):
        self.port_list = list(serial.tools.list_ports.comports())
        if len(self.port_list) == 0:
            print("none dev")
        else:
            print("cur dev port :")
            for i in range(0,len(self.port_list)):
                print(str(self.port_list[i]).split('-')[0])
        pass
    
    def open(self):
        try:
            self.ser_v = serial.Serial(self.port,self.bps,timeout=3000)
            if self.ser_v.is_open:
                print("port "+str(self.port)+" Opened")
                print("bps: "+str(self.bps))
                self.status = True
            else:
                print("Open failed")
                self.status = False
            pass
        except:
            print("Open failed, please recheck whether the serial port is occupied!!!")  
            self.status = False
            pass

        return self.status
        

    def close(self):
        self.ser_v.close()
        self.status = False
        print(str(self.port)+" closed")
        pass

    def send(self,data):
        status = True
        if self.status:
            # write
            self.ser_v.write(data.encode("gbk"))
            # read
            while status:
                data = self.ser_v.read_until()
                # print(data)
                if "ok\\" in str(data):
                    # print(str(data))
                    return          
                elif "Unknown command" in str(data):
                    print(str(data)+" error")
                    self.ser_v.write(data.encode("gbk"))
                    pass
        print(data)
        pass

    def read(self):
        # status = False
        # while status:
        #     data = self.ser_v.read_until()
        #     print(data)
        #     if "ok\\" in str(data):
        #         print(str(data))
        #         return 
        pass


    def set_bps(self,val):
        self.bps = val
        pass

    def set_com(self,num):
        self.port = num
        pass


    pass



'''
gcode 
'''
class Gcode(object):
    def __init__(self):
        pass

    def init(self):
        temp = "M1111\n"
        print(temp)
        return temp
        
    def line_mode(self):
        temp = "M2000\n"
        print(temp)
        return temp
    
    def quick_mode(self):
        temp = "M2001\n"
        print(temp)
        return temp

    def home(self):
        temp = "M1112\n"
        print(temp)
        return temp
    
    def Z(self,z):
        temp = "G0"+"Z"+str(z)+"\r\n"
        print(temp)
        return temp        

    def X(self):
        pass

    def Y(self):
        pass

    def XYZ(self,x,y,z):
        temp = "G0"+"X"+str(x)+"Y"+str(y)+"Z"+str(z)+"F5000"+"\r\n"
        print(temp)
        return temp

    def XY(self,x,y):
        temp = "G0"+"X"+str(x)+"Y"+str(y)+"\r\n"
        print(temp)
        return temp

    def M100x(self,x):
        temp = "M100"+str(x)+"\r\n"
        print(temp)
        return temp
    
    def speed(self,val):
        temp = "G0F"+str(val)+"\r\n"
        print(temp)
        return temp


    def slide(self,flag):
        if flag == 1:
            return "M2012F5000\r\n"
        elif flag == 0:
            return "M2013\r\n"
        pass
    pass

global gcode
gcode = Gcode()

def main():
    Gcode1="M1111\r\n"
    Gcode2="M1112\r\n"
    #dev port 14
    dev = Serial_dev()
    dev.set_com("COM3")
    dev.set_bps(115200)
    dev.open()
    while True:
        dev.send(Gcode1)
        dev.send(Gcode2)
        time.sleep(1)

    dev.close()
    # dev.scan()
    pass

if __name__ == "__main__":
    main()    
    pass

