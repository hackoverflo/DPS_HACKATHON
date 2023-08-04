from tkinter import*
import tkinter as tk

def games():
    window = Tk()
    window.geometry("550x400")
    window.resizable(0,0)
    window.config(bg = 'red')
    title = Label(window, text = 'Welcome to the Game window.\n Here you can access different games.', font = ('Aerial', 15))
    title.place(x = 100, y = 10)

    def tiles():
        from freegames import tiles
    def pac():
        from freegames import pacman
    def snake():
        from freegames import snake
    def fid():
        from freegames import fidget
    def life():
        from freegames import life

    btn1 = Button(window, text = 'Tiles game', bg = 'blue', foreground = 'white', height = 5, command = tiles, width = 10)
    btn1.pack()
    btn1.place(x = 20, y = 110)

    btn2 = Button(window, text = 'Pacman Game',  bg = 'green', foreground = 'white', height = 5, command = pac, width = 11)
    btn2.pack()
    btn2.place(x = 120, y = 110)

    btn3 = Button(window, text = 'Snake game',  bg = 'orange', foreground = 'black', height = 5, command = snake, width = 10)
    btn3.pack()
    btn3.place(x = 220, y = 110)

    btn4 = Button(window, text = 'Fidget game',  bg = 'cyan', foreground = 'black', height = 5, command = fid, width = 10)
    btn4.pack()
    btn4.place(x = 320, y = 110)

    btn5 = Button(window, text = 'Life game',  bg = 'yellow', foreground = 'black', height = 5, command = life, width = 10)
    btn5.pack()
    btn5.place(x = 420, y = 110)


    window.mainloop()