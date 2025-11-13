import pygame
from config import BOARD_SIZE


class SudokuInputController:
    # starts the game with the selected game mode
    def __init__(self, game_mode):
        # gets the game mode from board_size if it isnt put in
        if game_mode is None:
            self.game_mode = "4x4" if BOARD_SIZE == 4 else "9x9"
        else:
            self.game_mode = game_mode

        self.selected_cell = None  # gets the selected cell
        self.board_size = BOARD_SIZE  # gets the boardsize from the config file

    # changes teh coloumn index to a number
    def get_column_letter(self, col_index):
        return chr(ord('A') + col_index)

    # gets the coloumn number from the user
    def get_column_input(self):
        max_columns = self.board_size

        while True:
            print(f"\nEnter column letter (A-{self.get_column_letter(max_columns - 1)}): ")
            col_input = input().strip().upper()  # gets and organises user input

            # makes sure input length is correct
            if len(col_input) != 1:
                print("Please enter exactly one letter")
                continue

            # makes sure the input is valid
            if not col_input.isalpha():
                print("Please enter a valid letter (A-Z)")
                continue

            # changes the letter to the column_index
            col_index = ord(col_input) - ord('A')

            # makes sure column index is within the size
            if 0 <= col_index < max_columns:
                return col_index
            else:
                print(f"Column must be between A and {self.get_column_letter(max_columns - 1)}")

    # gets the row input from the user
    def get_row_input(self):
        max_rows = self.board_size

        while True:
            print(f"Enter row number (1-{max_rows}): ")
            row_input = input().strip()

            # makes sure the input is good
            if not row_input.isdigit():
                print("Please enter a valid number")
                continue

            # changes to to row index
            row_number = int(row_input)
            row_index = row_number - 1

            # makes sure the row index is within the size
            if 0 <= row_index < max_rows:
                return row_index
            else:
                print(f"Row must be between 1 and {max_rows}")

    # gets the number input from user
    def get_number_input(self):
        max_number = self.board_size

        while True:
            print(f"Enter number (1-{max_number}): ")
            number_input = input().strip()

            # makes sure the input is numeric
            if not number_input.isdigit():
                print("Please enter a valid number")
                continue

            number = int(number_input)

            # makes sure the number is within allowed range
            if 1 <= number <= max_number:
                return number
            else:
                print(f"Number must be between 1 and {max_number}")

    # the youtube guys method to select a cell
    def select_cell_interactive(self):
        print("\n=== Select a Cell ===")

        # gets column and row from user
        col_index = self.get_column_input()
        row_index = self.get_row_input()

        # stores the selected cell and changes it to a readable style
        self.selected_cell = (row_index, col_index)
        col_letter = self.get_column_letter(col_index)

        print(f"Selected cell: {col_letter}{row_index + 1}")
        return self.selected_cell

    # the youtube guys method to enter a number in selected cell
    def enter_number_interactive(self):
        # checks if a cell is selected, if not select one first
        if not self.selected_cell:
            print("No cell selected. Please select a cell first.")
            self.select_cell_interactive()

        # gets a number from user
        number = self.get_number_input()
        row, col = self.selected_cell

        # confirmation message
        print(f"Entering {number} at position ({self.get_column_letter(col)}{row + 1})")
        return row, col, number

    # handles pygame mouse clicks for cell selection
    def handle_mouse_click(self, pos, cell_size):
        """changes mouse position to grid coordinates"""
        x, y = pos
        col = x // cell_size  # gets the column from x position
        row = y // cell_size  # gets the row from y position

        # makes sure that click is within grid boundaries
        if 0 <= row < self.board_size and 0 <= col < self.board_size:
            self.selected_cell = (row, col)  #  saves the selected cell
            return (row, col)
        return None

    # handle pygame keyboard input for number
    def handle_key_press(self, key):
        """handles number input via keyboard"""
        # checks if a cell is selected before number input
        if not self.selected_cell:
            return None, None, None

        row, col = self.selected_cell

        # handle number keys
        if pygame.K_1 <= key <= pygame.K_9:
            number = key - pygame.K_0  # changes key code to actual number
            if 1 <= number <= self.board_size:
                return row, col, number

        return None, None, None

    # quick input reader for commands
    def quick_input(self, input_string):
        try:
            # remove spaces and change to uppercase
            cleaned = input_string.replace(' ', '').upper()

            # handles format with = sign
            if '=' in cleaned:
                position, number_str = cleaned.split('=')
            else:
                # handles format without = sign
                # find where letters end and numbers begin
                for i, char in enumerate(cleaned):
                    if char.isdigit():
                        position = cleaned[:i]  # gets position part
                        number_str = cleaned[i:]  # gets number part
                        break
                else:
                    return None, None, None

            # makes sure position format has at least column and row
            if len(position) < 2:
                return None, None, None

            # parse column letter and row number from position string
            col_letter = position[0]
            row_str = position[1:]

            # makes sure that row and number are actually numbers
            if not row_str.isdigit() or not number_str.isdigit():
                return None, None, None

            # chanhges to grid indices and number value
            col_index = ord(col_letter) - ord('A')  # changes letter to column index
            row_index = int(row_str) - 1  # changes to 0-based row index
            number = int(number_str)  # chaneges number string to integer

            # makes sure that all values are within the size
            if (0 <= row_index < self.board_size and
                    0 <= col_index < self.board_size and
                    1 <= number <= self.board_size):
                self.selected_cell = (row_index, col_index)  # updates the selection
                return row_index, col_index, number
            else:
                return None, None, None

        except (ValueError, IndexError):
            return None, None, None

    # gets currently selected cell coordinates
    def get_selected_cell(self):
        return self.selected_cell

    # clear current cell selection
    def clear_selection(self):
        self.selected_cell = None