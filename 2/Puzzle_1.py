# Solution to advent of code Day 2 puzzle 1

file = open("input.txt", "r")


#Values for the card picked by player
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
    # Saves the card chosen by player
    player = line[2]

    #If opponent picked Rock
    if opponent == 'A':
        if player == 'X':
            draw = True
        elif player == 'Y':
            win = True
        elif player == 'Z':
            loss = True
    #If opponent picked Paper
    elif opponent == 'B':
        if player == 'X':
            loss = True
        elif player == 'Y':
            draw = True
        elif player == 'Z':
            win = True
    #If opponent picked Scissor
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
