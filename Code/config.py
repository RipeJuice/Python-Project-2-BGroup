#SHARED VARIABLES
#If you want to access a variable from any file use "from {file name} import {variable}
#e.g. "from config import BOARD_SIZE"

import random

BOARD_SIZE = random.choice([4, 9])

# Possible artists to choose from:
pop_artists = [
    "Adele",
    "Ariana Grande",
    "Billie Eilish",
    "Bruno Mars",
    "Dua Lipa",
    "Ed Sheeran",
    "Justin Bieber",
    "Lady Gaga",
    "Michael Jackson",
    "Taylor Swift"
]

rock_artists = [
    "Arctic Monkeys",
    "Billie Eilish (collaborations)",
    "Foo Fighters",
    "Green Day",
    "Imagine Dragons",
    "Linkin Park",
    "Nirvana",
    "Paramore",
    "The Beatles",
    "Twenty One Pilots"
]

country_artists = [
    "Blake Shelton",
    "Carrie Underwood",
    "Chris Stapleton",
    "Dan + Shay",
    "Eric Church",
    "Kacey Musgraves",
    "Luke Bryan",
    "Morgan Wallen",
    "Miranda Lambert",
    "Taylor Swift"
]

# Music files

# Instrumental
chill = []
upbeat = []
retro = []
# etc.

# Lyrical (for simplicity, only most well-known)
pop = []
rock = []
country = []
# etc.


# All music files
music_files = []