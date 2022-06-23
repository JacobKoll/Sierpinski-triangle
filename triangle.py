from tkinter import *
import random

root = Tk()
c_width, c_height = 1000, 1000
tp1_x = c_width/2
tp1_y = c_height-950
tp2_x = c_width-950
tp2_y = c_height-50
tp3_x = c_width-50
tp3_y = c_height-50

c = Canvas(root, width=c_width, height=c_height, bg='black')
c.pack()

def plot_point(x, y):
    c.create_oval(x, y, x+1, y+1, outline='white')

plot_point(tp1_x, tp1_y)
plot_point(tp2_x, tp2_y)
plot_point(tp3_x, tp3_y)

def simulate(n_points):
    for p in range(n_points):
        # need to do some fancy math here to figure out the bounds, I think.
        rp_x = random.randint(tp2_x, tp3_x)
        rp_y = random.randint(tp1_y, tp2_y)
        plot_point(rp_x, rp_y)

simulate(10)
root.mainloop()
