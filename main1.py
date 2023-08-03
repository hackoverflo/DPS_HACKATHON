import webbrowser
import random
from random import randint
import pyttsx3
import speech_recognition as sr
import tkinter as tk
import randfacts
from tkinter import *
import webview



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        dash = r.recognize_google(audio, language='en-in')
        dash = str(dash)
        print(f"User said: {dash}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return dash

def study_web():
    ka = "https://www.khanacademy.org/"
    webbrowser.open(ka)
    by = "https://byjus.com/"
    webbrowser.open(by)
    ud = "https://www.udemy.com/?utm_source=aff-campaign&utm_medium=udemyads&LSNPUBID=yNfEamYSgXk&ranMID=47901&ranEAID=yNfEamYSgXk&ranSiteID=yNfEamYSgXk-To_ECAZe.CNJwb6htF_Vsg&gclid=CjwKCAjw_aemBhBLEiwAT98FMh_9qY6NVEHFgTPjPkfk1DXVArfvjLxQcXLuwoSQSCWuPoeWughwHRoC1H0QAvD_BwE"
    webbrowser.open(ud)
    dou = "https://www.doubtnut.com/"
    webbrowser.open(dou)
    br = "https://brainly.in/"
    webbrowser.open(br)
    SH = "https://www.shaalaa.com/"
    webbrowser.open(SH)

ideas = []
def idea_box():
    speak("ENTER YOUR IDEAS, YOUR OPINION ON TODAY'S EDUCATION SYSTEM AND WHAT WOULD YOU DO TO MAKE it BETTER?")
    z = takeCommand()
    ideas.append(z)
    for i in range(len(ideas)): #after calling
        print(ideas[i])

def math_guess():
    
    start = 1
    end = 100
    value = randint(start, end)
    speak("I'm thinking of a number between", start, 'and', end)
    guess = None
    while guess != value:
        m = speak("Guess the number")
        text = input('Guess the number: ')
        guess = int(text)
        if guess < value:
            print('Higher.')
        elif guess > value:
            print('Lower.')
    print('Congratulations! You guessed the right answer:', value)

points = 0
def point_check():
    print("Your points are " + str(points))

def study_jokes():
    
    jokes = ['''Teacher: Great! You are studying in break time!
    Student: Thank you. I heard that it is good to study before sleep.''',
    ''' Why did the students eat their homework?
    Because the teacher said that it was a piece of cake.''',
    ''' Never drink water while studying
    It will dilute your concentration ''',''' The Sun must have spent many years studying, he has got millions of degrees.''', '''Student: I do not think I deserved zero on my final exam. It does not seem fair to me.
    Teacher: I absolutely agree with you. But that is really the lowest mark I can give you. ''', ''' What is the best way to sleep the night before an exam?
    I sleep next to my notes, sincerely hoping they transfer into my brain by osmosis.''', ''' Nothing is better than studying
    That is why I do nothing.''','''I just realized that never is a contraction of not ever.
    And blush is a contraction of blood rush.
    And studying is a contraction of student dying. ''',''' What do you call a teapot of boiling water on top of mount Everest?
    A high-pot-in-use''',''' What do you call the number seven and the number three when they go out on a date?
    The odd couple (but seven is in his prime).''']

    n = random.randint(0, (len(jokes)-1))
    print(jokes[n])
    speak(jokes[n])

def facts():
    fact= randfacts.get_fact()
    print('Facts to make you more interested in the art fo studying: ')
    speak('Facts to make you more interested in the art fo studying: ')
    print(fact)
    speak(fact)

def quiz():
    speak("Enter level:- primary , secondary or tertiary")
    grade = takeCommand()
    def secondaryQuiz():
        score = 0
        listQ = ['Which animal never drinks water?', 'Physical phase of life is called ?' , 'The Largest Cell is? ','Which is the Largest Human Cell?','The Total Number of Bones in the Human Body?']

        listA = ['Kangaroo Rat','Protoplasm','Ostrich','Nerve Cell','206']
        for i in range(len(listQ)-1):
            randInt = random.randint(0,(len(listQ)-1))
            que3 = speak(listQ[randInt])
            que = input(listQ[randInt])
            if que == listA[randInt].lower():
                print('Correct Answer')
                speak('Correct Answer')
                
                score +=1
            elif que != listA[randInt]:
                print('Wrong Answer')
                speak('Wrong Answer')
                score +=0
        print(str(score) + "is your final score")
        speak(str(score) + "is your final score")
    def primaryQuiz():
        score = 0
        listQ = ['The tree has a branch filled with green', 'What part of the body helps you move?' , ' What star shines in the day and provides light? ','Which shape is a laptop?','How many fingers does your hand have?']

        listA = ['leaves','legs','sun','rectangle','5']
        for i in range(len(listQ)-1):
            randInt = random.randint(0,(len(listQ)-1))
            que1 = speak(listQ[randInt])
            que = takeCommand()
            if que == listA[randInt].lower():
                print('Correct Answer')
                score +=1
                listQ.pop(randInt)
            elif que != listA[randInt]:
                print('Wrong Answer')
                listQ.pop(randInt)
        print(str(score) + " is your final score")
        speak(str(score) + " is your final score")

    def tertiaryQuiz():
        score = 0
        listQ = ['The SI Unit of Speed is', 'The movement of earth on its axis is called ?' , ' The Center of Atom is called:','In which Ocean Mariana Trench is located?','Scientis who gave law if gravitation?']

        listA = ['m/s','rotation','nucleus','pacific ocean','Newton']
        for i in range(len(listQ)-1):
            randInt = random.randint(0,(len(listQ)-1))
            que2 = speak(listQ[randInt])
            que = input(listQ[randInt])
            if que == listA[randInt].lower():
                print('Correct Answer')
                score +=1
            elif que != listA[randInt]:
                print('Wrong Answer')
                score +=0
        print(str(score) + " is your final score")
        speak(str(score) + " is your final score")


    if grade == 'primary':
        primaryQuiz()
    elif grade == 'secondary':
        secondaryQuiz()
    elif grade == 'tertiary':
        tertiaryQuiz()
    else:
        print(' no quiz available for you ')

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

    btn = Button(window, text = 'Delete', bg = 'black', foreground = 'white', command = lambda:canvas.delete('all'))
    btn.grid(column=3, row = 4)

    window.mainloop()

def visuals():
    root = tk.Tk()
    def circuits():
        root.geometry('700x700')
        webview.create_window('CIRCUITS','https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html')
        webview.start()

    def chem():
        root2 = tk.Tk()
        root2.geometry('700x700')
        webview.create_window('PERIODIC TABLE','https://artsexperiments.withgoogle.com/periodic-table/')
        webview.start()

    def skeleton():
        root3 = tk.Tk()
        root3.geometry('700x700')
        webview.create_window('SKELETAL SYSTEM','https://www.artec3d.com/3d-models/human-skeleton-hd')
        webview.start()

def out():

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

    speakbutton = Button(output_box, text = 'Speak(instead)', bg = 'black', foreground = 'white',command=lambda:takeCommand())
    speakbutton.pack()
    speakbutton.place(x = '220', y = '200')
    output_box.mainloop()

def recite():
    score_reci = 0
    listOfQ = [] 
    listOfA = []
    for i in range(5):
        speak("Enter the Question: ")
        quest = takeCommand()
        speak("Enter the Answer for that question: ")
        ans = takeCommand()
        listOfQ.append(quest)
        listOfA.append(ans)
    # speak("Practice Time")
    speak("Practice Time")
    # speak("Enter your question")



    for i in range(0,(len(listOfA)-1)):
        randomN = random.randint(0,(len(listOfQ)-1))
        speak(listOfQ[randomN])
        q = takeCommand()
        if (q==listOfA[randomN]):
            speak('Correct Answer')
            score_reci+=1
            # speak("Correct Answer")
        else:
            print("Wrong answer")
    if score_reci>=(5-1):
        score+=1

if __name__ == "__main__":
    quiz()