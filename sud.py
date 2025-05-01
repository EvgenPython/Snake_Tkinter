import random
import tkinter as tk
import copy
from tkinter import messagebox


class SudokuBoard:
    def __init__(self):
        self.board = [[0] * 9 for _ in range(9)]
        self.solve_board()
        self.puzzle = self.make_puzzle()

    def solve_board(self, board=None):
        if board is None:
            board = self.board
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    nums = list(range(1, 9))
                    random.shuffle(nums)
                    for num in nums:
                        if self.is_valid(board, i, j, num):
                            pass

    def is_valid(self, board, row, col, num):
        pass

    def make_puzzle(self):
        pass


class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.cells = {}
        self.user_input = {}
        self.draw_grid()
        self.draw_buttons()

    def draw_grid(self):
        for i in range(9):
            for j in range(9):
                frame = tk.Frame(self.root, width=200, height=200, borderwidth=1, relief="solid", bg="white")
                frame.grid(row=i, column=j, padx=(1 if j % 3 == 0 else 0), pady=(1 if i % 3 == 0 else 0))
                label = tk.Label(frame, text="", font=("Arial", 20), width=4, height=2)
                label.pack()
                label.bind("<Button-1>", lambda e, row=i, col=j: self.cycle_number(row, col))

    def draw_buttons(self):
        btn_frame = tk.Frame(self.root)
        btn_frame.grid(row=9, column=0, columnspan=9, pady=10)
        check_btn = tk.Button(btn_frame, text=f"{'Перевірити':^10}", command=self.check_solution)
        check_btn.pack(padx=10)
        exit_btn = tk.Button(btn_frame, text=f"{'Вихід':^10}", command=self.root.quit)
        exit_btn.pack(padx=10)

    def check_solution(self):
        pass

    def cycle_number(self, row, col):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    sudoku = SudokuGUI(root)
    root.mainloop()
