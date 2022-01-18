from tkinter import *
from tkinter import ttk
from tkinter import Tk, font

import serial
import time

if __name__ == '__main__':

    root = Tk()
    root.geometry('1000x500') #pixels
    root.title('Missing A Pitch')
    root.resizable(0,0)

    frm = ttk.Frame(root, padding=10)
    frm.pack(fill = BOTH, expand = True) #side = LEFT
    frm.grid()

    #relatively config the index of th grid
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=3)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_columnconfigure(3, weight=1)
    root.grid_columnconfigure(4, weight=1)
    root.grid_columnconfigure(5, weight=1)
    root.grid_columnconfigure(6, weight=1)

    label1 = Label(tfrm, text='Tones', bg='lavender', font=('Lucida Grande', 35))
    label1.grid(row=0, column=0)

    font.nametofont('TkDefaultFont').configure(family='Lucida Grande', size=20, weight=font.BOLD)

    time.sleep(1)

usb_port = '/dev/cu.usbmodem14102'
port = serial.Serial(usb_port, 9600, timeout=1)
#baudrate should be the same
#port.baudrate = '115200'
# ser = port.read(100)
print(port.name)
print(port.isOpen())
print('Connected.')
#port.timeout = None #0
# port.close()
port.reset_input_buffer()
time.sleep(1)

def tone():
    # str_value = b'Hi, it's been a long way.\n'
    # #str to byte
    # #str_value = 'Hi\n'.encode()
    # #str to utf
    # print('Sending:')
    # print(str_value)
    # port.write(str_value)
    # time.sleep(1)
    #
    # received_type = port.readline()
    # print('Raw received:')
    # print(received_type)
    # received_str = received_type.decode('utf-8').rstrip()
    # #byte to str
    # print('Converted received:')
    # print(received_str)
    # time.sleep(1)

def do():
    val = 226
    tone = str(val).encode()
    print('Sending:')
    print(tone)
    port.write(tone)
    return #break loop

def re():
    val = 294
    tone = str(val).encode()
    print('Sending:')
    print(tone)
    port.write(tone)
    return #break loop

def mi():
    val = 330
    tone = str(val).encode()
    print('Sending:')
    print(tone)
    port.write(tone)
    return #break loop

def mi():
    val = 330
    tone = str(val).encode()
    print('Sending:')
    print(tone)
    port.write(tone)
    return #break loop

def fa():
    val = 349
    tone = str(val).encode()
    print('Sending:')
    print(tone)
    port.write(tone)
    return #break loop

def so():
    val = 392
    tone = str(val).encode()
    print('Sending:')
    print(tone)
    port.write(tone)
    return #break loop

def la():
    val = 440
    tone = str(val).encode()
    print('Sending:')
    print(tone)
    port.write(tone)
    return #break loop

def si():
    val = 494
    tone = str(val).encode()
    print('Sending:')
    print(tone)
    port.write(tone)
    return #break loop

while True:

    c = Button(root, text='Do-C', command= lambda: do(), bg='black')
    d = Button(root, text='Re-D', command= lambda: re(), bg='white')
    e = Button(root, text='Mi-E', command= lambda: mi(), bg='black')
    f = Button(root, text='Fa-F', command= lambda: fa(), bg='white')
    g = Button(root, text='So-G', command= lambda: so(), bg='black')
    a = Button(root, text='Ra-A', command= lambda: la(), bg='white')
    b = Button(root, text='Si-B', command= lambda: si(), bg='black')

    c.grid(row=1, column=0, sticky='ns', padx=3, pady=3)
    d.grid(row=1, column=1, sticky='ns', padx=3, pady=3)
    e.grid(row=1, column=2, sticky='ns', padx=3, pady=3)
    f.grid(row=1, column=3, sticky='ns', padx=3, pady=3)
    g.grid(row=1, column=4, sticky='ns', padx=3, pady=3)
    a.grid(row=1, column=5, sticky='ns', padx=3, pady=3)
    b.grid(row=1, column=6, sticky='ns', padx=3, pady=3)

    ttk.Label(frm, text='Freq: 226').grid(column=0, row=2)
    ttk.Label(frm, text='Freq: 294').grid(column=1, row=2)
    ttk.Label(frm, text='Freq: 330').grid(column=2, row=2)
    ttk.Label(frm, text='Freq: 349').grid(column=3, row=2)
    ttk.Label(frm, text='Freq: 394').grid(column=4, row=2)
    ttk.Label(frm, text='Freq: 440').grid(column=5, row=2)
    ttk.Label(frm, text='Freq: 494').grid(column=6, row=2)

    r = Button(frm, text='Reset', command= port.write(0))
    e = Button(frm, text='Close', command=root.destroy)

    r.grid(column=3, row=3, sticky='ew', padx=3, pady=3)
    e.grid(column=3, row=4, sticky='ew', padx=3, pady=3)

    root.mainloop()
