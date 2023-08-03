import pygame
import math
pygame.init()
screen = pygame.display.set_mode((1000,666))
pygame.display.set_caption('image')	
bg = pygame.image.load("edu\doggggg.png").convert()
quiz = pygame.image.load('edu\dbutton_quiz.png')
visuals = pygame.image.load('edu\dbutton_visuals.png')
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
	screen.blit(quiz,(600,600))
	screen.blit(visuals,(300,300))

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
			elif spaceshipX > 1000:
				spaceshipX = 1000
			elif spaceshipX < 0:
				spaceshipX = 0
			elif spaceshipY > 666:
				spaceshipY = 666
			elif spaceshipY < 0:
				spaceshipY = 0
			elif i.key == pygame.K_UP or i.key == pygame.K_DOWN:
				spaceshipYc = 0
		elif isCollision(spaceshipX,spaceshipY,600,600):
			quizF()
		elif isCollision(spaceshipX,spaceshipY,300,300):
			visualsF()
	spaceshipX += spaceshipXc
	spaceshipY += spaceshipYc
	screen.blit(bg,(0,0))
	buttons()
	spaceShip()
	pygame.display.update()
	
