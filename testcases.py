import random
import math

stack = [] # holds elements as [i, j]

grid = [[], [], []]

# n : num_rows
# m : num_columns
n = 3
m = 3

visited = []
for i in range(n * m):
    visited.append(0)

# I am maintaining the visited count using a py list where 1 at m * i + j th
# position tells that the cell (i, j) (0-indexed) is visited.

def getUnivisitedNeighbors(i, j):
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

stack.append(3)

# cell_1 and cell_2 are provided as 
def removeWall(cell_1, cell_2):
    difference_cell = 
    

while(len(stack) != 0):
    current = stack.pop()

    # if the current cell has any neighbors which have not been visited
    un = getUnivisitedNeighbors(current[0], current[1])
    if(len(un) == 0):
        continue

    stack.append(current)

    # choose one of the unvisited neighbours
    un_chosen = random.choice(un)

    # remove wall between current cell and the chosen cell
    removeWall(current, un_chosen)

    # mark the chosen cell as visited and push it to the stack
    visited[un_chosen[0] * m + un_chosen[1]] = 1
    stack.append(un_chosen)
    
