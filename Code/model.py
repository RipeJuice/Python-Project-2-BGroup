# MODEL (imagine main)
# Model only focuses on tasks. It doesn't take input.
"""
HELLO. THIS IS THE MAIN FILE. See below for file functions.
# Currently, the goals are to create an environment which allows the user to interact with the program
and to get all the boards ready in the dictionaries. We also need a home screen and settings.
I would love to make the game as aesthetically pleasing as possible, so if you want to add visually pleasing features, go ahead.
#It is working, so try running the model file. If you want to test individual code, just change the file at the top next to the play button.
"""

"""
Different files have different functions:
model.py - Organizes all of the files and runs tasks. Also holds main loop.
view.py - Displays what user can see.
controller.py - Controls user input and the connects the model and the view.
game_setup.py - All pre-game setup like main menu, settings (including setting defaults) and more.
config. py - Stores shared variables
puzzles_and_solutions.py - Contains puzzles and solutions
"""


#Imports
from Code import controller
from controller import SudokuInputController
from Code import game_setup
from Code import view
from Code.config import music_files
from view import GameView, BOARD_SIZE
from Code import puzzles_and_solutions
from Code import music
from config import BOARD_SIZE
import pygame
import sys
import colorsys
import random

# 10 for each of Easy, Medium, Hard (4x4) - 30 total
# 10 for each of Easy, Medium, Hard, Evil (9x9) - 30 total
# 60 total


def initialize_game_grid(puzzle_string, size):
    #Creates empty list for the grid
    grid = []
    #A for loop which iterates for the value of either 4 or 9. i is for vertical direction.
    for i in range(size):
        #Creates an empty list for the rows inside the grid.
        row = []
        #A for loop which iterates for the value of either 4 or 9. j is for horizontal direction.
        for j in range(size):
            #Assign the variable char the correct index of the parameter puzzle_string.
            #The correct index is calculated by adding the number of cells per row by the number of rows and adding the position across the current row.
            char = puzzle_string[i * size + j]
            #The variable value is assigned the integer value of the cell if it isn't empty otherwise it's assigned a value of zero.
            value = int(char) if char != '-' else 0

            #Adds initial data to the cell
            cell_data = {
                "value": value,
                "notes": set(),
                "is_original": value != 0
            }
            row.append(cell_data) #Adds the cell to the list for the row
        grid.append(row) #Adds the entire row to the grid
    return grid #Returns the grid



def get_row_col_from_mouse(pos, size, width):
    #Converts the screen into rows and columns based on coordinate system
    x, y = pos #x and y are assigned the respective values from pos
    cell_size = width // size #cell_size is assigned the value of width divided by the board size
    #row and column are  assigned the value of the y  and x position divided by the size of each cell
    row = y // cell_size
    col = x // cell_size
    return row, col #Returns row and column

def main():
    #ADDED: Start Menu Logic
    #Calls the main menu function from game_setup.py
    #The loop  only starts if main_menu() returns "start_game"
    game_setup.main_menu()

    #Randomly selects the difficulty
    random_diff = random.choice(["easy", "medium", "hard"])

    #Randomly selects a number from 1 to 10
    random_int = random.randint(1, 10)

    #Creates current board using the function grab_puzzle
    current_board = puzzles_and_solutions.grab_puzzle(f"{random_diff}", f"{BOARD_SIZE}", f"{random_int}")
    #Print statements for debugging
    print(f"The difficulty is {random_diff}.")
    print(f"The board size is {BOARD_SIZE}x{BOARD_SIZE}.")
    print(f"The current board is {current_board}.")

    #Changes the variable current_board  to the 2D Array created in the function initialize_game_grid
    current_board = initialize_game_grid(current_board, BOARD_SIZE)

    # The variable BOARD_SIZE is passed into the GameView class through the parameter size.
    # Also, an attribute of a specific instance of GameView called board_size is assigned the value of the parameter size which is BOARD_SIZE.
    game_view_instance = GameView(BOARD_SIZE)

    # Before game defaults
    selected_cell = None
    note_mode = False

    # ... the rest of your main function remains the same ...
    from view import WIDTH

    clock = pygame.time.Clock()
    hue = 0

    # Loading the music
    music.load_music(random.choice(music_files))
    # playing the music
    music.loop_music()

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




    
