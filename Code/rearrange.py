# Import dependencies
import sys
import random

# define variables
input = sys.argv[1:]
output = ""

# shuffle
random.shuffle(input)

#iterate through the input, append to output
for word in input:
     output += f"{word} "

# print output
print(output)