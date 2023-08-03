import webbrowser
from freegames import memory
import random
from random import randint

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

def memory_game():
    print("enjoy game")
    memory
    
ideas = []
def idea_box():
    z = input("Enter your ideas pertaining education system and how it could be changed.\n")
    ideas.append(z)
    for i in range(len(ideas)): #after calling
        print(ideas[i])

def math_guess():
    
    start = 1
    end = 100
    value = randint(start, end)
    print("I'm thinking of a number between", start, 'and', end)
    guess = None
    while guess != value:
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