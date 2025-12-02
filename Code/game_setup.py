# GAME SETUP
# Handles main menu, settings, and pre-game configuration.

# Imports
import pygame
import sys
from view import screen, WIDTH, HEIGHT, WHITE, BLACK, font, LIGHT_GRAY, PRESSED_GRAY
from config import BOARD_SIZE # We will use BOARD_SIZE from config as default


BACKGROUND_IMG = pygame.image.load("../monogram-line-seamless-pattern_8830-622 copy.tiff")

# Initial position for the first image
bg_x1 = 0
# Initial position for the second image (right next to the first one)
bg_x2 = WIDTH

# Speed of the scroll (adjust as needed)
SCROLL_SPEED = 0.08

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
    while True:

        draw_scrolling_background()

        font_size = 40
        menu_font = pygame.font.SysFont("Impact", font_size)
        draw_text('Broken Record', menu_font, WHITE, screen, WIDTH // 2, HEIGHT // 4 - 50)
        font_size = 60
        menu_font = pygame.font.SysFont("Impact", font_size)
        draw_text('SODOKU', menu_font, WHITE, screen, WIDTH // 2, HEIGHT // 4)
        title_lines = pygame.Rect(150, 155, 50, 5)
        pygame.draw.rect(screen, WHITE, title_lines)
        title_lines = pygame.Rect(440, 155, 50, 5)
        pygame.draw.rect(screen, WHITE, title_lines)


        # Define button areas (simple Rect objects for collision detection)
        play_button = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50)
        exit_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 70, WIDTH // 2, 50)

        # Draw buttons
        pygame.draw.rect(screen, WHITE, play_button)
        pygame.draw.rect(screen, WHITE, exit_button)
        draw_text('PLAY', font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 25)
        draw_text('EXIT', font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 95)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    # In a real scenario, you'd return selected settings (e.g., "easy", "9")
                    # For now, we return a simple flag to start the game
                    return "start_game"
                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()



        pygame.display.update()