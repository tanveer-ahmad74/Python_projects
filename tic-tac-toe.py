from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
import sys
#Global_variables
ActvePlayer =1
ActvePlayer =2

#need a list for player 1 and player 2
P1 = []
P2 = []

root = Tk()
root.title("Tic-Tac_toe Player: 1")
style = ttk.Style()
style.theme_use('classic')
#Add_Buttons

Button_1= ttk.Button(root, text = '')
Button_1.grid(row =0, column = 0,sticky = 'snew',ipadx = 60, ipady= 60)
Button_1.config(command=lambda: ButtonClick(1))

Button_2 = ttk.Button(root, text = '')
Button_2.grid(row =0, column = 1,sticky = 'snew',ipadx = 60, ipady= 60)
Button_2.config(command=lambda: ButtonClick(2))

Button_3 = ttk.Button(root, text = '')
Button_3.grid(row =0, column = 2,sticky = 'snew',ipadx = 60, ipady= 60)
Button_3.config(command=lambda: ButtonClick(3))

Button_4 = ttk.Button(root, text = '')
Button_4.grid(row =1, column = 0,sticky = 'snew',ipadx = 60, ipady= 60)
Button_4.config(command=lambda: ButtonClick(4))

Button_5 = ttk.Button(root, text = '')
Button_5.grid(row =1, column = 1,sticky = 'snew',ipadx = 60, ipady= 60)
Button_5.config(command=lambda: ButtonClick(5))


Button_6 = ttk.Button(root, text = '')
Button_6.grid(row =1, column = 2,sticky = 'snew',ipadx = 60, ipady= 60)
Button_6.config(command=lambda: ButtonClick(6))


Button_7 = ttk.Button(root, text= '')
Button_7.grid(row =2, column = 0, sticky = 'snew',ipadx = 60, ipady= 60)
Button_7.config(command=lambda: ButtonClick(7))


Button_8 = ttk.Button(root, text= '')
Button_8.grid(row =2, column=1, sticky='snew', ipadx= 60, ipady= 60)
Button_8.config(command=lambda: ButtonClick(8))

Button_9 = ttk.Button(root, text = '')
Button_9.grid(row =2, column= 2, sticky= 'snew',ipadx= 60, ipady= 60)
Button_9.config(command=lambda: ButtonClick(9))

def ButtonClick(id):
    global ActvePlayer
    global  P1
    global  P2
    if (ActvePlayer ==1):
       SetLayout(id,"X")
       P1.append(id)
       root.title("Tic-Tac_toe: Player: 2")
       ActvePlayer = 2
       print("P1: {}".format(P1))

    elif ActvePlayer == 2:
       SetLayout(id,"O")
       P2.append(id)
       root.title("Tic-Tac_toe: Player: 1 ")
       ActvePlayer = 1
       print("P2: {}".format(P2))
       Autoplay()
    CheckWinner()
def SetLayout(id,PlayerSymbol):
    if id == 1:
        Button_1.config(text=PlayerSymbol)
        Button_1.state(['disabled'])
    elif id == 2:
        Button_2.config(text=PlayerSymbol)
        Button_2.state(['disabled'])
    elif id == 3:
        Button_3.config(text=PlayerSymbol)
        Button_3.state(['disabled'])
    elif id == 4:
        Button_4.config(text=PlayerSymbol)
        Button_4.state(['disabled'])
    elif id == 5:
        Button_5.config(text=PlayerSymbol)
        Button_5.state(['disabled'])
    elif id == 6:
        Button_6.config(text=PlayerSymbol)
        Button_6.state(['disabled'])
    elif id == 7:
        Button_7.config(text=PlayerSymbol)
        Button_7.state(['disabled'])
    elif id == 8:
        Button_8.config(text=PlayerSymbol)
        Button_8.state(['disabled'])
    elif id == 9:
        Button_9.config(text=PlayerSymbol)
        Button_9.state(['disabled'])



def CheckWinner():
    winner = -1
    if ((1 in P1) and (2 in P1) and (3 in P1)):
        winner = 1
    if ((1 in P2) and (2 in P2) and (3 in P2)):
        winner = 2
    if ((4 in P1) and (5 in P1) and (6 in P1)):
        winner = 1
    if ((4 in P2) and (5 in P2) and (6 in P2)):
        winner = 2
    if ((7 in P1) and (8 in P1) and (9in P1)):
        winner = 1
    if ((7 in P2) and (8 in P2) and (9 in P2)):
        winner = 2

    if ((1 in P1) and (4 in P1) and (7 in P1)):
        winner = 1
    if ((1 in P2) and (4 in P2) and (7 in P2)):
        winner = 2
    if ((2 in P1) and (5 in P1) and (8 in P1)):
        winner = 1
    if ((2 in P2) and (5 in P2) and (8 in P2)):
        winner = 2
    if ((3 in P1) and (6 in P1) and (9 in P1)):
        winner = 1
    if ((3 in P2) and (6 in P2) and (9 in P2)):
        winner = 2

    if winner == 1:
        messagebox.showinfo(title="Congrats", message="Player 1 is the Winner")
        sys.exit()
    elif winner == 2:
        messagebox.showinfo(title="Congrats", message="Player 2 is the Winner")
        sys.exit()



def Autoplay():
    EmptyCells = []
    global P1
    global P2
    for cell in range(9):
        if(not((cell+1 in P1)or(cell+1 in P2))):
            EmptyCells.append(cell+1)

    RandomIndex = randint(0, len(EmptyCells)-1)
    ButtonClick(EmptyCells[RandomIndex])

root.mainloop()
