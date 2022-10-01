import os
import tkinter as tk

# This is the window root widget
from tkinter import messagebox
from tkinter.messagebox import showinfo

root = tk.Tk()
turn = [True]
count = [0]
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

def restart():
    root.destroy()
    os.startfile("main.py")

def show_win():

    if turn:
        messagebox.showinfo("Window", "Player 1 Won!")

    else:
        messagebox.showinfo("Window", "Player 2 Won!")

    restart()


def check_win():
    if ((board[0][0] == board[0][1] == board[0][2] == ("X" and "O")) or
            (board[1][0] == board[1][1] == board[1][2] == ("X" and "O")) or
            (board[2][0] == board[2][1] == board[2][2] == ("X" and "O")) or
            (board[0][0] == board[1][0] == board[2][0] == ("X" and "O")) or
            (board[0][1] == board[1][1] == board[2][1] == ("X" and "O")) or
            (board[0][2] == board[1][2] == board[2][2] == ("X" and "O")) or
            (board[0][0] == board[1][1] == board[2][0] == ("X" and "O")) or
            (board[0][2] == board[1][1] == board[2][0] == ("X" and "O"))):
        show_win()
    if count[0] >= 9:
        showinfo("Window", " IT'S A TIE!!!!")


def update_board(r, c, sign):
    board[r][c] = sign
    print(board)
    check_win()


def handle_click(r, c):
    # grid_slaves gets specific widget with row column combo
    widget = root.grid_slaves(row=r, column=c)[0]
    if widget["text"] == "":
        if turn[0]:
            widget["text"] = "O"
            update_board(r, c, "O")
            turn[0] = False
        else:
            widget["text"] = "X"
            update_board(r, c, "X")
            turn[0] = True
    else:
        pass
    count[0] = count[0]+1


def initiate_GUI():
    for i in range(3):
        root.columnconfigure(i, weight=1, minsize=75)
        root.rowconfigure(i, weight=1, minsize=50)

        for j in range(3):
            label = tk.Label(master=root,
                             height=30,
                             width=30,
                             highlightthickness=4,
                             highlightbackground="#37d3ff"
                             )
            label.grid(row=i, column=j)
            # label.pack(fill=tk.BOTH)
            label.bind("<Button-1>",
                       lambda x, row=i, column=j: handle_click(row, column))

    root.mainloop()


initiate_GUI()

# If three in a row then game is won
# If all spot filled up without 3 in a row then no winner
# Have option to restart game once won