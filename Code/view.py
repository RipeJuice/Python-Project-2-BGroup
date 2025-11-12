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


# Initializes Pygame
pygame.init()

# BOARD SIZE
BOARD_SIZE = 9

# Dimensions
WIDTH = 540
HEIGHT = 540
GRID_ROWS = BOARD_SIZE
GRID_COLS = BOARD_SIZE
CELL_SIZE = WIDTH // GRID_COLS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# Display Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"Sudoku ULTIMATE")

# Fonts
font_size = 40 if BOARD_SIZE == 9 else 60
font = pygame.font.SysFont("Impact", font_size)


# Takes string and outputs board with characters
def create_board_from_string(board_string, size):
    board = []
    expected_length = size * size
    # Ensure the string is exactly the required length
    if len(board_string) != expected_length:
        print(f"Error: Board string must be exactly {expected_length} characters long for a {size}x{size} board.")
        return None

    for i in range(size):
        row = []
        for j in range(size):
            # Convert character to integer, 0 means empty cell
            num = int(board_string[i * size + j])
            row.append(num)
        board.append(row)
    return board

# 
def draw_grid():
    screen.fill(WHITE)
    # Determine the subgrid size (3 for 9x9, 2 for 4x4)
    subgrid_size = 3 if BOARD_SIZE == 9 else 2
    for i in range(GRID_ROWS + 1):
        # Thicker lines for subgrid boundaries
        thickness = 3 if i % subgrid_size == 0 else 1

        # Horizontal lines
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)
        # Vertical lines
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), thickness)


def draw_numbers(board):
    for i in range(GRID_ROWS):
        for j in range(GRID_COLS):
            num = board[i][j]
            if num != "-":
                text_surface = font.render(str(num), True, BLACK)
                # Center the number within the cell
                text_rect = text_surface.get_rect(center=(j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text_surface, text_rect)





while True:
    display.update()
    draw_grid()
