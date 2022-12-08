#Solution to Advent of code Day 1, Puzzle 1

#Opens the file with read
file = open("input.txt", "r")

#Initialize variables
max = 0
current = 0

#Goes through every line in the file
for line in file:

    #If the line is empty with a newline, we've reached a new elf
    if line == "\n":
        #If the current elf is carrying more than the max
        if current > max:
            #Set the current to new max
            max = current
        #Reset current to 0    
        current = 0
    #If the line is not a newline, aka a valid number
    else:
        #Add the current line value to current
        current += int(line.strip())

#Print the max value
print("The elf with the most amount of calories, carries" , max ,  "calories")
    
