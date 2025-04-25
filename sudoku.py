import random
import tkinter as tk
import copy
from tkinter import messagebox


class SudokuBoard:
    pass


class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.cells = {}
        self.user_input = {}
        self.draw_grid()
        # self.draw_buttons()

    def draw_grid(self):
        for i in range(9):
            for j in range(9):
                frame = tk.Frame(self.root, width=200, height=200, borderwidth=1, relief="solid", bg="white")
                frame.grid(row=i, column=j, padx=(1 if j % 3 == 0 else 0), pady=(1 if i % 3 == 0 else 0))
                label = tk.Label(frame, text="", font=("Arial", 20), width=4, height=2)
                label.pack()
                label.bind("<Button-1>")


if __name__ == "__main__":
    root = tk.Tk()
    sudoku = SudokuGUI(root)
    root.mainloop()
