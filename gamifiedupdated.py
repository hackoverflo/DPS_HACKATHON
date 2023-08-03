import pygame
import math
pygame.init()
screen = pygame.display.set_mode((1000,666))
pygame.display.set_caption('image')	
bg = pygame.image.load("edu\doggggg.png").convert()
quiz = pygame.image.load('edu\dbutton_quiz.png')
visuals = pygame.image.load('edu\dbutton_visuals.png')
idea_box = pygame.image.load('edu\dbutton_idea-box.png')
jokes = pygame.image.load('edu\dbutton_jokes.png')
facts = pygame.image.load('edu\dbutton_facts.png')
games = pygame.image.load('edu\dbutton_games.png')
station = pygame.image.load('edu\square.png')
spaceship = pygame.image.load('edu\spaceship (1).png')
spaceshipX = 100
spaceshipY = 100
def isCollision(spaceshipX,spaceshipY,x,z):
	distance = math.sqrt(math.pow(spaceshipX-x,2)+math.pow(spaceshipY-z,2))
	if distance <= 20:
		return True
	else:
		return False


def spaceShip():
	screen.blit(spaceship,(spaceshipX,spaceshipY))

def buttons():
	screen.blit(quiz,(600,100))
	screen.blit(visuals,(700,500))
	screen.blit(idea_box,(150,150))
	screen.blit(jokes,(100,250))
	screen.blit(facts,(300,600))
	screen.blit(games,(100,500))
	screen.blit(station,(500,333))
def quizF():
	print('passed')
def visualsF():
	pass
spaceshipYc = 0
spaceshipXc = 0
status = True
while (status):
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			status = False 
		elif i.type == pygame.KEYDOWN:
			if i.key == pygame.K_UP:
				spaceshipYc = -0.3
			elif i.key == pygame.K_DOWN:
				spaceshipYc = 0.3
			elif i.key == pygame.K_RIGHT:
				spaceshipXc = 0.3
			elif i.key == pygame.K_LEFT:
				spaceshipXc = -0.3
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
	spaceShip()
	if isCollision(spaceshipX,spaceshipY,600,100):
		spaceshipX = 500
		spaceshipY = 333
		spaceShip()
		quizF()
	if isCollision(spaceshipX,spaceshipY,700,500):
		spaceshipX = 500
		spaceshipY = 333
		spaceShip()
		visualsF()
	spaceshipX += spaceshipXc
	spaceshipY += spaceshipYc
	screen.blit(bg,(0,0))
	buttons()
	spaceShip()
	pygame.display.update()
	
