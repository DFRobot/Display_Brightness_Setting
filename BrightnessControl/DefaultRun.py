# -*- coding:utf-8 -*-
#!/usr/bin/python
'''
 MIT License

 Copyright (C) <2019> <@DFRobot Liuzhixin>

  Permission is hereby granted, free of charge, to any person obtaining a copy of this
  software and associated documentation files (the "Software"), to deal in the Software
  without restriction, including without limitation the rights to use, copy, modify,
  merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
  permit persons to whom the Software is furnished to do so.

  The above copyright notice and this permission notice shall be included in all copies or
  substantial portions of the Software.
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
  INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
  PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
  FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
  ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
import  time
import  serial
import  sys

_LIGHT_DATA = [0x55, 0xAA, 0x00, 0x0D, 0x0A]

def count(x=[0]):
    x[0]+=1
    return int(x[0])

def writeRegister(number):
    data =(int)(number * 2.55)
    _LIGHT_DATA[2] = data
    success = False
    while not success:
        try:
            ser = serial.Serial("/dev/ttyUSB0",9600,timeout=0.5)
            if ser.isOpen == False:
                ser.open()
            ser.write(_LIGHT_DATA)
            time.sleep(0.1)
            ser.write(_LIGHT_DATA)
            time.sleep(0.1)
            ser.write(_LIGHT_DATA)
            ser.close()
            success = True
            
        except Exception as e:
            print(str(e))        
            if count() < 6:
                time.sleep(1)
            else:
                print("No device found!")
                break

def getLightData():
    success = False
    while not success:
        try:
            pathData = sys.argv[1] + "/config.txt"
            f = open(pathData, 'r')
            luminanceData = f.read()
            a = luminanceData.split()
            success = True
            return int(a[2])
        except Exception as e:
            if count() < 10:
                time.sleep(1)
            else:
                print("No profile!")
                break
    return 50
    
def main():
    lightData = getLightData()
    writeRegister(lightData)

if __name__ =='__main__':
    main()
