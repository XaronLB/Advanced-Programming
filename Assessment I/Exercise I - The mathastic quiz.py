from tkinter import *
from tkinter import ttk as ttk
from random import *

# Iwibndow properties
mainWindow = Tk()
mainWindow.title("Exercise 1: Math Quiz")
mainWindow.geometry(f"360x360")
mainWindow.after(1, mainWindow.wm_state, 'zoomed')


count, solved, attempts, scores = 0, 0, 0, 0

def clearFrame() : #clears the frame
    for widget in frame0.winfo_children() : widget.grid_forget()
    
def displayMenu() : #displays the main menu of the quiz
    clearFrame()
    Label(frame0, text = "The Mathastic Quiz", font = ("Cascadia Code", 32, "bold"), bg = "skyblue").grid(column = 0, row = 0, sticky = "EW")
    Button(frame0, text = "Easy", font = ("Cascadia Code", 20, "bold"), fg = "white", bg = "darkblue", command = lambda: displayProblem(1, generateQuestion(1))).grid(column = 0, row = 1, sticky = "EW")
    Button(frame0, text = "Medium", font = ("Cascadia Code", 20, "bold"), fg = "white", bg = "darkblue", command = lambda: displayProblem(2, generateQuestion(2))).grid(column = 0, row = 2, sticky = "EW")
    Button(frame0, text = "Hard", font = ("Cascadia Code", 20, "bold"), fg = "white", bg = "darkblue", command = lambda: displayProblem(3, generateQuestion(3))).grid(column = 0, row = 3, sticky = "EW")
    Button(frame0, text = "Souls like", font = ("Cascadia Code", 20, "bold"), fg = "white", bg = "darkblue", command = lambda: displayProblem(4, generateQuestion(4))).grid(column = 0, row = 4, sticky = "EW")
    
def randomInt(digits) : #randomly generates the values of the questions
    randFloat = random() * 9.99999999
    return int(randFloat * (10.0 ** (digits - 1)))

def generateQuestion(level) : #generates the questions for the quiz
    question = f"{randomInt(2)} {decideOperation()} {randomInt(1)}" if level == 1 else "0"
    question = f"{randomInt(2)} {decideOperation()} {randomInt(2)}" if level == 2 else question
    question = f"{randomInt(2)} {decideOperation()} {randomInt(2)} {decideOperation()} {randomInt(2)}" if level == 3 else question
    question = f"{randomInt(3)} {decideOperation()} {randomInt(3)} {decideOperation()} {randomInt(3)}" if level == 4 else question
    return question

def isCorrect(userInput, question, level, decrease) : # checks the userinput(answer) and displays the intended output
    global count, scores, solved, attempts
    clearFrame()
    solution = eval(question)
    try :
        userInput = int(userInput)
    except :
        Label(frame0, text = "Make sure it's a number", font = ("Cascadia Code", 32, "bold"), bg = "skyblue").grid(column = 0, row = 0, sticky = "EW")
        Button(frame0, text = "Re-enter Answer", font = ("Cascadia Code", 20, "bold"), fg = "white", bg = "darkblue", command = lambda: displayProblem(level, question, decrease)).grid(column = 0, row = 1, sticky = "EW")
        return
    if userInput != solution and decrease == 1.0 :
        attempts += 1
        Label(frame0, text = "Wrong Answer.", font = ("Cascadia Code", 32, "bold"), bg = "skyblue").grid(column = 0, row = 0, sticky = "EW")
        Label(frame0, text = "50% Decrease", font = ("Cascadia Code", 20, "bold"), bg = "skyblue").grid(column = 0, row = 1, sticky = "EW")
        Button(frame0, text = f"Try Again", font = ("Cascadia Code", 20, "bold"), fg = "white", bg = "darkblue", command = lambda: displayProblem(level, question, 0.5)).grid(column = 0, row = 1, sticky = "EW")
        return
    count += 1
    if userInput == solution :
        solved += 1
        scores += level * decrease * 10
        Label(frame0, text = "Correct", font = ("Cascadia Code", 32, "bold"), bg = "skyblue").grid(column = 0, row = 0, sticky = "EW")
    else :
        attempts += 1
        Label(frame0, text = "Inorrect", font = ("Cascadia Code", 32, "bold"), bg = "skyblue").grid(column = 0, row = 0, sticky = "EW")
    Label(frame0, text = f"Solution: {solution}\nYour Answer: {userInput}", font = ("Cascadia Code", 20, "bold"), bg = "skyblue").grid(column = 0, row = 1, sticky = "EW")
    if count < level * 4 :
        Button(frame0, text = "Continue", font = ("Cascadia Code", 20, "bold"), fg = "white", bg = "darkblue", command = lambda: displayProblem(level, generateQuestion(level))).grid(column = 0, row = 2, sticky = "EW")
        return
    Button(frame0, text = "Results", font = ("Cascadia Code", 20, "bold"), fg = "white", bg = "darkblue", command = lambda: displayResults(level)).grid(column = 0, row = 2, sticky = "EW")

def displayResults(level) : # displays the user final result
    global count, scores, solved, attempts
    percentage = (10 * scores) / (level * 4)
    grade = "not goo(D)" if percentage > 50 else "(F)ail"
    grade = "(C) if you can get better" if percentage > 60 else grade
    grade = "good jo(B)" if percentage > 70 else grade
    grade = "(A)mazing" if percentage > 80 else grade
    clearFrame()
    Label(frame0, text = f"Correct: {solved}\nTries: {attempts}\nPercentage: {round(percentage, 1)}%\nQuestions: {count}", font = ("Cascadia Code", 20, "bold"), bg = "skyblue").grid(column = 0, row = 0, sticky = "EW")
    Label(frame0, text = f"Score: {round(scores, 1)}", font = ("Cascadia Code", 32, "bold"), bg = "skyblue").grid(column = 0, row = 1, sticky = "EW")
    Label(frame0, text = f"Grade: {grade}", font = ("Cascadia Code", 32, "bold"), bg = "skyblue").grid(column = 0, row = 2, sticky = "EW")
    Button(frame0, text = "Menu", font = ("Cascadia Code", 20, "bold"), fg = "white", bg = "darkblue", command = lambda: displayMenu()).grid(column = 0, row = 3, sticky = "EW")
    count, scores, solved, attempts = 0, 0, 0, 0 # resets the values to default

def decideOperation() :
    return "-" if bool(getrandbits(1)) else "+"

def displayProblem(level, question, decrease = 1.0) : #shows the menu where it displays the question and request a userinput
    clearFrame()
    entry0 = Entry(frame0, font = ("Cascadia Code", 20, "bold"))
    Label(frame0, text = question + " =", font = ("Cascadia Code", 32, "bold"), bg = "skyblue").grid(column = 0, row = 0, sticky = "EW")
    entry0.grid(column = 0, row = 1, sticky = "EW")
    Button(frame0, text = "Submit Answer", font = ("Cascadia Code", 20, "bold"), fg = "white", bg = "darkblue", command = lambda: isCorrect(entry0.get(), question, level, decrease)).grid(column = 0, row = 2, sticky = "EW")

# inserts main frame
ttk.Style().configure("frame0.TFrame", background = "skyblue")
frame0 = ttk.Frame(mainWindow, style = "frame0.TFrame", padding = 38)
frame0.place(relx = 0.5, rely = 0.5, anchor = "center")

# shows menu
displayMenu()

mainWindow.mainloop()