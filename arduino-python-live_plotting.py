import tkinter as tk
from tkinter import *
from tkinter import ttk
import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

root=Tk()
fig=plt.figure()

ax = fig.add_subplot(1,1,1)
ax.set_xlim([0,20])
ax.set_ylim([0,6])
ax.plot([i for i in range(10)],[i for i in range(10)])
global z,arduino,j
j=0
z=0
xs=[i for i in range(10)]
ys=[]
data=0

def animate(i):
    print(z)
    if(z==1):
        data=int(arduino.readline())
        ys.append(data)
        print(ys)
        ax.clear()
        ax.set_xlim([float(len(ys)-60),float(len(ys))]) ## this limit is set for showing 60 data points in a graph
        ax.set_ylim([0.0,10.0])  ## limit can be changed with minimum and maximum
        ax.plot([i for i in range(len(ys))],ys)  ## plots the graph
        ax.set(xlabel='Time in x100 ms',ylabel='Magnitude')
        ax.set_title('NONe of concern')

            
    else:
        print("Not connected to com port")



def hello():
    global arduino,z
    arduino=serial.Serial('com3',9600)  ##mention here com port number and baud rate
    print("here")
    z=1
    print(z)
    
def stop():
    global z,arduino
    arduino=None
    z=0
    ax.clear()
b=Button(root,text="START",command=hello,font=('Arial','24'))
b.pack()
c=Button(root,text="Stop",command=stop,font=('Arial','24'))
c.pack()

anim = animation.FuncAnimation(fig, animate, interval=100)

plt.show()

root.mainloop()
