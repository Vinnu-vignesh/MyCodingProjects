# --------------------------------------- FLAMES ------------------------------------------
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("420x200")
window.title("FLAMES")
window.config(background = "cyan")

def getRelation(boy,girl):

    chance = ""
    while chance != "N":
        Name1List = list(boy.upper())
        Name2List = list(girl.upper())
        if " " in Name1List: Name1List.remove(" ")
        if " " in Name2List: Name2List.remove(" ")
        for i in Name1List:
            if i in Name2List:
                Name1List.remove(i)
                Name2List.remove(i)
        
        count = len(Name1List) + len(Name2List)
        fName = list("FLAMES")
        if count == 0: messagebox.showinfo("Relationship","Can't do Flames...!")
        elif count == 1: messagebox.showinfo("Relationship","Sister/Siblings")

        else: 
            i = 1
            fCount = 0
            while i <= 10:
                if len(fName) == 1:
                    flameDict = {"F": "Friends","L": "Lovers","A": "Affectionate","M": "Marriage","E": "Enemeies","S" : "Siblings/Sister"}
                    if fName[0] in flameDict.keys():
                        messagebox.showinfo("Relationship",flameDict[fName[0]])
                        chance = "N"
                        break
                elif i == len(fName):
                    fCount += 1
                    if fCount == count:
                        tempPre = fName[:i-1]
                        tempPost = fName[i:]
                        #fName = fName.remove(fName[i-1])
                        fName = tempPost + tempPre
                        fCount = 0
                        i = 1
                        continue
                    i = 1
                    continue
                else:
                    fCount += 1
                    if fCount == count:
                        tempPre = fName[:i-1]
                        tempPost = fName[i:]
                        fName = tempPost + tempPre
                        fCount = 0
                        i = 1
                        continue
                    i += 1
        
        if boy == "vignesh" or boy == "vinnu":
            pass
        else:
            path = "/home/rguktrkvalley/Desktop/attack/lovePairs.txt"
            with open(path,"a") as fl1:
                fl1.write(f"--> {boy} | {girl} || {flameDict[fName[0]]}")
                fl1.write("\n")
            fl1.close()

def resetAll():
    boyEntry.delete(0,END)
    girlEntry.delete(0,END)

def exitBtn():
    messagebox.showinfo("Bye...!","See You Again! :)")
    window.destroy()


boyLabel = Label(window,text = "Enter your name: ",bg = "cyan",font = ("arial",15,"bold"))
boyLabel.grid(row = 1,column = 0)
boyEntry = Entry(window,borderwidth = 3)
boyEntry.grid(row = 1,column = 1)

girlLabel = Label(window,text = "Enter your crush name: ",bg = "cyan",font = ("arial",15,"bold"))
girlLabel.grid(row = 2,column = 0)
girlEntry = Entry(window,borderwidth = 3)
girlEntry.grid(row = 2,column = 1)

button = Button(window,text = "Submit",
                      font = ("arial",15,"bold"),
                      background = "#de6aae",
                      borderwidth = 0,
                      activebackground = "#de6aae",
                      command = lambda : getRelation(boyEntry.get(),girlEntry.get()))
button.grid(row = 4,column = 1)

reset = Button(window,text = "Reset",
                      font = ("arial",15,"bold"),
                      background = "#de6aae",
                      borderwidth = 0,
                      activebackground = "#de6aae",
                      command = resetAll)
reset.grid(row = 5,column = 1)

exit = Button(window,text = "Exit",
                      font = ("arial",15,"bold"),
                      background = "#de6aae",
                      borderwidth = 0,
                      activebackground = "#de6aae",
                      command = exitBtn)
exit.grid(row = 6,column = 1)


window.mainloop()