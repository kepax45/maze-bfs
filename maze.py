import pygame.draw
import random


class Cell:
    id = 0
    def __init__(self, x, y, size, top=False, left=False, bottom=False, right=False):
        self.top = top
        self.size = size
        self.left = left
        self.right = right
        self.bottom = bottom
        self.color = (0, 255, 0)
        self.x = x
        self.y = y
        self.id = Cell.id+1
        Cell.id+=1
    def draw(self, surface):
        if(not self.top):
            pygame.draw.line(surface, self.color, (self.x, self.y), (self.x+self.size, self.y), 1)
        if(not self.bottom):
            pygame.draw.line(surface, self.color, (self.x, self.y+self.size), (self.x + self.size, self.y+self.size), 1)
        if(not self.left):
            pygame.draw.line(surface, self.color, (self.x, self.y), (self.x, self.y + self.size), 1)
        if(not self.right):
            pygame.draw.line(surface, self.color, (self.x+self.size, self.y), (self.x + self.size, self.y + self.size), 1)
def get_surrounding(i, j, cells, visited):
    res = []
    if i > 0 and (i - 1, j) not in visited:
        res.append((i-1, j, "top"))
    if i < len(cells)-1 and (i + 1, j) not in visited:
        res.append((i+1, j, "bottom"))
    if j > 0 and (i, j - 1) not in visited:
        res.append((i, j-1, "left"))
    if j < len(cells[0])-1 and (i, j + 1) not in visited:
        res.append((i, j+1, "right"))
    return res
def get_neighbors(i, j, cells):
    cell = cells[i][j]
    res = []
    if(cell.right == True):
        res.append((i, j+1))
    if(cell.left == True):
        res.append((i, j-1))
    if(cell.top == True):
        res.append((i-1, j))
    if(cell.bottom == True):
        res.append((i+1, j))
    return res
def choose_cell(stack, cells, visited):
    i = stack[-1][0]
    j = stack[-1][1]
    cell = cells[i][j]
    sur = get_surrounding(i, j, cells, visited)
    if(len(sur)==0):
        stack.pop()
        return
    size = random.randint(1, 2)
    for i in range(size):
        choice = sur[random.randint(0, len(sur)-1)]
        direction = choice[2]
        visited.append((choice[0], choice[1]))
        stack.append((choice[0], choice[1]))
        new_cell = cells[choice[0]][choice[1]]
        if(direction == "right"):
            cell.right = True
            new_cell.left = True
        if (direction == "top"):
            cell.top = True
            new_cell.bottom = True
        if (direction == "bottom"):
            cell.bottom = True
            new_cell.top = True
        if (direction == "left"):
            cell.left = True
            new_cell.right = True
        choose_cell(stack, cells, visited)
def generate_maze(stack, cells, visited):
    length = len(cells)*len(cells[0])
    while len(visited) < length:
        choose_cell(stack, cells, visited)
def bfs(s, e, cells):
    visited = [[False for i in range(len(cells[0]))] for i in range(len(cells))]
    prev = [[None for i in range(len(cells[0]))] for i in range(len(cells))]
    queue = [s]
    visited[s[0]][s[1]] = True
    while len(queue)>0:
        node = queue[0]
        i = node[0]
        j = node[1]
        neighbors = get_neighbors(i, j, cells)
        for neighbor in neighbors:
            i = neighbor[0]
            j = neighbor[1]
            if not visited[i][j]:
                queue.append(neighbor)
                visited[i][j] = True
                prev[i][j] = node
        queue.pop(0)
    at = e
    path = []
    while at != None:
        path.append(at)
        at = prev[at[0]][at[1]]
    path = path[::-1]
    return path
    
                
