#Harlan Ferguson 101133838
#Collection of all functions required for this assignment
import random 
import time
import math

#-------------------------Random Equation Portion -----------------------------------

def randomEquation():
    symbols = ("*","+","-")
    ranInt1 = random.randrange(1,11)
    ranInt2 = random.randrange(1,11)
    ranOperator = random.choice(symbols) 

    print(f"What is {ranInt1} {ranOperator} {ranInt2}?")

    if (ranOperator == "*"):
        answer = ranInt1 * ranInt2
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

def isFileOk():
    try:
        with open("Score.txt", "r") as file:
            content = file.readline()
    
    except FileNotFoundError:
        print("File not found. No problem! Making a new one")
        with open("Score.txt","w") as file:
            file.write("")
    
    except OSError:
        print("File found, but issue opening it. Please ensure it is not open somewhere else.")

    except Exception as e:
        print(f"Ran into an unexpected error: {e}")

def getScore():
    with open("Score.txt","r") as file:
        content = file.read()
        return content
        
def newScore(score):
    with open("Score.txt", "w") as file:
        file.write(str(score)) #write argument must be str, not int

def mathOne():
    currScore = 0
    isFileOk()
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
                print("Thanks for playing!")
                print(f"Your current score is {currScore}")
                print("WOW!")
                time.sleep(1)
                break
            else:
                continue
        else:
            print(f"Sorry! That's wrong! The correct answer is {answer}.")
            currScore -= 1
            exit = input("Would you like to stop playing? y/n").lower()
            if (exit == "y"):
                newScore(currScore)
                print("Thanks for playing!")
                print(f"Your current score is {currScore}")
                print("WOW!")
                time.sleep(1)
                break
            else:
                continue  

#-------------------------Quadratic Portion -----------------------------------

def discriminant(a, b, c): #used to find roots of quadratic formula
    return b**2 - 4*a*c

def quadratic(a, b, c):
    discrim = discriminant(a, b, c)
    
    if discrim > 0: #if positive, there are two answers
        x1 = (-b + math.sqrt(discrim)) / (2 * a)
        x2 = (-b - math.sqrt(discrim)) / (2 * a)
        return (2, x1, x2) #returns number of solutions and the 2 soltions as a tuple
    elif discrim == 0:
        x1 = -b / (2 * a)
        return (1, x1) #returns 1 solution and the solution as tuple
    else: #answer too complex becuase negative number
        return (0,) #returns a 0 tuple (to work with if-else block later)



def mathTwo():
    print("Welcome to the quadratic game!")
    print("aX^2 + bX + C = 0")
    a = float(input("Please input value for a: "))
    b = float(input("Please input value for b: "))
    c = float(input("Please input value for c: "))
    print(f"Your Quadratic Equation is: {a}X^2 + {b}X + {c} = 0")

    answer = quadratic(a,b,c)
    
    with open("QuadEqu.txt", "w") as file:
        file.write(f"Your Quadratic Equation is: {a}X^2 + {b}X + {c} = 0\n")
        
        if answer[0] == 2:
            print(f"We got two real answers, which are {answer[1]} and {answer[2]}")
            file.write(f"We got two real answers, which are {answer[1]} and {answer[2]}\n")
        elif answer[0] == 1:
            print(f"We got one real answer, which is {answer[1]}")
            file.write(f"We got one real answer, which is {answer[1]}\n")
        else:
            print("The Discriminant is negative, we got a pair of Complex answers.")
            file.write("The Discriminant is negative, we got a pair of Complex answers.\n")

#--------------------Menu to control the games played----------------------------------

def mainMenu():
    while True:
        print("Welcome to math games!")
        print("Type 1 for +,-,* equation game")
        print("Type 2 for quadratic game")
        print("Type 3 to exit")
        userIn = input()
        if(userIn == "1"):
            mathOne()
        elif(userIn == "2"):
            mathTwo()
        elif(userIn == "3"):
            break
        else:
            print("Please enter either 1 2 or 3")
            time.sleep(1) #without a sleep, it's hard to see the input message
            continue