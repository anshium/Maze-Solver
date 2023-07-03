import random
import math

code = {0: "", 1: "L", 2: "T", 3: "R", 4: "B", 5: "LT", 6: "TR", 7: "RB", 8: "LB", 9: "LTR", 10: "TRB", 11: "RBL", 12: "BLT", 13: "LR", 14: "TB", 15: "TRBL"}

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


# cell_1 and cell_2 are provided as [i, j]
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
    # print([key for key, value in code.items() if value == ''.join(sorted(str1))])
    # print([key for key, value in code.items() if value == ''.join(sorted(str2))])
    key_1 = [key for key, value in code.items() if value == ''.join(sorted(str1))][0]
    key_2 = [key for key, value in code.items() if value == ''.join(sorted(str2))][0]

    grid[cell_1[0]][cell_1[1]] = key_1
    grid[cell_2[0]][cell_2[1]] = key_2

    return

# Add constraints to the maze according to technoxian maze
extremesX = [0, n - 1]
extremesY = [0, m - 1]

corner = [random.choice(extremesX), random.choice(extremesY)]
print(corner)
to_append = [0, 0]
visited[corner[0] * m + corner[1]] = 1

if(corner[0] == n - 1 and corner[1] == m - 1):
    grid[corner[0]][corner[1]] = 10
    to_append[0] = corner[0]
    to_append[1] = corner[1] - 1
    grid[to_append[0]][to_append[1]] = 12
    
elif(corner[0] == 0 and corner[1] == m - 1):
    grid[corner[0]][corner[1]] = 9
    to_append[0] = corner[0] + 1
    to_append[1] = corner[1]
    grid[to_append[0]][to_append[1]] = 11
    
elif(corner[0] == n - 1 and corner[1] == 0):
    grid[corner[0]][corner[1]] = 11
    to_append[0] = corner[0] - 1
    to_append[1] = corner[1]
    grid[to_append[0]][to_append[1]] = 9
    
elif(corner[0] == 0 and corner[1] == 0):
    grid[corner[0]][corner[1]] = 12
    to_append[0] = corner[0]
    to_append[1] = corner[1] + 1
    grid[to_append[0]][to_append[1]] = 10

visited[to_append[0] * m + to_append[1]]
stack.append(to_append)

# Constraints on the end-point
# The endpoints are located at (0th indexed) - (7, 7), (8, 7), (7, 8), (8, 8)
# with a hole somewhere

endTL = [7, 7]
endTR = [7, 8]
endBL = [8, 7]
endBR = [8, 8]

exit_ = random.randint(1, 4)

grid[7][7] = 5
grid[7][8] = 6
grid[8][7] = 8
grid[8][8] = 7

visited[7 * m + 7] = 0 if exit_ == 1 else 1
visited[7 * m + 8] = 0 if exit_ == 2 else 1
visited[8 * m + 7] = 0 if exit_ == 3 else 1
visited[8 * m + 8] = 0 if exit_ == 4 else 1

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
