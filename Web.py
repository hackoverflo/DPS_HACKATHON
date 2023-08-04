from tkinter import*
import webbrowser
def visualsF():
    window = Tk()
    window.geometry("1000x500")
    window.resizable(0,0)
    window.config(bg = 'yellow')

    title = Label(window, text = 'Welcome to Web Page View Window.\n Here you can press on these buttons which will take you to those webpages.', font = ('Aerial', 15))
    title.place(x = 170, y = 30)

    def khan():
        ka = "https://www.khanacademy.org/"
        webbrowser.open(ka)
    def byjus():
        by = "https://byjus.com/"
        webbrowser.open(by)
    def udemy():
        ud = "https://www.udemy.com/?utm_source=aff-campaign&utm_medium=udemyads&LSNPUBID=yNfEamYSgXk&ranMID=47901&ranEAID=yNfEamYSgXk&ranSiteID=yNfEamYSgXk-To_ECAZe.CNJwb6htF_Vsg&gclid=CjwKCAjw_aemBhBLEiwAT98FMh_9qY6NVEHFgTPjPkfk1DXVArfvjLxQcXLuwoSQSCWuPoeWughwHRoC1H0QAvD_BwE"
        webbrowser.open(ud)
    def doubt():
        dou = "https://www.doubtnut.com/"
        webbrowser.open(dou)
    def brain():
        br = "https://brainly.in/"
        webbrowser.open(br)
    def shaala():
        SH = "https://www.shaalaa.com/"
        webbrowser.open(SH)

    bkhan = Button(window, text = 'Khan Academy', bg = 'green', foreground='white', height = 5, command = khan)
    bkhan.pack()
    bkhan.place(x = 20, y = 150)

bby = Button(window, text = 'Byjus', bg = 'red', foreground='white', height = 5, width = 12, command = byjus)
bby.pack()
bby.place(x = 180, y = 150)

bu = Button(window, text = 'Udemy', bg = 'blue', foreground='white', height = 5, width = 12, command = udemy)
bu.pack()
bu.place(x = 340, y = 150)

bdo = Button(window, text = 'Doubtnut', bg = 'black', foreground='white', height = 5, width = 12, command = doubt)
bdo.pack()
bdo.place(x = 500, y = 150)

bbr = Button(window, text = 'Brainly', bg = 'orange', foreground='white', height = 5, width = 12, command = brain)
bbr.pack()
bbr.place(x = 660, y = 150)

bsh = Button(window, text = 'Shaala', bg = 'white', foreground='black', height = 5, width = 12, command = shaala)
bsh.pack()
bsh.place(x = 810, y = 150)

window.mainloop()
