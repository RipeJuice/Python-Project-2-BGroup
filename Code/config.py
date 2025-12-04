# SHARED VARIABLES
# If you want to access a variable use "from {file name} import {variable}"
#e.g. "from config import BOARD_SIZE"
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

# NOTE: ALL MUSIC FILES MUST BE IN THIS FORMAT
#      >"[title]~[Artist]([genre]).mp3"<
#        *All spaces in title must be seperated by "-" or "_"
#                 *Artist should be exactly as written on site
#                        *Genre should be lower case and match one of the above genres exactly


# All music files
music_files = [
    "../Music/alone~BoDleasons(upbeat).mp3",
    "../Music/amalgam~rockot(elec).mp3",
    "../Music/background-music~DELOSound(relaxing).mp3",
    "../Music/background-music~The_Mountain(focus).mp3",
    "../Music/background_music_1~Unknown(chill).mp3",
    "../Music/dancing-on-the-waves~White_Records(upbeat).mp3",
    "../Music/echoes-of-bach-badinerie~White_Records(upbeat).mp3",
    "../Music/hopeful~Top-Flow(hopeful).mp3",
    "../Music/inspiring~SigmaMusicArtist(bright).mp3",
    "../Music/motivational~Top-Flow(uplifting).mp3",
    "../Music/Movement~SoulProdMusic.mp3",
    "../Music/neon-odyssey_short~Grand_Project(elec).mp3",
    "../Music/sleep-meditation~Petrushkasound(relaxing).mp3",
    "../Music/towards-the-sea~White_Records(upbeat).mp3"
]

def get_data(file):
    i = 0
    j = 0
    title = ""
    artist = ""
    genre = ""
    for char in file[9:]:
        i += 1
        if char == "~":
            break
        title += char
    for char in file[9+i:]:
        j += 1
        if char == "(":
            break
        if char != "~":
            artist += char
    for char in file[9+i+j:]:
        if char == ".":
            break
        if char != "(" and char != ")":
            genre += char

    # Formatting for visibility
    f_title = ""

    flag = False
    i = 0
    for char in title:
        if i == 0 or flag:
            f_title += char.upper()
            flag = False
        else:
            if char == "-" or char == "_":
                f_title += " "
                flag = True
            else:
                f_title += char

        i += 1



    return f_title, artist, genre

song_data = get_data(music_files[13]) # To be used later in model
print(song_data) # Test. You can try running just this file if you want to see

BOARD_SIZE = random.choice([4, 9])