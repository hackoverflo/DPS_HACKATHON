import random

listOfQ = [] 
listOfA = []
n = int(input("Enter number of questions you want to practice.\n"))
for i in range(n):
    quest = input("Enter the Question: ")
    ans = input("Enter the Answer for that question: ")
    listOfQ.append(quest)
    listOfA.append(ans)
# speak("Practice Time")
print("Practice Time")
# speak("Enter your question")



for i in range(0,(len(listOfA)-1)):
    randomN = random.randint(0,(len(listOfQ)-1))
    q = input(listOfQ[randomN]+"\n")
    if (q==listOfA[randomN]):
        print('Correct Answer')
        # speak("Correct Answer")
    else:
        print("Wrong answer")
    