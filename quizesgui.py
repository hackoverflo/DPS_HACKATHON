
from tkinter import *
import tkinter as tk
import random
from main1 import *



def gui(listQ,l):
    def openout_box():
         
    output_box = Tk()
    output_box.geometry("400x400")
    output_box.resizable(0,0)
    output_box.config(bg = 'yellow')
    title = Label(output_box, text = listQ[l], font = ('Times New Roman', 25))
    title.place(x = '45', y = '32')
    entryn= Entry(output_box, width= 55)
    entryn.focus_set()
    entryn.pack()
    entryn.place(x = 35, y = 140)
    enterbutton = Button(output_box, text = 'Enter', bg = 'black', foreground = 'white', command = lambda:openoutput_box)
    enterbutton.pack()
    enterbutton.place(x = 120, y = 200)
    speakbutton = Button(output_box, text = 'Speak(instead)', bg = 'black', foreground = 'white')
    speakbutton.pack()
    speakbutton.place(x = '220', y = '200')
    output_box.mainloop()

def primaryQuiz():
        score = 0
        listQ = ['The tree has a branch filled with green _____.', 'What part of the body helps you move?' , ' What star shines in the day and provides light? ','Which shape is a round?','Your hands have four fingers and a ____.']

        listA = ['leaves','legs','sun','circle','thumb','Thumb']
        for i in range(len(listQ)-1):
            randInt = random.randint(0,(len(listQ)-1))
            gui(listQ,randInt)
            que1 = speak(listQ[randInt])
            que = input(listQ[randInt])
            if que == listA[randInt].lower():
                print('Correct Answer')
                score +=1
            elif que != listA[randInt]:
                print('Wrong Answer')
                score +=0
        print(str(score) + " is your final score")
        speak(str(score) + " is your final score")
def openoutput_box():
    # print("apple")
    value = entryn.get()
    if value.lower() == 'primary':
        primaryQuiz()
    # elif value.lower() == 'secondary':
    #     secondaryQuiz()
    # elif value.lower() == 'tertiary':
    #     tertiaryQuiz()

