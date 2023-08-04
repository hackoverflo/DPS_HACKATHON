import tkinter as tk
from tkinter import*
def canvas():
    lastx, lasty = 0, 0
    def xy(event):
        global lastx, lasty
        lastx, lasty = event.x, event.y


    def addLine(event):
        global lastx, lasty
        canvas.create_line((lastx, lasty, event.x, event.y), width = 5)
        lastx, lasty = event.x, event.y


    window = tk.Tk()
    window.geometry("800x600")
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)



    canvas = tk.Canvas(window, width = '2', height = '2')
    canvas.pack()
    canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    canvas.bind("<Button-1>", xy)
    canvas.bind("<B1-Motion>", addLine)

    btn = Button(window, text = 'D\ne\nl\ne\nt\ne', bg = 'black', foreground = 'white', command = lambda:canvas.delete('all'), height = 26, font = ('Aerial', 15))
    btn.grid(column=1, row = 0)

    window.mainloop()
