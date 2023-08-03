from tkinter import*
import tkinter as tk
output_box = Tk()
output_box.geometry("400x400")
output_box.resizable(0,0)
output_box.config(bg = 'yellow')

title = Label(output_box, text = 'Type your answer here', font = ('Times New Roman', 25))
title.place(x = '55', y = '32')

entryn= Entry(output_box, width= 55)
entryn.focus_set()
entryn.pack()
entryn.place(x = 35, y = 140)

def openoutput_box():
    pass

enterbutton = Button(output_box, text = 'Enter', bg = 'black', foreground = 'white', command=openoutput_box)
enterbutton.pack()
enterbutton.place(x = 120, y = 200)

speakbutton = Button(output_box, text = 'Speak(instead)', bg = 'black', foreground = 'white')
speakbutton.pack()
speakbutton.place(x = '220', y = '200')
output_box.mainloop()