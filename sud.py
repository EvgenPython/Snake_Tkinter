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
                        print(nums)
                        if self.is_valid(board, i, j, num):
                            board[i][j] = num
                            if self.solve_board(board):
                                return True
                            # board[i][j] = 0
                    return False
        return False

    def is_valid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        box_x = (row // 3) * 3
        box_y = (col // 3) * 3
        for i in range(box_x, box_x + 3):
            for j in range(box_y, box_y + 3):
                if board[i][j] == num:
                    return False
        return True

    def make_puzzle(self, emptys=50):
        puzzle = copy.deepcopy(self.board)
        count = 0
        while count < emptys:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if puzzle[row][col] != 0:
                puzzle[row][col] = 0
                count += 1
        return puzzle


class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.board = SudokuBoard()
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
                label.pack(expand=True)
                label.bind("<Button-1>", lambda e, row=i, col=j: self.cycle_number(row, col))
                num = self.board.puzzle[i][j]
                if num != 0:
                    label.config(text=str(num), fg='black')
                else:
                    self.user_input[(i, j)] = 0
                self.cells[(i, j)] = label


    def draw_buttons(self):
        btn_frame = tk.Frame(self.root)
        btn_frame.grid(row=9, column=0, columnspan=9, pady=10)
        check_btn = tk.Button(btn_frame, text=f"{'Перевірити':^10}", command=self.check_solution)
        check_btn.pack(padx=10)
        exit_btn = tk.Button(btn_frame, text=f"{'Вихід':^10}", command=self.root.quit)
        exit_btn.pack(padx=10)

    def check_solution(self):
        temp_board = copy.deepcopy(self.board.puzzle)
        for (row, col), label in self.cells.items():
            if self.board.puzzle[row][col] == 0:
                val = self.user_input.get((row, col), 0)
                if val == 0:
                    messagebox.showwarning("Error", "Поле не повністю заповнено")
                    return
                temp_board[row][col] = val
        if self.board.solve_board(copy.deepcopy(temp_board)):
            messagebox.showinfo("Вітаю", "Ви виграли")
        else:
            messagebox.showinfo("Error", "Вирішено не вірно")

    def cycle_number(self, row, col):
        if self.board.puzzle[row][col] != 0:
            return
        current = self.user_input.get((row, col), 0)
        next_val = (current % 9) + 1 if current < 9 else 0
        self.user_input[(row, col)] = next_val
        label = self.cells[(row, col)]
        label.config(text=str(next_val) if next_val != 0 else "0", fg="blue")


if __name__ == "__main__":
    root = tk.Tk()
    sudoku = SudokuGUI(root)
    root.mainloop()
