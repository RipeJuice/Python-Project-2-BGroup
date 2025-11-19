# GAME SETUP
# Handles main menu, settings, and pre-game configuration.

# Imports
import pygame
import sys
from view import screen, WIDTH, HEIGHT, WHITE, BLACK, font, LIGHT_GRAY, PRESSED_GRAY
from config import BOARD_SIZE # We will use BOARD_SIZE from config as default



def draw_text(text, font_used, color, surface, x, y):
    """Helper function to draw text on the screen."""
    textobj = font_used.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    """Displays the main menu and handles user input for game settings."""
    while True:
        screen.fill(WHITE)
        draw_text('Sudoku ULTIMATE', font, BLACK, screen, WIDTH // 2, HEIGHT // 4)

        # Define button areas (simple Rect objects for collision detection)
        play_button = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50)
        exit_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 70, WIDTH // 2, 50)

        # Draw buttons
        pygame.draw.rect(screen, LIGHT_GRAY, play_button)
        pygame.draw.rect(screen, LIGHT_GRAY, exit_button)
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