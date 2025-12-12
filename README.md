SUD😭KU
 Purpose
Sudoku Broken Record is designed to provide an engaging and customizable Sudoku experience by combining traditional puzzle gameplay with modern visuals, animations, and quality-of-life features like note-taking and clickable cell selection.
The program allows players to:
Select puzzle difficulty
Choose board size (4x4 or 9x9)
Enter numbers with keyboard or mouse
Keep notes inside cells
Enjoy animated and glowing visual effects
The goal was to create a Sudoku game that feels like a real application, not just a school project.
 Project Overview
This program is separated into multiple components using the Model–View–Controller (MVC) design pattern. This makes the game easier to understand, debug, and extend.
A menu system allows the player to choose settings before gameplay.
The board loads from pre-written puzzles.
The user interacts using keyboard and mouse.
The screen updates dynamically every frame.
Game Design
Gameplay Features
Multiple difficulty levels (Easy, Medium, Hard, Evil)
Board sizes: 4x4 and 9x9
Notes Mode (for pencil markings)
Clickable cells
Locking original numbers
Animated glowing selection outline
Smooth visuals
Background music
Program Structure
The code is organized into multiple files with clear responsibilities:
model.py               → Main game loop & task manager
controller.py          → User input handling
view.py                → Drawing and animations
game_setup.py          → Main menu & settings
config.py              → Global variables (board size, settings)
puzzles_and_solutions.py → Sudoku puzzle database
music.py               → Background audio manager
Each file has a well-defined role, making the project scalable and easy to read.
 Game Logic
Cell Selection
When a player clicks:
Row, col = get_row_col_from_mouse(ev.pos, BOARD_SIZE, WIDTH)
selected_cell = (row, col)
This translates mouse position into grid coordinates.
Number Input Logic
If the user presses a key:
if pygame.K_1 <= key <= pygame.K_9:
number = key - pygame.K_1 + 1
Numbers only update empty (non-original) cells.
Notes System
Notes are stored as a Python set() inside each cell:
"notes": set()
When Note Mode is ON:
Pressing a number adds/removes the note.
The main value stays empty.
Invalid Moves
Original numbers cannot be changed:
if not board[row][col]["is_original"]
Visual System
The visuals use:
Pulsing sine-wave glow animation for selection
Dynamic hue-shifting grid
Note numbers drawn in small font inside each cell
Thick grid borders for subgrids
Selection Animation:
pulse = (sin(time) + 1) / 2
thickness = 2 + pulse * 3
Notes Layout:
Small numbers appear in mini 3×3 grids inside a cell.
Code Documentation
Important functions are documented and structured:
Example: Grid Initialization
def initialize_game_grid(puzzle_string, size):
Creates a 2D list of dictionaries that store:
Value
Notes
Locked state
Example: Puzzle Fetching
grab_puzzle(difficulty, size, number)
Safely retrieves puzzle strings from the database.
failsafes prevent:
Puzzle size mismatch
Out-of-range values
Invalid keyboard input
How to Run
Install Pygame:
pip install pygame
Run the game:
python model.py

Input
Action
Mouse Click
Select cell
Number Keys
Insert number
N
Toggle Note Mode
Backspace
Clear cell
ESC
Exit



