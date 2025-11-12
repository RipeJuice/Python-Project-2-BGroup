    # VIEW
# Only recieves simple input and is concerned about displaying what the user sees


# ALLOWS VNC DISPLAY
import os
import tempfile

# Check if XDG_RUNTIME_DIR is set
if 'XDG_RUNTIME_DIR' not in os.environ:
    # Create a temporary directory in /tmp for the runtime
    temp_dir = tempfile.mkdtemp(prefix='runtime-', dir='/tmp')
    os.environ['XDG_RUNTIME_DIR'] = temp_dir
    print(f"Set XDG_RUNTIME_DIR to: {temp_dir}")
else:
    print(f"XDG_RUNTIME_DIR already set to: {os.environ['XDG_RUNTIME_DIR']}")


# Imports
import pygame
import sys
from pygame import display, font, event
from pygame.locals import *

"""
import turtle

grid_size = 500
cell_size = grid_size/9
thin_line = 1
thick_line = 3

screen = turtle._Screen()
screen.setup(width=grid_size + 50, height=gridsize + 50)
screen.title("Sudoku")
screen.listen()

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

def draw_grid(size):
    start_x = grid_size/2
    start_y = grid_size/2
    pen.goto(start_x, start_y)
    pen.pendown()
"""


# Initializes Pygame
pygame.init()

# Dimensions
WIDTH = 540
HEIGHT = 540
GRID_ROWS = 9
GRID_COLS = 9
CELL_SIZE = WIDTH // GRID_COLS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# Display Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sodoku")

# Fonts
font = pygame.font.SysFont("Impact", 40)

# 
def draw_grid():
    screen.fill(BLACK)
    for i in range(GRID_ROWS + 1):
        thickness = 3 if i % 3 == 0 else 1

        # Horizontal lines


     
while True:
    display.update()
    draw_grid()