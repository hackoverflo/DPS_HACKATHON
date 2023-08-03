import tkinter as tk


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

canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)

window.mainloop()