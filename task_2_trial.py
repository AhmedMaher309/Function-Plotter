from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import time 

root = Tk()
root.geometry("500x300")
root.title(" Graph Drawer GUI")
equ=""

def Take_input():
	input = inputtxt.get("1.0", "end-1c")
	print(input)
	global equ
	equ =input


l = Label(text = "Write the equation as in python syntax to work successfully with lower case x")

inputtxt = Text(root, height = 2,
				width = 30,
				bg = "light yellow")

Display = Button(root, height = 2,
				width = 20,
				text ="Plot",
				command = lambda:Take_input())


close_btn = Button(root, text = 'finish', command = root.destroy)
close_btn.place(x=220, y=190)

l.pack()
inputtxt.pack()
Display.pack()
mainloop()

################################################################
x = np.linspace(-3, 3, 100)
y = x
#np.sin(x)
 
# to run GUI event loop
plt.ion()
 
# here we are creating sub plots
figure, ax = plt.subplots(figsize=(10, 5))
line1, = ax.plot(x, y)
 
# setting title
plt.title("Graph", fontsize=20)
 
# setting x-axis label and y-axis label
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
 
# Loop
for _ in range(-100,200):
    # creating new Y values
    new_y = eval(equ)
    line1.set_xdata(x)
    line1.set_ydata(new_y)
    figure.canvas.draw()
    figure.canvas.flush_events()
    time.sleep(0.1)

time.sleep(5)