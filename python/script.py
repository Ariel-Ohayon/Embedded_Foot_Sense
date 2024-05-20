import serial
import serial.tools.list_ports
import time

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QPixmap, QImage

import cv2 as cv

class SerialReader(QThread):
    data_recv = pyqtSignal(str)
    
    def __init__(self, port='com3', baud=9600, parent = None):
        super().__init__(parent)
        self.port = serport()
    
    def run(self):
        while True:
            if self.port.in_waiting:
                data = self.port.readline().decode()
                self.data_recv.emit(data)

class GUI(QMainWindow):
    def __init__(self):
        super(GUI,self).__init__()
        uic.loadUi('Design.ui',self)
        self.show()
        
        self.serial_thread = SerialReader()
        self.serial_thread.data_recv.connect(self.func_sens_label)
        self.serial_thread.start()
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.func_sens_label)
        self.timer.start(500)   #thread executing every 0.5 second
        
        self.filename = 'img.png'
        self.img = cv.imread(self.filename)

        
    def func_sens_label(self, data=None):
        if data:
            data_list = data.split()
            if(len(data_list) == 3):
                str_sens_data = data_list[2]
                str_values = str_sens_data.split(',')
                
                for i in range(0,8):
                    str_values[i] = str_values[i].replace(f'sens_{i}=','')
                
                self.Sensor1_Label.setText(f'Sensor1: {255 - map_val(int(str_values[0]))}')
                self.Sensor2_Label.setText(f'Sensor2: {255 - map_val(int(str_values[1]))}')
                self.Sensor3_Label.setText(f'Sensor3: {255 - map_val(int(str_values[2]))}')
                self.Sensor4_Label.setText(f'Sensor4: {255 - map_val(int(str_values[3]))}')
                self.Sensor5_Label.setText(f'Sensor5: {255 - map_val(int(str_values[4]))}')
                self.Sensor6_Label.setText(f'Sensor6: {255 - map_val(int(str_values[5]))}')
                self.Sensor7_Label.setText(f'Sensor7: {255 - map_val(int(str_values[6]))}')
                self.Sensor8_Label.setText(f'Sensor8: {255 - map_val(int(str_values[7]))}')
                
                center1_coordinates = (181, 1225)
                center2_coordinates = (136,843)
                center3_coordinates = (307,876)
                center4_coordinates = (133,410)
                center5_coordinates = (248,413)
                center6_coordinates = (380,400)
                center7_coordinates = (300,170)
                center8_coordinates = (170,170)
                
                
                radius = 30
                color1 = (map_val(int(str_values[0])), map_val(int(str_values[0])), 255)
                color2 = (map_val(int(str_values[1])), map_val(int(str_values[1])), 255)
                color3 = (map_val(int(str_values[2])), map_val(int(str_values[2])), 255)
                color4 = (map_val(int(str_values[3])), map_val(int(str_values[3])), 255)
                color5 = (map_val(int(str_values[4])), map_val(int(str_values[4])), 255)
                color6 = (map_val(int(str_values[5])), map_val(int(str_values[5])), 255)
                color7 = (map_val(int(str_values[6])), map_val(int(str_values[6])), 255)
                color8 = (map_val(int(str_values[7])), map_val(int(str_values[7])), 255)
                thickness = -1
                
                self.img = cv.circle(self.img, center1_coordinates, radius, color1, thickness)
                self.img = cv.circle(self.img, center2_coordinates, radius, color2, thickness)
                self.img = cv.circle(self.img, center3_coordinates, radius, color3, thickness)
                self.img = cv.circle(self.img, center4_coordinates, radius, color4, thickness)
                self.img = cv.circle(self.img, center5_coordinates, radius, color5, thickness)
                self.img = cv.circle(self.img, center6_coordinates, radius, color6, thickness)
                self.img = cv.circle(self.img, center7_coordinates, radius, color7, thickness)
                self.img = cv.circle(self.img, center8_coordinates, radius, color8, thickness)
                
                height, width, channel = self.img.shape
                bytes_per_line = 3 * width
                q_image = QImage(self.img.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
                self.label_img.setPixmap(QPixmap.fromImage(q_image))
        
            
def main():
    app = QApplication([])
    window = GUI()
    app.exec_()
    
def serport():
        # -- Initialize Serial Ports -- #
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()
    
    portlist = []
    for onePort in ports:
        portlist.append(str(onePort))
    if (portlist == []):
        print('COM PORTs not Found')
        return None
    else:
        print('List of the COM Ports:')
        for onePort in ports:
            print(str(onePort))
        # -- Serial Port Detection -- #
        
        
        # -- Connect to serial Port -- #
        COM = input('Enter The COM Port you want to connect: ')
        print(f"connect to COM Port: {COM}")
        Connection = serial.Serial(COM,9600,timeout=0.5)
        Connection.baudrate = 9600
        Connection.parity = 'N'
        Connection.bytesize = 8
        Connection.stopbits = 1
        return Connection


def map_val(val):
    return int( val * (255/1023) )

if __name__ == '__main__':
    main()