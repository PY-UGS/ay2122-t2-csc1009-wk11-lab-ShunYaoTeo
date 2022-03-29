
from datetime import datetime
class clockTime:

    def __init__(self):
        self.hour  = 00
        self.min = 00
        self.sec = 00

    def setHours(self):
        self.hour = int(input("Enter Hour: "))      
    def setMinutes(self):
        self.min = int(input("Enter Minutes: "))

    def setSeconds(self):
        self.sec = int(input("Enter Seconds: "))

    def setTime(self):
        self.setHours()
        self.setMinutes()
        self.setSeconds()

    def showTime(self):
        print("%02d:%02d:%02d" %(self.hour,self.min,self.sec))


if __name__ == "__main__":
    clock = clockTime()

    clock.setTime()
    clock.showTime()
