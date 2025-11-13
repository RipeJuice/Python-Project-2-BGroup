# CONTROLLER

# Still working on this. I'll get to it later. --Malachi

import pygame
import sys



class SudokuController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.running = True

    def run_game_loop(self):
        # The main loop moves from model.py to the controller
        while self.running:
            # Clock handling, dynamic colors logic (from model.py main) can go here
            # ...

            self.handle_events()
            self.update_view()
            # ... (pygame.display.update() and delay/clock.tick() might move here)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Need a utility function here or pass screen info
                # row, col = self.get_row_col_from_mouse(event.pos)
                # self.view.set_selection(row, col) # Or call model to update selection

                print(f"Click detected in controller at {event.pos}")

            if event.type == pygame.KEYDOWN:
                # Pass keyboard input to the model or view to process
                pass  # self.model.handle_key(event.key)

    # Need a function to translate mouse position (can be global utility or in view)
    def get_row_col_from_mouse(self, pos, size, width):
        x, y = pos
        cell_size = width // size
        row = y // cell_size
        col = x // cell_size
        return row, col

    def update_view(self):
        # This is where we tell the view to draw the current state
        pass  # self.view.update_display(self.model.current_board_string)


