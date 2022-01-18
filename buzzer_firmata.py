from tkinter import *
from tkinter import ttk

#from pyfirmata import *
from pyfirmata import Arduino, util
import time

if __name__ == '__main__':
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    root.geometry("800x300")
    ttk.Label(frm, text="Tones").grid(column=0, row=0)
    time.sleep(1)

port = Arduino('/dev/cu.usbmodem14102')
pwmpin = port.get_pin('d:9:p')
#port.digital[9].write(1)
#increase_pwm = True
#pwm a:0:i for input
print(port.name)
print("Connected.")
time.sleep(1)

def tone():
    tone = 226 / 1000 #pwm mode 0-1 #-60
    #byteval 1-255 >> 7 /2^7 %128
    # 2 bits for int
    print("Do-C -ing: ")
    print(tone)
    pwmpin.write(tone)

    #preventing analog overflow
    # iterator = util.Iterator(port)
    # iterator.start()
    # port.analog[0].enable_reporting()
    # port.analgo[0].read()

    print("Sleeping.")
    pwmpin.write(0) #1-128
    time.sleep(1)

while True:

    ttk.Button(frm, text="Do-C", command= lambda: tone()).grid(column=0,row=1)
    ttk.Button(frm, text="Freq").grid(column=0, row=2)
    ttk.Button(frm, text="Close", command=root.destroy).grid(column=0, row=4)

    root.mainloop()
