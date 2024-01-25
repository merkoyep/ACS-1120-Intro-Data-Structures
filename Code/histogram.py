import re


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        #For every line in the file, split each word in the line, and append to words
        words = [re.sub(r'[^a-zA-Z]', '', word).lower() for line in file for word in line.split()]
    return words

def generate_histogram(text):
    # takes text and returns a dictionary of each word as a key and its occurence as values.
    histogram = {}
    for word in text:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

def unique_words(histogram):
    #Takes a histogram and returns the total count (int) of unique words.
    return len(histogram)

def frequency(word, histogram):
    # Takes a word, and histogram, returns times the word appears in the text
    return histogram[word]

def average(words, histogram):
    # Returns mean frequency of words in text
    return len(words) / unique_words(histogram)

def find_least_frequent_words(histogram):
    # Returns list of least frequent words
    lowest_frequency = min(histogram.values())
    least_frequent_words = [key for key, value in histogram.items() if value == lowest_frequency]
    return least_frequent_words

def find_most_frequent_words(histogram):
    # Returns list of most frequent words
    highest_frequency = max(histogram.values())
    most_frequent_words = [key for key, value, in histogram.items() if value == highest_frequency]
    return most_frequent_words