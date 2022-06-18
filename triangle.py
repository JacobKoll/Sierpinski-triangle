from tkinter import *

root = Tk()

c = Canvas(root, width=1000, height=1000)
c.pack()

points = [100,100,300,100,200,300]
c.create_polygon(points)

root.mainloop()
