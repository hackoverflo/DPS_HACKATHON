import pygame
import math 
import random
from main1 import *
def quiz():
    grade = input("Primary, Secondary or Tertiary?")
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
        listQ = ['The tree has a branch filled with green _____.', 'What part of the body helps you move?' , ' What star shines in the day and provides light? ','Which shape is a round?','Your hands have four fingers and a ____.']

        listA = ['leaves','legs','sun','circle','thumb','Thumb']
        for i in range(len(listQ)-1):
            randInt = random.randint(0,(len(listQ)-1))
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


    if grade == 'Primary':
        primaryQuiz()
    elif grade == 'Secondary':
        secondaryQuiz()
    elif grade == 'Tertiary':
        tertiaryQuiz()
    else:
        print(' no quiz available for you ')

pygame.init()
screen = pygame.display.set_mode((1000,666))
pygame.display.set_caption('image')	
bg = pygame.image.load("edu\doggggg.png").convert()
quizk = pygame.image.load('edu\dbutton_quiz.png')
visuals = pygame.image.load('edu\dbutton_visuals.png')
facts = pygame.image.load('edu\dbutton_question-announcer.png')
spaceship = pygame.image.load('edu\spaceship (1).png')
spaceshipX = 100
spaceshipY = 100
def isCollision(spaceshipX,spaceshipY,x,z):
	distance = math.sqrt(math.pow(spaceshipX-x,2)+math.pow(spaceshipY-z,2))
	if distance < 20:
		return True
	else:
		return False

def spaceShip():
	screen.blit(spaceship,(spaceshipX,spaceshipY))

def buttons():
	screen.blit(quizk,(600,600))
	screen.blit(visuals,(300,300))
	screen.blit(facts,(500,200))
def quizF():
	print('passed')
	
def visualsF():
	print('passed')
	
def questionAnnouncerF():
	print('passed')
	
spaceshipYc = 0
spaceshipXc = 0
status = True
while (status):
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			status = False 
		elif i.type == pygame.KEYDOWN:
			if i.key == pygame.K_UP:
				spaceshipYc = -0.5
			elif i.key == pygame.K_DOWN:
				spaceshipYc = 0.5
			elif i.key == pygame.K_RIGHT:
				spaceshipXc = 0.5
			elif i.key == pygame.K_LEFT:
				spaceshipXc = -0.5
		elif i.type == pygame.KEYUP:
			if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT:
				spaceshipXc = 0
			else:
				spaceshipYc = 0
	
	spaceshipX += spaceshipXc
	spaceshipY += spaceshipYc
	if isCollision(spaceshipX,spaceshipY, 600,600):
		spaceshipX = 100
		spaceshipY = 200
		spaceShip()
		quiz() 
	elif isCollision(spaceshipX,spaceshipY,300,300):
		visualsF()
	elif isCollision(spaceshipX,spaceshipY,500,200):
		questionAnnouncerF()
		
	screen.blit(bg,(0,0))
	buttons()
	spaceShip()
	pygame.display.update()