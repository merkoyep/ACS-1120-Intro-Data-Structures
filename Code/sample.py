# Build a program that can generate sentences from the words in the histogram
import random
import histogram

words = histogram.read_file("../Code/data/histogramtext.txt")


def uniform_rand_word(histogram):
    random_index = random.randint(0, len(histogram))
    return histogram[random_index]

word_histogram = histogram.generate_histogram(words)

print(histogram.find_most_frequent_words(word_histogram))