#The purpose of music.py is to play background music during the game.

#Importing PyGame
import pygame

#Initializing the mixer module to load and play sounds
pygame.mixer.init()

#Function to load audio file
def load_music(filepath):
    pygame.mixer.music.load(filepath)
    print("music loaded")

#Function to loop the music indefinitely by passing in -1 as a parameter
def loop_music():
    pygame.mixer.music.play(-1)
    print("music playing")