
import random # Import random library for game to function.

# Actual program
print('Lets play a game of shell game, choose any cup and if the cup has the ball underneath it you win. There is ten cups and you are blindfolded.')
print('Choose a number through 1-10, this will be your choice for the cup in left to right chronological order.')
userInput = input()
ballPlaceholder = random.randrange(1,10)


if int(userInput) == ballPlaceholder:
    print('You have won!')
elif int(userInput) < ballPlaceholder:
    print('You have lost')
elif int(userInput) > ballPlaceholder:
    print('You have lost')