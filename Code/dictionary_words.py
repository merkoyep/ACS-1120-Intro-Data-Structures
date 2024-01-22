import random
import sys

# define variables
num_of_words = int(sys.argv[1])
sentence = ""

# open file
with open("/usr/share/dict/words", 'r', encoding='utf-8') as file:
    words = [line.strip() for line in file]

# construct sentence
for i in range(num_of_words):
    if i == num_of_words - 1:
        sentence += f"{words[random.randint(0, len(words) - 1)]}."
    else:
        sentence += f"{words[random.randint(0, len(words) - 1)]} "

# display sentence
print(sentence)
