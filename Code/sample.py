# Build a program that can generate sentences from the words in the histogram
import random
import histogram

words = histogram.read_file("../Code/data/histogramtext.txt")
word_histogram = histogram.generate_histogram(words)

def uniform_rand_word(histogram):
    random_index = random.randint(0, len(histogram))
    list_of_keys = []
    for entry in histogram:
        list_of_keys.append(entry)
    return list_of_keys[random_index]

print(uniform_rand_word(word_histogram))
    
