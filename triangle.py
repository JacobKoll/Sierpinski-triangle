from tkinter import *
import random

class Sierpinski(Tk):
    def __init__(self, parent, iterations):
        Tk.__init__(self, parent)
        self.c_width = 1000
        self.c_height = 1000
        self.iterations = min(100000, iterations)
        self.resizable(False, False)
        self.title('Sierpinski\'s Triangle Demo')
        self.initialize()

    def initialize(self):
        self.canvas = Canvas(self, width=self.c_width, height=self.c_height, bg='black')
        self.canvas.pack(side=RIGHT, expand=YES, fill=BOTH)
        self.simulate()

    def plot_point(self, x, y):
        self.canvas.create_oval(x, y, x+1, y+1, outline='white')
        return {'x':x, 'y':y}

    def intercept(self, x, tline):
        m = (tline['y2'] - tline['y1'])/(tline['x2'] - tline['x1'])
        return m*(x-tline['x1'])+tline['y1']

    def simulate(self):
        # Some fancy math to figure out the bounds. This method is random enough but is skewed to the lower portion of the triangle.
        # x = random.randint(x2, x3)
        # y = random.randint(m(x-x1)+y1, y2) m changes depending on what side of the triangle x happens to be on.
        t = {1:self.plot_point(self.c_width/2, self.c_height-950),
             2:self.plot_point(self.c_width-950, self.c_height-50),
             3:self.plot_point(self.c_width-50, self.c_height-50)}

        rp_x = random.randint(t[2]['x'], t[3]['x'])
        tline = {'x1':t[1]['x'], 'y1':t[1]['y'], 'x2':t[2]['x'], 'y2':t[2]['y']}
        if rp_x > t[1]['x']:
            tline = {'x1':t[1]['x'], 'y1':t[1]['y'], 'x2':t[3]['x'], 'y2':t[3]['y']}
        rp_y = random.randint(self.intercept(rp_x, tline), t[2]['y'])
        p = self.plot_point(rp_x, rp_y)
        for point in range(self.iterations):
            rtp = t[random.randint(1,3)]
            mp = self.plot_point((p['x']+rtp['x'])/2,(p['y']+rtp['y'])/2)
            p = mp

triangle = Sierpinski(None, 100000)
triangle.mainloop()

