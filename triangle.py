from tkinter import *
import random

root = Tk()
root.resizable(False, False)
root.title('Sierpinski\'s Triangle Demo')
c_width, c_height = 1000, 1000
canvas = Canvas(root, width=c_width, height=c_height, bg='black')
canvas.pack()

def plot_point(x, y):
    canvas.create_oval(x, y, x+1, y+1, outline='white')
    return {'x':x, 'y':y}

def intercept(x, tline):
    m = (tline['y2'] - tline['y1'])/(tline['x2'] - tline['x1'])
    return m*(x-tline['x1'])+tline['y1']

def simulate(n_points):
    t = {1:plot_point(c_width/2, c_height-950),
         2:plot_point(c_width-950, c_height-50),
         3:plot_point(c_width-50, c_height-50)}

    # Some fancy math to figure out the bounds. This method is random enough but is skewed to the lower portion of the triangle.
    # x = random.randint(x2, x3)
    # y = random.randint(m(x-x1)+y1, y2) m changes depending on what side of the triangle x happens to be on.
    rp_x = random.randint(t[2]['x'], t[3]['x'])
    tline = {'x1':t[1]['x'], 'y1':t[1]['y'], 'x2':t[2]['x'], 'y2':t[2]['y']}
    if rp_x > t[1]['x']:
        tline = {'x1':t[1]['x'], 'y1':t[1]['y'], 'x2':t[3]['x'], 'y2':t[3]['y']}
    rp_y = random.randint(intercept(rp_x, tline), t[2]['y'])

    p = plot_point(rp_x, rp_y)
    for point in range(n_points):
        rtp = t[random.randint(1,3)]
        mp = plot_point((p['x']+rtp['x'])/2,(p['y']+rtp['y'])/2)
        p = mp

iterations = 10000
simulate(0)

# This is the worst way to update the canvas. I will update later to keep track of each point and draw and erase as the slider moves.
def slider_changed(event):
    canvas.delete("all")
    simulate(slider.get())

slider = Scale(root,from_=0,to=iterations,length=c_width,orient='horizontal',command=slider_changed)
slider.pack()

root.mainloop()
