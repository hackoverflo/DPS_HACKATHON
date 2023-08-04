import pygame
import math
def game():
	score = 0 #lock for two hours and you have to open all the doors and buttons and find your way through
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
	# station = pygame.image.load('edu\square.png')
	spaceship = pygame.image.load('edu\spaceship.png')
	spaceshipUpgrade = pygame.image.load('edu\spaceship2.png')
	spaceshipX = 100
	spaceshipY = 100
	def isCollision(spaceshipX,spaceshipY,x,z):
		distance = math.sqrt(math.pow(spaceshipX-x,2)+math.pow(spaceshipY-z,2))
		if distance <= 20:
			return True
		else:
			return False
	
	
	def spaceShip(spaceship):
		screen.blit(spaceship,(spaceshipX,spaceshipY))
	
	def buttons():
		screen.blit(quiz,(600,100))
		screen.blit(visuals,(700,500))
		screen.blit(idea_box,(150,150))
		screen.blit(jokes,(100,250))
		screen.blit(facts,(300,600))
		screen.blit(games,(100,500))
		# screen.blit(station,(500,333))
	def quizF():
		global score
		score +=1
		print('passed')
	def visualsF():
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
		score+=1
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
		if isCollision(spaceshipX,spaceshipY,600,100):
			spaceshipX = 500
			spaceshipY = 333
	
			if score >= 3:
				spaceship = pygame.image.load('edu\spaceship2.png')
			spaceShip(spaceship)
			quizF()
	
		if isCollision(spaceshipX,spaceshipY,700,500):
			spaceshipX = 500
			spaceshipY = 333
			if score >= 3:
				spaceship = pygame.image.load('edu\spaceship2.png')
			spaceShip(spaceship)
			visualsF()
		if isCollision(spaceshipX,spaceshipY,150,150):
			spaceshipX = 500
			spaceshipY = 333
			if score >= 3:
				spaceship = pygame.image.load('edu\spaceship2.png')
			spaceShip(spaceship)
			idea_boxF()
		if isCollision(spaceshipX,spaceshipY,100,250):
			spaceshipY =333
			spaceshipX = 500
			if score >= 3:
				spaceship = pygame.image.load('edu\spaceship2.png')
			spaceShip(spaceship)
			jokesF()
		if isCollision(spaceshipX, spaceshipY, 300,600):
			spaceshipX = 500
			spaceshipY = 333
			if score >= 3:
				spaceship = pygame.image.load('edu\spaceship2.png')
			spaceShip(spaceship)
			factsF()
		if isCollision(spaceshipX, spaceshipY, 100,500) and score>=5:
			spaceshipX = 500
			spaceshipY = 333
			if score >= 3:
				spaceship = pygame.image.load('spaceship2.png')
			spaceShip(spaceship)
			gamesF()
		
		spaceshipX += spaceshipXc
		spaceshipY += spaceshipYc
		screen.blit(bg,(0,0))
		spaceShip(spaceship)
		buttons()
		pygame.display.update()
		
	
