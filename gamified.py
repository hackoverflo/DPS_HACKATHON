import pygame
from pygame import *
import math
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