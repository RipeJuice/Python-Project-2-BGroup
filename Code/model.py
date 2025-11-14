# MODEL (imagine main)
# Only cares about tasks; doesn't ask for input

# HELLO. THIS IS THE MAIN FILE. See below for file functions.
# Right now, our goals are to create an environment where
# the user can interact with the game to play and getting all
# of the boards ready in our dictionaries. We also need a
# home screen and settings, among other things. I would love
# to make this as aesthetically pleasing as possible, so
# if you want to add something visually nice, go ahead.
# I got it to work, so try running this file. If you want to test
# individual code, just change the file at the top next to the play button.

"""
Different files have different functions:
model.py - organizes everything and runs tasks (also holds main loop)
view.py - displays what user sees
controller.py - controls user input and connects model and view
game_setup.py - all pre-game setup like main menu, settings (including setting defaults),
    and more. Could include things like music, etc.
config. py - stores shared variables
puzzles_and_solutions.py - contains puzzles and solutions
"""





# Imports
from Code import controller
from Code import game_setup
from Code import view
from view import GameView
from Code import puzzles_and_solutions
from config import BOARD_SIZE
from controller import SudokuInputController
import pygame
import sys
import colorsys

# 10 for Easy, Medium, Hard (4x4) - 30 total
# 10 for Easy, Medium, Hard (9x9) - 30 total
#                                   60 total

def get_row_col_from_mouse(pos, size, width):
    # Translates coordinates into rows and columns
    x, y = pos
    cell_size = width // size
    row = y // cell_size
    col = x // cell_size
    return row, col




def main():
    current_board = puzzles_and_solutions.grab_puzzle("easy", "4", "3")
    print(current_board)

    game_view_instance = GameView(BOARD_SIZE)

    from view import WIDTH

    selected_cell = None # Defines variable for later (mouse clicks)

    clock = pygame.time.Clock()
    hue = 0

    running = True
    while running:

        clock.tick(60)

        for ev in pygame.event.get():
            # EXIT GAME
            if ev.type == pygame.QUIT: # If they exit pygame
                running = False

            # MOUSE CLICK
            if ev.type == pygame.MOUSEBUTTONDOWN: # Mouse clicks
                row, col = get_row_col_from_mouse(ev.pos, BOARD_SIZE, WIDTH) # Gets coordinates of cell clicked
                selected_cell = (row, col) # Defines that
                print(f"Selected cell: {row}, {col}") # Testing

            # TYPING
            if ev.type == pygame.KEYDOWN:
                if selected_cell:
                    if ev.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                        print(f"Entered number: {ev.unicode}") # For now, later we will input that into game
                    elif ev.key == pygame.K_BACKSPACE:
                        print("Cleared cell.") # For now.
            # Handle other events like key presses here later

        current_time_ms = pygame.time.get_ticks()

        hue = (hue + 0.0005) % 1.0

        rgb_tuple = colorsys.hls_to_rgb(hue, 0.125, 1)
        # Scale for Pygame
        dynamic_color = (int(rgb_tuple[0] * 255), int(rgb_tuple[1] * 255), int(rgb_tuple[2] * 255))
        rgb_glow_tuple = colorsys.hsv_to_rgb(hue, 1, 1)
        dynamic_glow_color =  (int(rgb_glow_tuple[0] * 255), int(rgb_glow_tuple[1] * 255), int(rgb_glow_tuple[2] * 255))
        # Drawing the screen
        game_view_instance.draw_grid(dynamic_color)

        game_view_instance.draw_selection(selected_cell, current_time_ms, dynamic_glow_color)

        game_view_instance.draw_numbers(current_board, dynamic_color)

        # Update the display
        pygame.display.update()

        pygame.time.delay(10)

    pygame.quit()
    sys.exit()

# Run the main function
if __name__ == "__main__":
    main()




    
