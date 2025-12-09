# GAME SETUP
# Handles main menu, settings, and pre-game configuration.

# Imports
import pygame
import sys
import music
import config
from config import screen, WIDTH, HEIGHT
from config import WHITE, BLACK, LIGHT_GRAY, PRESSED_GRAY
from config import BOARD_SIZE # We will use BOARD_SIZE from config as default
global selected_size
global selected_difficulty

BACKGROUND_IMG = pygame.image.load("../monogram-line-seamless-pattern_8830-622 copy.tiff")

# Initial position for the first image
bg_x1 = 0
# Initial position for the second image (right next to the first one)
bg_x2 = WIDTH

# Speed of the scroll (adjust as needed)
SCROLL_SPEED = 0.1




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
        pygame.draw.rect(screen, LIGHT_GRAY, size4_btn)
        pygame.draw.rect(screen, LIGHT_GRAY, size9_btn)
        draw_text("4 x 4", menu_font, BLACK, screen, WIDTH//2, HEIGHT//3 + 25)
        draw_text("9 x 9", menu_font, BLACK, screen, WIDTH//2, HEIGHT//3 + 85)
        diff_buttons = []
        # Draw difficulty buttons AFTER size is chosen
        if selected_size:

            diff_buttons = []
            diff_list = difficulties_all + (difficulties_9x9_only if selected_size == 9 else [])

            for i, diff in enumerate(diff_list):
                rect = pygame.Rect(WIDTH//4, HEIGHT//2 + 60 + i*60, WIDTH//2, 50)
                diff_buttons.append((rect, diff))
                pygame.draw.rect(screen, LIGHT_GRAY, rect)
                draw_text(diff.upper(), menu_font, BLACK, screen, WIDTH//2, rect.y + 25)

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
                            return selected_size, selected_difficulty

        pygame.display.update()


