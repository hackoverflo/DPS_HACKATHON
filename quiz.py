import random

grade = input("Primary, Secondary or Tertiary?")

def secondaryQuiz():
    score = 0
    listQ = ['Which animal never drinks water?', 'Physical phase of life is called ?' , 'The Largest Cell is? ','Which is the Largest Human Cell?','The Total Number of Bones in the Human Body?']
    
    listA = ['Kangaroo Rat','Protoplasm','Ostrich','Nerve Cell','204']
    for i in range(len(listQ)-1):
        randInt = random.randint(0,(len(listQ)-1))
        que = input(listQ[randInt])
        if que == listA[randInt].lower():
            print('Correct Answer')
            score +=1
        elif que != listA[randInt]:
            print('Wrong Answer')
            score +=0
    print(score + "is your final score")
def primaryQuiz():
    score = 0
    listQ = ['The tree has a branch filled with green _____.', 'What part of the body helps you move?' , ' What star shines in the day and provides light? ','Which shape is a round?','Your hands have four fingers and a ____.']
    
    listA = ['leaves','legs','sun','circle','thumb']
    for i in range(len(listQ)-1):
        randInt = random.randint(0,(len(listQ)-1))
        que = input(listQ[randInt])
        if que == listA[randInt].lower():
            print('Correct Answer')
            score +=1
        elif que != listA[randInt]:
            print('Wrong Answer')
            score +=0
    print(score + "is your final score")
    
def tertiaryQuiz():
    score = 0
    listQ = ['The SI Unit of Speed is', 'The movement of earth on its axis is called ?' , ' The Center of Atom is called:','In which Ocean Mariana Trench is located?','Scientis who gave law if gravitation?']
    
    listA = ['m/s','rotation','nucleus','pacific ocean','Newton']
    for i in range(len(listQ)-1):
        randInt = random.randint(0,(len(listQ)-1))
        que = input(listQ[randInt])
        if que == listA[randInt].lower():
            print('Correct Answer')
            score +=1
        elif que != listA[randInt]:
            print('Wrong Answer')
            score +=0
    print(score + "is your final score")
    

if grade == 'Primary':
    primaryQuiz()
elif grade == 'Secondary':
    secondaryQuiz()
elif grade == 'Tertiary':
    tertiaryQuiz()
else:
    print(' no quiz available for you ')