# CONTROLLER
# Processes user actions and connects model and view
class SudokuInputController:
    def __init__(self, game_mode):
        self.game_mode = game_mode
        self.selected_cell = None
        
    def get_column_letter(self, col_index):
        return chr(ord('A') + col_index)
    
    def get_column_input(self):
        max_columns = 4 if self.game_mode == "4x4" else 9
        
        while True:
            print(f"\nEnter column letter (A-{self.get_column_letter(max_columns-1)}): ")
            col_input = input().strip().upper()
            
            if len(col_input) != 1:
                print("Please enter exactly one letter")
                continue

                

