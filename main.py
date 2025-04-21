import tkinter

from X_O_Tk import *
from snake import *


class Games:
    def __init__(self, root):
        self.win = root
        self.win.title("Games")
        self.win.geometry("500x500")
        self.win.resizable(False, False)
        self.buttons_list = []
        self.create_buttons()

    def create_buttons(self):
        button1 = tk.Button(self.win, text="X O", font=("Arial", 20), width=15, command=self.game_x_O)
        button1.pack(pady=35)
        button2 = tk.Button(self.win, text="Snake game", font=("Arial", 20), width=15, command=self.game_snake)
        button2.pack()

    def game_x_O(self):
        root = tk.Tk()
        TicTacToe(root)
        self.win.destroy()
    def game_snake(self):
        root = tk.Tk()
        SnakeGame(root)
        self.win.destroy()


if __name__ == "__main__":
    root = tkinter.Tk()
    g = Games(root)
    root.mainloop()
