import tkinter as tk
import random
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.window = root
        self.window.title("Tic Tac Toe")
        self.player = "x"
        self.computer = "O"
        self.board = [""] * 9
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.window, text="", font=("Arial", 40), width=5, height=2,
                               command=lambda i=i: self.player_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def player_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)
            if self.check_winner(self.player):
                messagebox.showinfo("Game End", "You Win!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game End", "Нічия")
                self.reset_game()
            else:
                self.window.after(200, self.comp_move)

    def comp_move(self):
        empty_indexes = [i for i, val in enumerate(self.board) if val == ""]

        move = random.choice(empty_indexes)
        self.board[move] = self.computer
        self.buttons[move].config(text=self.computer)
        if self.check_winner(self.computer):
            messagebox.showinfo("Game Over", "Comp Win!")
            self.reset_game()
        elif "" not in self.board:
            messagebox.showinfo("Game End", "Нічия")
            self.reset_game()

    def reset_game(self):
        self.board = [""] * 9
        for btn in self.buttons:
            btn.config(text="")

    def check_winner(self, symbol):
        combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for a, b, c in combos:
            if self.board[a] == self.board[b] == self.board[c] == symbol:
                return True
        return False



