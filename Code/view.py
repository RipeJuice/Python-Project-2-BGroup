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
from config import BOARD_SIZE

# Global Declarations
global BOARD_SIZE

global WIDTH
global HEIGHT
global GRID_ROWS
global GRID_COLS
global CELL_SIZE
global WHITE
global BLACK
global GRAY

global screen

global font

# Initializes Pygame
pygame.init()


    # Dimensions


WIDTH = 640 # was 540
HEIGHT = 640 # was 540
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

class GameView:

    def __init__(self, size):
        self.board_size = size
        # Maybe configure globals here or store relevant objects
        import view as v  # Access globals from view if needed


    def draw_grid(self, grid_color):
        screen.fill(WHITE)
        # Determine the subgrid size (3 for 9x9, 2 for 4x4)
        subgrid_size = 3 if BOARD_SIZE == 9 else 2
        for i in range(GRID_ROWS + 1):
            # Thicker lines for subgrid boundaries
            thickness = 3 if i % subgrid_size == 0 else 1

            # Horizontal lines
            pygame.draw.line(screen, grid_color, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)
            # Vertical lines
            pygame.draw.line(screen, grid_color, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), thickness)


    def draw_numbers(self, board, text_color):
        # Ensure the string is the correct length before proceeding
        expected_length = self.board_size * self.board_size
        if len(board) != expected_length:
            print(f"Error: Expected a string of length {expected_length}, but got {len(board)}")
            return

        # Iterate using the board size (e.g., 9x9 or 4x4)
        for i in range(self.board_size):  # i is the row index
            for j in range(self.board_size):  # j is the column index

                # Calculate the 1D index from the 2D (row, col) coordinates
                index = i * self.board_size + j

                # Get the number from the string at that specific index
                num_char = board[index]

                # Only draw if the cell is not empty
                if num_char != '-':
                    text_surface = font.render(str(num_char), True, text_color)
                    # Center the number within the cell
                    text_rect = text_surface.get_rect(
                        center=(j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2))
                    screen.blit(text_surface, text_rect)
