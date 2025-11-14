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
import math

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
LIGHT_GRAY = (200, 200, 200)
PRESSED_GRAY = (210, 210, 210)


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

    # Highlights cell for "pressed down" look
    def draw_selection(self, selected_cell, current_time_ms, line_color):
        if selected_cell is None:
            return

        row, col = selected_cell

        # Pulsating effect using sine
        pulse_speed = 0.005
        pulse_value = (math.sin(current_time_ms * pulse_speed) + 1.0) / 2.0
        thickness = int(2 + pulse_value * 3) # Min: 2, Max: 5

        # Draw border lines
        top = (col * CELL_SIZE, row * CELL_SIZE)
        bottom = (col * CELL_SIZE, (row + 1) * CELL_SIZE)
        left = (col * CELL_SIZE, row * CELL_SIZE)
        right = ((col + 1) * CELL_SIZE, row * CELL_SIZE)

        # Draw glow lines
        pygame.draw.line(screen, line_color, top, (top[0] + CELL_SIZE, top[1]), thickness)  # Top
        pygame.draw.line(screen, line_color, bottom, (bottom[0] + CELL_SIZE, bottom[1]), thickness)  # Bottom
        pygame.draw.line(screen, line_color, left, (left[0], left[1] + CELL_SIZE), thickness)  # Left
        pygame.draw.line(screen, line_color, right, (right[0], right[1] + CELL_SIZE), thickness)  # Right

        # Use a slightly darker gray surface to show pressing the cell down
        s = pygame.Surface((CELL_SIZE, CELL_SIZE))
        s.set_alpha(150)  # Make it semi-transparent (0-255)
        s.fill(PRESSED_GRAY)  # Fill with darker gray

        # Blit the effect onto the main screen
        screen.blit(s, (col * CELL_SIZE, row * CELL_SIZE))