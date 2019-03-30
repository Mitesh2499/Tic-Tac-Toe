from tkinter import *
from tkinter import messagebox
from random import *
import winsound
bclick = True


tk = Tk()
tk.title("Tic Tac toe")

n = 9
btns = []

x = randint(0, 1)


def winX():
    winsound.PlaySound("Ta_Da1.wav", winsound.SND_ASYNC)
    messagebox.showinfo("Winner", " Player 1 WIN")


def winO():
    winsound.PlaySound("Ta_Da1.wav", winsound.SND_ASYNC)
    messagebox.showinfo("Winner", " Player2 WIN")


def win(s):
    if s == "X":
        winX()
    else:
        winO()


def check():

    if btns[0]["text"] != "" and btns[1]["text"] == btns[0]["text"] and btns[2]["text"] == btns[1]["text"]:
        win(btns[0]["text"])
    elif btns[3]["text"] != "" and btns[4]["text"] == btns[3]["text"] and btns[5]["text"] == btns[3]["text"]:
        win(btns[3]["text"])
    elif btns[6]["text"] != "" and btns[7]["text"] == btns[6]["text"] and btns[8]["text"] == btns[6]["text"]:
        win(btns[6]["text"])

    elif btns[0]["text"] != "" and btns[3]["text"] == btns[0]["text"] and btns[6]["text"] == btns[0]["text"]:
        win(btns[0]["text"])
    elif btns[1]["text"] != "" and btns[4]["text"] == btns[1]["text"] and btns[7]["text"] == btns[1]["text"]:
        win(btns[1]["text"])
    elif btns[2]["text"] != "" and btns[5]["text"] == btns[2]["text"] and btns[8]["text"] == btns[2]["text"]:
        win(btns[2]["text"])

    elif btns[0]["text"] != "" and btns[4]["text"] == btns[0]["text"] and btns[8]["text"] == btns[0]["text"]:
        win(btns[0]["text"])
    elif btns[2]["text"] != "" and btns[4]["text"] == btns[2]["text"] and btns[6]["text"] == btns[2]["text"]:
        win(btns[2]["text"])
    elif btns[0]["text"] != "" and btns[1]["text"] != "" and btns[2]["text"] != "" and btns[3]["text"] != "" and btns[4]["text"] != "" and btns[5]["text"] != "" and btns[6]["text"] != "" and btns[7]["text"] != "" and btns[8]["text"] != "":
        winsound.PlaySound("Ta_Da1.wav", winsound.SND_ASYNC)
        messagebox.showinfo("Draw Game", "Try Again")


def ttt(button):
    global bclick

    if button["text"] == "" and bclick == True:

        button.config(text="X")
        bclick = False
    elif button["text"] == "" and bclick == False:

        button["text"] = "O"
        bclick = True

    check()


name = Label(None, text="Tic Tac Toe", font=('Times 20 bold'))
name.grid(row=0, column=1)
var = IntVar()

player1 = Radiobutton(text="Player 1 X", variable=var, value=1)
player1.grid(row=1, column=1)
player2 = Radiobutton(text="Player 2 O", variable=var, value=0)
player2.grid(row=2, column=1)
if x == 0:
    bclick = True
    messagebox.showinfo("", " Player 1  will PLay first X")
else:
    bclick = False
    messagebox.showinfo("", " Player 2  will PLay first O")


for i in range(9):
    btns.append(Button(font=('Times 20 bold'), bg='white', fg='black', height=4, width=8))
row = 3
column = 0
index = 1


for i in btns:

    i.grid(row=row, column=column)
    i.config(command=lambda current_button=i: ttt(current_button))

    column += 1
    if index % 3 == 0:
        row += 1
        column = 0
    index += 1

tk.mainloop()
