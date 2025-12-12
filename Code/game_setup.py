# GAME SETUP
# Handles main menu, settings, and pre-game configuration.

# Imports
import pygame
import sys
import music
import config
import math
import random
from config import screen, WIDTH, HEIGHT
from config import WHITE, BLACK, LIGHT_GRAY, PRESSED_GRAY, DARK_GRAY, TRANSWHITE
from config import BOARD_SIZE # We will use BOARD_SIZE from config as default
global selected_size
global selected_difficulty

BACKGROUND_IMG = pygame.image.load("../monogram-line-seamless-pattern_8830-622-copy.png")

# Initial position for the first image
bg_x1 = 0
# Initial position for the second image (right next to the first one)
bg_x2 = WIDTH

# Speed of the scroll (adjust as needed)
SCROLL_SPEED = 0.1

# Constants for bobbing numbers
AMPLITUDE = 8      # Maximum pixels up/down
FREQUENCY = 2.5    # Speed of the bobbing (cycles per sec)

message = random.choice(
    [
    "50+ puzzles!",
    "Challenge Yourself!",
    "Zen Mode Active",
    "Daily Puzzle Ready",
    "Infinite Possibilities",
    "Expertly Crafted",
    "Can You Beat Evil?",
    "High Scores Await",
    "Improve Focus",
    "Master Logic",
    "Your Next Move?",
    "Track Your Stats",
    "Pure Strategy",
    "Break the Record",
    "Time to Play",
    "Brain Power Up!",
    "Rethink Everything",
    "No Guesses Needed",
    "Chaotically Chaotic...",
    # Pop Culture / Fun References
    "All Your Base Are Mine",
    "Gotta Solve 'Em All",
    "The Matrix Awaits",
]
)

# List of animated text elements
animated_decorations = [
    # --- LARGE NUMBERS (font_size = 55) ---
    {
        'text': message,
        'font_size': 30,
        'base_x': WIDTH - (WIDTH // 8) - 80,
        'base_y': HEIGHT // 8 + 5,
        'time_offset': 0.0,         # Starts half a cycle later (for smooth opposition)
        'angle': -25
    },
]


def draw_transparent_text_and_rotate(text, font_object, color_rgba, surface, x, y, angle):
    """
    Renders text with transparency, rotates it by 'angle', and centers
    the resulting rotated surface at (x, y).
    """

    # 1. Render the text surface (original size)
    text_surface = font_object.render(text, True, color_rgba)
    text_surface.set_alpha(color_rgba[3])  # Apply transparency

    rotated_surface = pygame.transform.rotate(text_surface, angle)

    rotated_rect = rotated_surface.get_rect()

    # Set the center of this new rectangle to the desired position (x, y)
    rotated_rect.center = (x, y)

    # 4. Blit the rotated, transparent surface
    surface.blit(rotated_surface, rotated_rect)


def draw_scrolling_background():
    global bg_x1, bg_x2 # Declare globals to modify them

    # 1. Move both images left
    bg_x1 -= SCROLL_SPEED
    bg_x2 -= SCROLL_SPEED

    # 2. Check if the first image is fully off-screen
    if bg_x1 <= -WIDTH:
        bg_x1 = WIDTH # Reset its position to the right of the second image

    # 3. Check if the second image is fully off-screen
    if bg_x2 <= -WIDTH:
        bg_x2 = WIDTH # Reset its position to the right of the first image

    # 4. Draw both images
    screen.blit(BACKGROUND_IMG, (bg_x1, 0))
    screen.blit(BACKGROUND_IMG, (bg_x2, 0))


def draw_text(text, font_used, color, surface, x, y):
    """Helper function to draw text on the screen."""
    textobj = font_used.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    """Displays the main menu and handles user input for game settings."""

    if config.BOARD_SIZE is not None:
        print(f"DEBUG: Menu already executed. Using config values: Size={config.BOARD_SIZE}, Diff={config.DIFFICULTY}")
        return config.BOARD_SIZE, config.DIFFICULTY

    music.load_music("../Music/background_music_1~Unknown(chill).mp3")
    music.loop_music()

    global selected_size
    global selected_difficulty
    """Menu to select board size and difficulty."""
    selected_size = None
    selected_difficulty = None

    # Difficulty pools
    difficulties_all = ["easy", "medium", "hard"]
    difficulties_9x9_only = ["evil"]



    while True:

        draw_scrolling_background()


        # --- SIZE BUTTONS ---
        font_size = 20
        draw_text('v0.8.0', pygame.font.SysFont("Arial", font_size), WHITE, screen, WIDTH - (WIDTH // 20), HEIGHT - (HEIGHT // 30))
        size4_btn = pygame.Rect(WIDTH // 4, HEIGHT // 3, WIDTH // 2, 50)
        size9_btn = pygame.Rect(WIDTH // 4, HEIGHT // 3 + 60, WIDTH // 2, 50)
        font_size = 40
        menu_font = pygame.font.SysFont("Impact", font_size)
        draw_text('Broken Record', menu_font, WHITE, screen, WIDTH // 2, HEIGHT // 4 - 50)
        font_size = 60
        menu_font = pygame.font.SysFont("Impact", font_size)
        draw_text('SUDOKU', menu_font, WHITE, screen, WIDTH // 2, HEIGHT // 4)
        title_lines = pygame.Rect(150, 155, 50, 5)
        pygame.draw.rect(screen, WHITE, title_lines)
        title_lines = pygame.Rect(440, 155, 50, 5)
        pygame.draw.rect(screen, WHITE, title_lines)
        font_size = 40
        pygame.draw.rect(screen, DARK_GRAY, pygame.Rect(WIDTH // 4 + 5, HEIGHT // 3 + 5, WIDTH // 2, 50))
        # pygame.draw.rect(screen, DARK_GRAY, pygame.Rect(WIDTH // 4 + 5, HEIGHT // 2 + 15 + i * 60 + 50, WIDTH // 2, 50))
        pygame.draw.rect(screen, DARK_GRAY, pygame.Rect(WIDTH // 4 + 5, HEIGHT // 3 + 60 + 5, WIDTH // 2, 50))
        pygame.draw.rect(screen, WHITE, size4_btn)
        pygame.draw.rect(screen, WHITE, size9_btn)

        draw_text("4 x 4", pygame.font.SysFont("Impact", 55), BLACK, screen, WIDTH//2, HEIGHT//3 + 25)
        draw_text("9 x 9", pygame.font.SysFont("Impact", 55), BLACK, screen, WIDTH//2, HEIGHT//3 + 85)
        diff_buttons = []

        # Music Icon
        music_icon = pygame.image.load('../Images/music_icon3.png').convert_alpha()
        music_icon_rect = music_icon.get_rect()

        music_icon_rect.centerx = WIDTH // 8
        music_icon_rect.centery = HEIGHT // 8

        screen.blit(music_icon, music_icon_rect)

        # Settings Icon
        settings_icon = pygame.image.load('../Images/settings--v2.png').convert_alpha()
        settings_icon_rect = settings_icon.get_rect()

        settings_icon_rect.centerx = WIDTH // 8
        settings_icon_rect.centery = HEIGHT // 8 + 100

        screen.blit(settings_icon, settings_icon_rect)

        # BOBBING ANIMATION
        current_time = pygame.time.get_ticks() / 1000.0

        # DRAW THE ANIMATED DECORATIONS
        for item in animated_decorations:
            # Calculate the Y-Offset, incorporating the unique 'time_offset'
            # item['time_offset'] shifts the phase, making the bobbing asynchronous
            y_offset = AMPLITUDE * math.sin(FREQUENCY * (current_time + item['time_offset']))

            # Calculate the final animated position
            animated_y = item['base_y'] + y_offset

            # Create the specific font instance needed for this item
            # NOTE: Creating fonts inside the loop is slightly inefficient, but simple.
            # For optimization, create all font objects before the loop.
            decor_font = pygame.font.SysFont("Impact", item['font_size'])

            # Use the new transparent drawing function
            draw_transparent_text_and_rotate(
                item['text'],
                decor_font,
                TRANSWHITE,
                screen,
                item['base_x'],  # Use base_x
                animated_y,  # Use the bobbing y-position
                item['angle']  # Pass the angle here
            )



        # Draw difficulty buttons AFTER size is chosen
        if selected_size:

            diff_buttons = []
            diff_list = difficulties_all + (difficulties_9x9_only if selected_size == 9 else [])

            pygame.draw.rect(screen, WHITE, pygame.Rect(WIDTH // 3, HEIGHT // 3 + 110 + 30, WIDTH // 3, 5))
            for i, diff in enumerate(diff_list):
                pygame.draw.rect(screen, DARK_GRAY, pygame.Rect(WIDTH // 4 + 5, HEIGHT // 2 + 15 + i * 60 + 50, WIDTH // 2, 50))
                rect = pygame.Rect(WIDTH//4, HEIGHT//2 + 60 + i*60, WIDTH//2, 50)
                diff_buttons.append((rect, diff))
                pygame.draw.rect(screen, WHITE, rect)
                # move to the right a bit, the same amount away as it is from the bottom of the button

                draw_text(diff.upper(), pygame.font.SysFont("Impact", 55), BLACK, screen, WIDTH//2, rect.y + 25)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # SIZE
                if size4_btn.collidepoint(event.pos):
                    selected_size = 4

                if size9_btn.collidepoint(event.pos):
                    selected_size = 9

                # DIFFICULTY
                if selected_size:
                    for rect, diff in diff_buttons:
                        if rect.collidepoint(event.pos):
                            selected_difficulty = diff
                            print(selected_difficulty)
                            print(selected_size)

                            config.BOARD_SIZE = selected_size
                            config.DIFFICULTY = selected_difficulty

                            print(f"Game Settings Selected: Size={config.BOARD_SIZE}, Diff={config.DIFFICULTY}")
                            return selected_size, selected_difficulty

        pygame.display.update()

pygame.init()
main_menu()


