from tkinter import *
import math

def calculate():
    playLevel=entLevel.get()
    curExp=entCurExp.get()
    maxExp=entMaxExp.get()
    curMon=monster.get()
    curParty=partyMembers.get()

    expNeed=int(maxExp)-int(curExp)

    if curMon=="Baby Shroom":
        bExpPer=12
        monLevel=1
    elif curMon=="Shroom":
        bExpPer=36
        monLevel=3
    elif curMon == "Elder Shroom":
        bExpPer=60
        monLevel=5
    elif curMon == "Crabby":
        bExpPer=84
        monLevel=7
    elif curMon == "Goblin":
        bExpPer=108
        monLevel=9
    elif curMon == "Scarecrow":
        bExpPer=156
        monLevel=13
    elif curMon == "Spider":
        bExpPer=156
        monLevel=15
    elif curMon == "Rubee":
        bExpPer=200
        monLevel=17

    if int(playLevel)>(int(monLevel+9)):
        playLevel=(int(monLevel)+9)

    expPer=bExpPer*(.1*(int(monLevel)-(int(playLevel)-10)))

    if curParty==5:
        expPer*=1.2
    elif curParty!=0:
        expPer*=1.1

    killNeed=math.ceil(int(expNeed)/int(expPer))
    output.configure(text="Output: " + str(killNeed))

root = Tk()

root.title("Monster Calculator")

partyMembers = IntVar()
monster = StringVar()

lblLevelInput = Label(root, text="Input your level", font="Arial")
lblCurExpInput = Label(root, text="\tInput the amount of exp you have", font="Arial")
lblMaxExpInput = Label(root, text="\tInput the amount of exp it takes to level up", font="Arial")
lblPartyCount = Label(root, text="\tHow many other people are in your party?", font="Arial")
lblMonster = Label(root, text="\tWhat monster are you fighting?", font="Arial")

entLevel = Entry(root)
entCurExp = Entry(root)
entMaxExp = Entry(root)

optParty = OptionMenu(root, partyMembers, 0, 1, 2, 3, 4, 5)
optParty.configure(font=("Arial", 12))
optMonster = OptionMenu(root, monster,"Baby Shroom", "Shroom", "Elder Shroom", "Crabby", "Goblin", "Scarecrow", "Spider", "Rubee")
optMonster.configure(font=("Arial",12))

btnCalculate = Button(root, text="Calculate", command=calculate, font="Arial")

lblLevelInput.grid(row=0, column=0)
lblCurExpInput.grid(row=0, column=1)
lblMaxExpInput.grid(row=0, column=2)
lblPartyCount.grid(row=0, column=3)
lblMonster.grid(row=0, column=4)
entLevel.grid(row=1, column=0)
entCurExp.grid(row=1, column=1)
entMaxExp.grid(row=1, column=2)
optParty.grid(row=1, column=3)
optMonster.grid(row=1, column=4)
btnCalculate.grid(row=2, column=0)

output = Label(root, text="", font="Arial")
output.grid(row=2, column=1)

root.mainloop()
