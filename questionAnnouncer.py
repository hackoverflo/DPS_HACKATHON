import random

listOfQ = [] 
listOfA = []
for i in range(5):
    quest = input("Enter the Question: ")
    ans = input("Enter the Answer for that question: ")
    listOfQ.append(quest)
    listOfA.append(ans)
    yOrN = input("Do you want to ask yourself questions?")
    if yOrN == 'Y':
        randInt = random.randint(0,(len(listOfQ)-1))
        print(listOfQ[randInt])
        if listOfQ[randInt] == listOfA[randInt]:
            print('correct answer !')