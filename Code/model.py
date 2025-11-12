# MODEL (imagine main)
# Only cares about tasks; doesn't ask for input


"""
Different files have different functions:
model.py - organizes everything and runs tasks
view.py - displays what user sees
controller.py - controls user input and connects model and view
game_setup.py - creates the game board and all pre-game setup

"""





# Imports
from Code import controller
from Code import game_setup
from Code import view
from view import GameView
from Code import puzzles_and_solutions
from config import BOARD_SIZE
import pygame
import sys
import colorsys

# 10 for Easy, Medium, Hard (4x4) - 30 total
# 10 for Easy, Medium, Hard (9x9) - 30 total
#                                   60 total
def main():
    current_board = puzzles_and_solutions.grab_puzzle("easy", "4", "2")
    print(current_board)

    game_view_instance = GameView(BOARD_SIZE)

    clock = pygame.time.Clock()
    hue = 0

    running = True
    while running:

        clock.tick(60)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            # Handle other events like key presses here later

        hue = (hue + 0.0005) % 1.0

        rgb_tuple = colorsys.hls_to_rgb(hue, 0.125, 1)
        # Scale for Pygame
        dynamic_color = (int(rgb_tuple[0] * 255), int(rgb_tuple[1] * 255), int(rgb_tuple[2] * 255))

        # Drawing the screen
        game_view_instance.draw_grid(dynamic_color)
        game_view_instance.draw_numbers(current_board, dynamic_color)

        # Update the display
        pygame.display.update()

        pygame.time.delay(10)

    pygame.quit()
    sys.exit()

# Run the main function
if __name__ == "__main__":
    main()




    
