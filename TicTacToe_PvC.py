# Python program for Tic-Tac-Toe game...

# -------- Required Modules ---------------
from tkinter import *
import random

# -------- Outlook of the reult -----------

window = Tk()
window.geometry("420x480")
window.config(background = "#0ff")
window.title("Tic-Tac-Toe")
titleLabel = Label(window,text = "Tic-Tac-Toe",
                          font = ("MV Boli",40,"bold"),
                          bg = "#0ff",
                          fg = "#000")
titleLabel.pack()

ticFrame = Frame(window,bg = "pink",bd = 5,relief = SUNKEN)
ticFrame.pack()

# ---------- Main Code -----------------------------

# ---------- Functions -----------
def nextTurn(row,column,play):

    if buttons[row][column]['text'] == "" and checkWinner() is False:
        if play == Players[0]:
            buttons[row][column]['text'] = play
            if checkWinner() is False:
                x = y = [0,1,2]
                crow,ccolumn = random.choice(x),random.choice(y)
                while buttons[crow][ccolumn]['text'] != "":
                    crow,ccolumn = random.choice(x),random.choice(y)
                buttons[crow][ccolumn]['text'] = Players[1]
                if checkWinner() is True:
                    playerLabel.config(text = ("Computer Wins!"))
                elif checkWinner() == "Tie":
                    playerLabel.config(text = ("TIE!"))

            elif checkWinner() is True:
                playerLabel.config(text = (Players[0]+" Wins!"))
            elif checkWinner() == "Tie":
                playerLabel.config(text = ("TIE!"))


def checkWinner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg = "#1de027",activebackground = "#1de027")
            buttons[row][1].config(bg = "#1de027",activebackground = "#1de027")
            buttons[row][2].config(bg = "#1de027",activebackground = "#1de027")
            return True
    
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg = "#1de027",activebackground = "#1de027")
            buttons[1][column].config(bg = "#1de027",activebackground = "#1de027")
            buttons[2][column].config(bg = "#1de027",activebackground = "#1de027")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg = "#1de027",activebackground = "#1de027")
        buttons[1][1].config(bg = "#1de027",activebackground = "#1de027")
        buttons[2][2].config(bg = "#1de027",activebackground = "#1de027")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg = "#1de027",activebackground = "#1de027")
        buttons[1][1].config(bg = "#1de027",activebackground = "#1de027")
        buttons[2][0].config(bg = "#1de027",activebackground = "#1de027")
        return True
    
    elif emptySpaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg = "#eb0909",activebackground = "#eb0909")
        return "Tie"
    else:
        return False

    

def emptySpaces():
    
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

def newGame():

    playerLabel.config(text = Players[0]+" turn")

    for Row in range(3):
        for Column in range(3):
            if (Row+Column)%2 == 0:
                buttons[Row][Column].config(text = "",bg = "#a1a1a1",activebackground = "#d6cbd1")
            else:
                buttons[Row][Column].config(text = "",bg = "#f0f0f0",activebackground = "#f0f0f0")



# ---------- Driving Code ----------

Players = ["X","O"]

player = Players[0]
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

playerLabel = Label(window,text = "player[X] turn",font = ('consolas',35,'bold'),bg = "#0ff")
playerLabel.pack()

resetBtn = Button(window,text = "Restart",font = ('consolas',40,'bold'),bg = "#0ff",activebackground = "#0ff",command = newGame)
resetBtn.pack(side = "right")

for x in range(3):
        for y in range(3):
            if (x+y)%2 == 0:
                buttons[x][y] = Button(ticFrame,text = "",font = ("consolas",25,"bold"),bg = "#a1a1a1",activebackground = "#d6cbd1",width = 3,height = 2,
                                    command = lambda row = x,column = y,play = player: nextTurn(row,column,play))
                buttons[x][y].grid(row = x,column = y)
            else:
                buttons[x][y] = Button(ticFrame,text = "",font = ("consolas",25,"bold"),width = 3,height = 2,
                                    command = lambda row = x,column = y,play = player: nextTurn(row,column,play))
                buttons[x][y].grid(row = x,column = y)


window.mainloop()