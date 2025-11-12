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
import game_setup
import controller
import view
import pygame

# 10 for Easy, Medium, Hard (4x4) - 30 total
# 10 for Easy, Medium, Hard (9x9) - 30 total
#                                   60 total

running = True
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            # Handle other events like key presses here later

        # Drawing the screen
        draw_grid()
        draw_numbers(current_board)

        # Update the display
        pygame.display.update()

    pygame.quit()
    sys.exit()

# Run the main function
if __name__ == "__main__":
    main()




    
