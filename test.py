self.grid = [[Cell(self.canvas, x, y, owner, click_callback) for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]


# res = [i for i in range(0, 5)]
# print(res)
#
# res_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(3):
#     for j in range(3):
#         print(res_2[i][j], end=" ")

res_3 = [[i for i in range(3, 9)] for j in range(3)]
print(res_3)