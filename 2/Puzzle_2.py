# Solution to advent of code Day 2 puzzle 1

file = open("input.txt", "r")


# Values for the card picked by player
valueDict = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

# Initializes a score
score = 0

# For each line in the file
for line in file:
    # Initializes results to false
    win = False
    draw = False
    loss = False

    # Saves the card chosen by opponent
    opponent = line[0]
    # Saves wanted result
    result = line[2]

    # If opponent picks Rock
    if opponent == 'A':
        # If we should lose
        if result == 'X':
            player = 'Z'
        # If we  should draw
        elif result == 'Y':
            player = 'X'
         # If we should win
        elif result == 'Z':
            player = 'Y'
            
    # If opponent picks Paper
    elif opponent == 'B':
        # If we should lose
        if result == 'X':
            player = 'X'
        # If we  should draw
        elif result == 'Y':
            player = 'Y'
        # If we should win
        elif result == 'Z':
            player = 'Z'

    # If opponent picks Scissor
    elif opponent == 'C':
        # If we should lose
        if result == 'X':
            player = 'Y'
        # If we  should draw
        elif result == 'Y':
            player = 'Z'
        # If we should win
        elif result == 'Z':
            player = 'X'


# Implementation from Puzzle 1

    # If opponent picked Rock
    if opponent == 'A':
        if player == 'X':
            draw = True
        elif player == 'Y':
            win = True
        elif player == 'Z':
            loss = True
    # If opponent picked Paper
    elif opponent == 'B':
        if player == 'X':
            loss = True
        elif player == 'Y':
            draw = True
        elif player == 'Z':
            win = True
    # If opponent picked Scissor
    elif opponent == 'C':
        if player == 'X':
            win = True
        elif player == 'Y':
            loss = True
        elif player == 'Z':
            draw = True

    # Adds points depending on the result
    if win == True:
        score += 6 + valueDict[player]
    elif draw == True:
        score += 3 + valueDict[player]
    elif loss == True:
        score += valueDict[player]


print(score)
