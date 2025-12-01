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
from view import GameView, BOARD_SIZE
from Code import puzzles_and_solutions
from Code import music
from music import load_music
from music import loop_music
from config import BOARD_SIZE
from controller import SudokuInputController
import pygame
import sys
import colorsys
import random

# 10 for Easy, Medium, Hard (4x4) - 30 total
# 10 for Easy, Medium, Hard (9x9) - 30 total
#                                   60 total

def initialize_game_grid(puzzle_string, size):
    grid = []
    for i in range(size):
        row = [] # Rows inside grid
        for j in range(size):
            char = puzzle_string[i * size + j] # Sets char to the original cell value
            value = int(char) if char != '-' else 0 # Makes sure it isn't empty and turns the char into integer

            cell_data = {
                "value": value,
                "notes": set(),
                "is_original": value != 0
            } # Adds data to cell
            row.append(cell_data) # Adds cell to list
        grid.append(row) # Adds entire row to grid
    return grid



def get_row_col_from_mouse(pos, size, width):
    # Translates coordinates into rows and columns
    x, y = pos
    cell_size = width // size
    row = y // cell_size
    col = x // cell_size
    return row, col





def main():
    # --- ADDED: Start Menu Logic ---
    # Call the main menu function from game_setup.py
    # The loop below will only start once main_menu() returns "start_game"
    game_setup.main_menu()
    # --------------------------------
    random_diff = random.choice(["easy", "medium", "hard"])
    current_board = puzzles_and_solutions.grab_puzzle(f"{random_diff}", f"{BOARD_SIZE}", f"{random.randint(1, 10)}")
    print(random_diff)
    print(BOARD_SIZE)
    print(current_board)

    current_board = initialize_game_grid(current_board, BOARD_SIZE)

    game_view_instance = GameView(BOARD_SIZE)


    selected_cell = None # Before game defaults
    note_mode = False # Before game defaults


    # ... the rest of your main function remains the same ...
    from view import WIDTH


    clock = pygame.time.Clock()
    hue = 0

    # Loading the music
    #music.load_music("/Users/geschantz/PycharmProjects/Python-Project-2-BGroup/Code/background_music_1.mp3")
    # playing the music
    #music.loop_music()

    running = True
    while running:
        # ... (rest of the while loop code you already had) ...
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
                if ev.key == pygame.K_n:
                    note_mode = not note_mode
                    print(f"Note mode is now {'ON' if note_mode else 'OFF'}")

                    if selected_cell:
                        row, col = selected_cell
                        # Make sure the user can only modify empty cells
                        if not current_board[row][col]["is_original"]:
                            # Check for valid number
                            if ev.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                                try:
                                    number_pressed = int(ev.unicode)

                                    if note_mode:
                                        # Handles notes
                                        notes_set = current_board[row][col]["notes"]
                                        if number_pressed in notes_set:
                                            notes_set.remove(number_pressed)
                                        else:
                                            notes_set.add(number_pressed)
                                        current_board[row][col]["value"] = 0 # Make sure cell is empty
                                    else:
                                        # Handle main value input
                                        current_board[row][col]["value"] = number_pressed
                                        current_board[row][col]["notes"] = set() # Clears notes
                                except ValueError:
                                    pass # If user didn't press a valid key



                            elif ev.key in [pygame.K_BACKSPACE, pygame.K_DELETE]:
                                print("Cleared cell.")
                                current_board[row][col]["value"] = 0
                                current_board[row][col]["notes"].clear()

        current_time_ms = pygame.time.get_ticks()

        hue = (hue + 0.0005) % 1.0

        if note_mode:
            glow_color = (255, 165, 0)
        else:
            glow_color = (0, 0, 139)


        rgb_tuple = colorsys.hls_to_rgb(hue, 0.125, 1)
        # Scale for Pygame
        dynamic_color = (int(rgb_tuple[0] * 255), int(rgb_tuple[1] * 255), int(rgb_tuple[2] * 255))

        # Drawing the screen
        game_view_instance.draw_grid(dynamic_color)

        game_view_instance.draw_selection(selected_cell, current_time_ms, glow_color)

        game_view_instance.draw_numbers(current_board, dynamic_color)

        # Update the display
        pygame.display.update()

        pygame.time.delay(10)

    pygame.quit()
    sys.exit()

# Run the main function
if __name__ == "__main__":
    main()




    
