import random
import pygame
import time
import pyautogui
from maze import *

def make_maze():
    global cells, stack, visited, path, maze_color, path_color, drawn_path
    cells = [[Cell(unit_size*j, unit_size*i, unit_size) for j in range(amount)] for i in range(amount)]
    stack = [(0, 0)]
    visited = list(stack)
    generate_maze(stack, cells, visited)
    path = bfs((0, 0), (len(cells)-1, len(cells[0])-1), cells)
    maze_color = list(random.randint(0, 255) for _ in range(3))
    path_color = list(255-maze_color[i] for i in range(3))
    drawn_path = []
cells_on_side = 20
window_side_length = (int(0.8*min(pyautogui.size()))//cells_on_side)*cells_on_side
window = pygame.display.set_mode((window_side_length+1, window_side_length+1))
unit_size = window_side_length//cells_on_side
amount = window_side_length // unit_size
make_maze()
clock = pygame.time.Clock()
running = True
while running:
    drawn_path.append(path[0])
    path.pop(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    for row in cells:
        for cell in row:
            cell.color = maze_color
            cell.draw(window)
    for cell in drawn_path:
        r = cell[0]
        c = cell[1]
        pygame.draw.rect(window, path_color, pygame.Rect(c*unit_size+2, r*unit_size+2, unit_size-2, unit_size-2))
    if(len(path)==0):
        make_maze()
    pygame.display.flip()
    pygame.draw.rect(window, (0, 0, 0), pygame.Rect(0, 0, window_side_length, window_side_length))
    clock.tick(10)
pygame.quit()
