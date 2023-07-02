import random
import math

code = {0: "0", 1: "L", 2: "T", 3: "R", 4: "B", 5: "LT", 6: "TR", 7: "RB", 8: "LB", 9: "LTR", 10: "TRB", 11: "RBL", 12: "BLT", 13: "LR", 14: "TB", 15: "TRBL"}

for i in range(len(code.keys())):
    code[i] = ''.join(sorted(code[i]))

# print(code)

stack = [] # holds elements as [i, j]

grid = []

# n : num_rows
# m : num_columns
n = 16
m = 16

# fill the grid
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(15)
    grid.append(temp)

visited = []
for i in range(n * m):
    visited.append(0)

# print(visited)

# I am maintaining the visited count using a py list where 1 at m * i + j th
# position tells that the cell (i, j) (0-indexed) is visited.

def getUnivisitedNeighbors(i, j):
    # print(visited)
    unvisitedNeighbors = [] # Values would be stored in the form of (i, j)
    if(j - 1 >= 0 and visited[m * i + (j - 1)] == 0):
        unvisitedNeighbors.append([i, j - 1])
        
    if(j + 1 < m and visited[m * i + (j + 1)] == 0):
        unvisitedNeighbors.append([i, j + 1])
        
    if(i - 1 >= 0 and visited[m * (i - 1) + j] == 0):
        unvisitedNeighbors.append([i - 1, j])
        
    if(i + 1 < m and visited[m * (i + 1) + j] == 0):
        unvisitedNeighbors.append([i + 1, j])

    return unvisitedNeighbors

visited[1 * m + 0] = 1
stack.append([1, 0])


# cell_1 and cell_2 are provided as 
def removeWall(cell_1, cell_2):
    difference_cell = [0, 0]
    difference_cell[0] = cell_2[0] - cell_1[0]
    difference_cell[1] = cell_2[1] - cell_1[1]

    # the point is that at a time only one of the values of diiference_cell should be non-zero (4 dir only)
    # and that non-zero value should have magnitude of 1, otherwise this fn won't work

    wall_at = 0
    
    if(abs(difference_cell[0]) == 1):
        wall_at = 0
    elif(abs(difference_cell[1]) == 1):
        wall_at = 1

    # # print(code[grid[cell_1[0]][cell_1[1]]])
    
    # return
    str1 = code[grid[cell_1[0]][cell_1[1]]]
    str2 = code[grid[cell_2[0]][cell_2[1]]]

    # print(str1)
    # print(str2)
    
    if(wall_at == 1):
        if(difference_cell[wall_at] == -1):
            str1 = str1.replace("L", '')
            str2 = str2.replace("R", '')
        elif(difference_cell[wall_at] == 1):
            str1 = str1.replace("R", '')
            str2 = str2.replace("L", '')
    
    elif(wall_at == 0):
        if(difference_cell[wall_at] == -1):
            str1 = str1.replace("T", '')
            str2 = str2.replace("B", '')
        elif(difference_cell[wall_at] == 1):
            # print("here")
            str1 = str1.replace("B", '')
            str2 = str2.replace("T", '')
    # print(difference_cell)
    # print(str1)
    # print(str2)
    
    key_1 = [key for key, value in code.items() if value == ''.join(sorted(str1))][0]
    key_2 = [key for key, value in code.items() if value == ''.join(sorted(str2))][0]

    grid[cell_1[0]][cell_1[1]] = key_1
    grid[cell_2[0]][cell_2[1]] = key_2

    return

removeWall([0, 0], [1, 0])
# print(grid[1][0])

while(len(stack) != 0):
    current = stack.pop()

    # print(grid)
    
    # if the current cell has any neighbors which have not been visited
    un = getUnivisitedNeighbors(current[0], current[1])
    # print(un)
    if(len(un) == 0):
        continue

    stack.append(current)

    # choose one of the unvisited neighbours
    un_chosen = random.choice(un)
    # print(un_chosen)
    # remove wall between current cell and the chosen cell
    removeWall(current, un_chosen)

    # mark the chosen cell as visited and push it to the stack
    visited[un_chosen[0] * m + un_chosen[1]] = 1
    stack.append(un_chosen)
   
print(grid)

