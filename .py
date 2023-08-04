import pygame
from pygame import *
import math


import webbrowser
import random
from random import randint
import pyttsx3
import speech_recognition as sr
import tkinter as tk
import randfacts
from tkinter import *
import webview

score =0

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
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        takeCommand()
        return "None"
    return query

def web_study():
    web_window = tk.Tk()
    web_window.geometry("1000x500")
    web_window.resizable(0,0)
    web_window.config(bg = '#ABE97A')

    title = Label(web_window, text = 'Welcome to Web Page View web_window.\n Here you can press on these buttons which will take you to those webpages.', font = ('Aerial', 15))
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

    bkhan = Button(web_window, text = 'Khan Academy', bg = 'green', foreground='white', height = 5, command = khan)
    bkhan.pack()
    bkhan.place(x = 20, y = 150)

    bby = Button(web_window, text = 'Byjus', bg = 'red', foreground='white', height = 5, width = 12, command = byjus)
    bby.pack()
    bby.place(x = 180, y = 150)

    bu = Button(web_window, text = 'Udemy', bg = 'blue', foreground='white', height = 5, width = 12, command = udemy)
    bu.pack()
    bu.place(x = 340, y = 150)

    bdo = Button(web_window, text = 'Doubtnut', bg = 'black', foreground='white', height = 5, width = 12, command = doubt)
    bdo.pack()
    bdo.place(x = 500, y = 150)

    bbr = Button(web_window, text = 'Brainly', bg = 'orange', foreground='white', height = 5, width = 12, command = brain)
    bbr.pack()
    bbr.place(x = 660, y = 150)

    bsh = Button(web_window, text = 'Shaala', bg = 'white', foreground='black', height = 5, width = 12, command = shaala)
    bsh.pack()
    bsh.place(x = 810, y = 150)

    web_window.mainloop()

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
    speak('Congratulations! You guessed the right answer:', value)

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

ideas = []
def idea_box():
    speak("ENTER YOUR IDEAS, YOUR OPINION ON TODAY'S EDUCATION SYSTEM AND WHAT WOULD YOU DO TO MAKE it BETTER?")
    z = takeCommand()
    ideas.append(z)
    for i in range(len(ideas)): #after calling
        print(ideas[i])

grade=''
def quiz():
    speak("Enter level, primary,secondary or tertiary")
    grade = takeCommand()
    if grade == 'primary':
        primaryQuiz()
    elif grade == 'secondary':
        secondaryQuiz()
    elif grade == 'tertiary':
        tertiaryQuiz()
    else:
        speak("no quiz available")
def primaryQuiz():
    qscore = 0
    listQ = ['The tree has a branch filled with green?', 'What part of the body helps you move?' , ' What star shines in the day and provides light? ','Which shape is a laptop?','Your hands have four fingers and a ?']
    listA = ['leaves','legs','sun','rectangle','thumb']
    for i in range(len(listQ)-1):
        randomNum = random.randint(0,(len(listQ)-1))
        speak(listQ[randomNum])
        ans = takeCommand()
        if listA[randomNum] in ans:
            print('Correct Answer')
            speak('Correct Answer')
            qscore+=1
            listQ.pop(randomNum)
        elif 'exit' in ans:
            break
        else:
            print('Wrong Answer')
            speak('Wrong Answer')
            listQ.pop(randomNum)
    print(str(qscore) + " is your final score")
    speak(str(qscore) + " is your final score")
    if qscore>=2:
        score+=1
            
def secondaryQuiz():
    qscore = 0
    listQ = ['Which animal never drinks water?', 'Physical phase of life is called ?' , 'The Largest Cell is? ','Which is the Largest Human Cell?','The Total Number of Bones in the Human Body?']
    listA = ['Kangaroo rat','Protoplasm','ostrich','nerve cell','206']
    for i in range(len(listQ)-1):
        randomNum = random.randint(0,(len(listQ)-1))
        speak(listQ[randomNum])
        ans = takeCommand()
        if listA[randomNum] in ans:
            print('Correct Answer')
            speak('Correct Answer')
            qscore+=1
            listQ.pop(randomNum)
        elif 'exit' in ans:
            break
        else:
            print('Wrong Answer')
            speak('Wrong Answer')
            listQ.pop(randomNum)
    print(str(qscore) + " is your final score")
    speak(str(qscore) + " is your final score")
    if qscore>=2:
        score+=1

def tertiaryQuiz():
    qscore = 0
    listQ = ['The SI Unit of Speed is', 'The movement of earth on its axis is called ?' , ' The Center of Atom is called:','In which Ocean Mariana Trench is located?','Scientis who gave law if gravitation?']
    listA = ['metre per second','rotation','nucleus','pacific ocean','Newton']
    for i in range(len(listQ)-1):
        randomNum = random.randint(0,(len(listQ)-1))
        speak(listQ[randomNum])
        ans = takeCommand()
        if listA[randomNum] in ans:
            print('Correct Answer')
            speak('Correct Answer')
            qscore+=1
            listQ.pop(randomNum)
        elif 'exit' in ans:
            break
        else:
            print('Wrong Answer')
            speak('Wrong Answer')
            listQ.pop(randomNum)
    print(str(qscore) + " is your final score")
    speak(str(qscore) + " is your final score")
    if qscore>=2:
        score+=1

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
        from freegames import memory

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

    btn5 = Button(window, text = 'Memory game',  bg = 'yellow', foreground = 'black', height = 5, command = life, width = 10)
    btn5.pack()
    btn5.place(x = 420, y = 110)


    window.mainloop()



if __name__ == "__main__":
    pass
def game():
	score = 0
	font1 = pygame.font.SysFont('freesansbold.ttf',32)
	textX = 10
	textY = 10
	 #lock for two hours and you have to open all the doors and buttons and find your way through
	#no leaderboard, this is a study app so it should make the student motivated aftet than
	pygame.init()
	screen = pygame.display.set_mode((1000,666))
	pygame.display.set_caption('image')	
	bg = pygame.image.load("edu\djbravo.png").convert()
	quiz = pygame.image.load('edu\dbutton_quiz.png')
	visuals = pygame.image.load('edu\dbutton_visuals.png')
	idea_box = pygame.image.load('edu\dbutton_idea-box.png')
	jokes = pygame.image.load('edu\dbutton_jokes.png')
	facts = pygame.image.load('edu\dbutton_facts.png')
	games = pygame.image.load('edu\dbutton_games.png')
	questionAnnouncer = pygame.image.load('edu\dbutton_question-announcer.png')
	# station = pygame.image.load('edu\square.png')
	spaceship = pygame.image.load('edu\spaceship.png')
	spaceshipX = 100
	spaceshipY = 100
	quizX = 100
	quizY = 100
	visualsX = 300
	visualsY = 250
	idea_boxX = 1000
	idea_boxY = 350
	jokesX = 50
	jokesY = 280
	factsX = 850
	factsY = 450
	gamesX = 300
	gamesY = 500
	questionAnnouncerX = 650
	questionAnnouncerY = 200
	def isCollision(spaceshipX,spaceshipY,x,z):
		distance = math.sqrt(math.pow(spaceshipX-x,2)+math.pow(spaceshipY-z,2))
		if distance <= 20:
			return True
		else:
			return False

	def showScore(x,y):
		score = font1.render("Score: " + str(score), True, (255,255,255))
		screen.blit(score, (x,y))

	def spaceShip(spaceship):
		screen.blit(spaceship,(spaceshipX,spaceshipY))

	def buttons():
		screen.blit(quiz,(quizX,quizY))
		screen.blit(visuals,(visualsX,visualsY))
		screen.blit(idea_box,(idea_boxY,idea_boxY))
		screen.blit(jokes,(jokesX,jokesY))
		screen.blit(facts,(factsX,factsY))
		screen.blit(games,(gamesX,gamesY))
		screen.blit(questionAnnouncer,(questionAnnouncerX,questionAnnouncerY))
		# screen.blit(station,(500,333))
	def quizF():
		pass
		print('passed')
	def visualsF():
		global score
		score += 1
	def idea_boxF():
		global score
		score += 0.5
	def jokesF():
		global score
		if score>=5:
			pass #speak 10 jokes
		else:
			pass #speak 3 jokes only, these jokes will also be limited to one use per day
	def factsF():
		global score
		score +=1 #alwyas open might as well give them extra fax
	def gamesF():
		global score
		score+=1

	def questionAnnouncerF():
		pass
		#requires level or score >= 7 to unlock or make the button even fucntional
		#After that there will be 3 games inside
	spaceshipYc = 0
	spaceshipXc = 0
	status = True
	while (status):
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				status = False 
			elif i.type == pygame.KEYDOWN:
				if i.key == pygame.K_UP:
					spaceshipYc = -0.6
				elif i.key == pygame.K_DOWN:
					spaceshipYc = 0.6
				elif i.key == pygame.K_RIGHT:
					spaceshipXc = 0.6
				elif i.key == pygame.K_LEFT:
					spaceshipXc = -0.6
			elif i.type == pygame.KEYUP:
				if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT:
					spaceshipXc = 0

				elif i.key == pygame.K_UP or i.key == pygame.K_DOWN:
					spaceshipYc = 0
			else:
				pass
			
		if spaceshipX >= 1000:
			spaceshipX = 1000
		elif spaceshipX <= 0:
			spaceshipX = 0
		elif spaceshipY >=666:
			spaceshipY = 666
		elif spaceshipY <= 0:
			spaceshipY = 0
		spaceShip(spaceship)
		if isCollision(spaceshipX,spaceshipY,quizX,quizY):
			spaceshipX = 500
			spaceshipY = 333

			if score >= 3:
				spaceship = pygame.image.load('edu\spaceship2.png')
			spaceShip(spaceship)
			quizF()

		if isCollision(spaceshipX,spaceshipY,visualsX,visualsY):
			spaceshipX = 500
			spaceshipY = 333
			if score >= 3:
				spaceship = pygame.image.load('edu\spaceship2.png')
			spaceShip(spaceship)
			visualsF()
		if isCollision(spaceshipX,spaceshipY, idea_boxX, idea_boxY):
			spaceshipX = 500
			spaceshipY = 333
			if score >= 3:
				spaceship = pygame.image.load('edu\spaceship2.png')
			spaceShip(spaceship)
			idea_boxF()
		if isCollision(spaceshipX,spaceshipY,jokesX,jokesY):
			spaceshipY =333
			spaceshipX = 500
			if score >= 3:
				spaceship = pygame.image.load('edu\spaceship2.png')
			spaceShip(spaceship)
			jokesF()
		if isCollision(spaceshipX, spaceshipY, factsX, factsY):
			spaceshipX = 500
			spaceshipY = 333
			if score >= 3:
				spaceship = pygame.image.load('edu\spaceship2.png')
			spaceShip(spaceship)
			factsF()
		if isCollision(spaceshipX, spaceshipY, gamesX, gamesY) and score>=5:
			spaceshipX = 500
			spaceshipY = 333
			score -=1
			if score >= 3:
				spaceship = pygame.image.load('spaceship2.png')
			spaceShip(spaceship)
			gamesF()
		if isCollision(spaceshipX,spaceshipY, questionAnnouncerX,questionAnnouncerY):
			spaceshipX = 500
			spaceshipY = 333
			score +=1
			if score >=3:
				spaceship = pygame.image.load('edu\spaceship2.png')
			spaceship(spaceship)
			questionAnnouncerF()
		
		spaceshipX += spaceshipXc
		spaceshipY += spaceshipYc
		screen.blit(bg,(0,0))
		spaceShip(spaceship)
		buttons()
		showScore(textX,textY)
		pygame.display.update()

game()