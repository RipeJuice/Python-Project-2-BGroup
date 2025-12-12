import pygame
pygame.mixer.init()

is_muted = False
previous_volume = 1.0

def load_music(filepath):
    pygame.mixer.music.load(filepath)
    print("music loaded")

def loop_music():
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1.0)
    print("music playing")

def toggle_mute():
    global is_muted, previous_volume
    if not is_muted:
        previous_volume = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(0)
        is_muted = True
        print("MUSIC MUTED")
    else:
        pygame.mixer.music.set_volume(previous_volume)
        is_muted = False
        print("MUSIC UNMUTED")