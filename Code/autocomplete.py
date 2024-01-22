import random
import sys

# define variables
matches = []

# open file
with open("/usr/share/dict/words", 'r', encoding='utf-8') as file:
    words = [line.strip() for line in file]

# construct sentence
for word in words:
    if word.startswith(sys.argv[1]):
        matches.append(word)

# display sentence
print(matches)
