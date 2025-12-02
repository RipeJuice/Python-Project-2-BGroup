# SHARED VARIABLES
# If you want to access a variable in this file (or any file really),
# ...use "from {file name} import {variable}
# ...ex. "from config import BOARD_SIZE"
import random
from bisect import bisect_right

# Music files

# Instrumental moods
chill = []
upbeat = [
    ""
]
retro = []
bright = []
restless = []
dreamy = []
hopeful = []
uplifting = []
relaxing = []
electronic = []
focus = [] # Your original probably fits here
# etc.

# All music files
music_files = []

BOARD_SIZE = random.choice([4, 9])