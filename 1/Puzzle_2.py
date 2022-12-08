# Solution to Advent of code Day 1, Puzzle 2

# Opens the file with read
file = open("input.txt", "r")

# Initialize variables
current = 0
top_three = [0, 0, 0]

# Goes through every line in the file
for line in file:

    # If the line is empty with a newline, we've reached a new elf
    if line == "\n":
        # Iterate through the top 3
        for i in range(0, len(top_three)):
            # If an elf is carrying more than the current of the top three
            if current > top_three[i]:
                # Set the current top three to current
                top_three[i] = current
                # Break if found
                break
        # Reset current to 0
        current = 0
    # If the line is not a newline, aka a valid number
    else:
        # Add the current line value to current
        current += int(line.strip())

# Initialize variable for total
total = 0
# Sums the top three into total
for elf in top_three:
    total += elf

#Print the total amount
print(total)
