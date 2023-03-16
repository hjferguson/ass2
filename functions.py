#Collection of all functions required for this assignment
import random 

def randomEquation():
    symbols = ("*","/","+","-")
    ranInt1 = random.randrange(0,11)
    ranInt2 = random.randrange(0,11)
    ranOperator = random.choice(symbols) 

    print(f"What is {ranInt1} {ranOperator} {ranInt2}?")

    if (ranOperator == "*"):
        answer = ranInt1 * ranInt2
        return answer
    elif (ranOperator == "/"):
        try:
            answer = ranInt1 / ranInt2
            return answer
        except(ZeroDivisionError):
            ranInt1 = random.randrange(1,11)
            answer = ranInt1 / ranInt2
            return answer
    elif (ranOperator == "+"):
        answer = ranInt1 + ranInt2
        return answer
    elif (ranOperator == "-"):
        answer = ranInt1 - ranInt2
        return answer
    else:
        print("Error. Please restart program")

    

def isEmpty(): #need to also check to see if file exsists
    with open("Score.txt", "rb") as file: #rb = read binary. File either empty with 0 bytes, or has something
        size = 4 #set to 4 bytes. Will cover score to 1,000,000,000 which is way more than enough
        content = file.read(size)
        if content:
            return False
    return True

def getScore():
    with open("Score.txt","r") as file:
        content = file.read()
        return content
        
def newScore(score):
    with open("Score.txt", "w") as file:
        file.write(str(score)) #write argument must be str, not int

def menu():
    currScore = 0
    if isEmpty():
        print("Welcome to your math game!")
    else:
        score = getScore()
        print(f"I am happy to meet you again! Your last score was {score}!")

    while True:
        answer = randomEquation()
        userInput = input("Enter answer here:")
        if(str(answer)==userInput):
            print("Correct! Good work!")
            currScore += 1
            exit = input("Would you like to stop playing? y/n").lower()
            if (exit == "y"):
                newScore(currScore)
                break
            elif (exit == "n"):
                continue
        else:
            print(f"Sorry! That's wrong! The correct answer is {answer}.")
            currScore -= 1
            exit = input("Would you like to stop playing? y/n").lower()
            if (exit == "y"):
                newScore(currScore)
                break
            elif (exit == "n"):
                continue  

