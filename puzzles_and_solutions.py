#Contains the empty puzzles and the corresponding solutions

#4x4 puzzles
puzzles_4x4 = {
    "easy_size4_1" : "4--12--31-3----",
    "easy_size4_2" : "4--323-432----3-",
    "easy_size4_3" : "-4311-4-3-------",
    "easy_size4_4" : "3-2-12--2---4---",
    "easy_size4_5" : "-24---3-2--44--3",
    "easy_size4_6" : "4--323-432----3-",
    "easy_size4_7" : "3---4--223411---",
    "easy_size4_8" : "-1--24-1-3--42-3",
    "easy_size4_9" : "--4-41--3---14--",
    "easy_size4_10" : "-431-----3--124-",
    "medium_size4_1" : "32-------314--3-",
    "medium_size4_2" : "-42-2-14-23-----",
    "medium_size4_3" : "1--3-3-----13142",
    "medium_size4_4" : "-1-4-23--3-2----",
    "medium_size4_5" : "32-1-1-2-3--1---",
    "medium_size4_6" : "-4-1-----1424-1-",
    "medium_size4_7" : "234---2--2-4-41-",
    "medium_size4_8" : "--313---1--4-413",
    "medium_size4_9" : "3---24----3-4-2-",
    "medium_size4_10" : "4--22-4-34------",
    "hard_size4_1" : "123---21----3--",
    "hard_size4_2" : "---313--3----1--",
    "hard_size4_3" : "---4--1--12-----",
    "hard_size4_4" : "-1----1--32-2-1-",
    "hard_size4_5" : "-3----34---3-42-",
    "hard_size4_6" : "-1---2---3-4----",
    "hard_size4_7" : "-3-----2------23",
    "hard_size4_8" : "-1-3----------34",
    "hard_size4_9" : "---131-4--4-----",
    "hard_size4_10" : "-----31--14-4---",
}

#Function to print the selected puzzle
def grab_puzzle(diff, size, num):
    puzzle = puzzles_4x4.get(f"{diff}_size{size}_{num}")
    print(puzzle)
grab_puzzle("easy", "4", "1")






