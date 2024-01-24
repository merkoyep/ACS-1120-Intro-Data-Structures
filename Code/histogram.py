import re

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        #For every line in the file, split each word in the line, and append to words
        words = [re.sub(r'[^a-zA-Z]', '', word) for line in file for word in line.split()]
    return words
    
def generate_histogram(text):
    # takes text and returns a list of lists, where the first item is the word and the second is the frequency.
    histogram = []
    for word in text:
        word_found = False
        for entry in histogram:
            if word == entry[0]:
                entry[1] += 1
                word_found = True
                break
        if not word_found:
            histogram.append([word, 1])
    return histogram

def unique_words(histogram):
    #Takes a histogram and returns the total count (int) of unique words.
    return len(histogram)

def frequency(word, histogram):
    # Takes a word, and histogram, returns times the word appears in the text
    for entry in histogram:
        if word == entry[0]:
            return entry[1]
    return "Word is not in the histogram."

def average(words, histogram):
    # Returns mean frequency of words in text
    return len(words) / unique_words(histogram)

def find_least_frequent_words(histogram):
    # Returns list of least frequent words
    least_frequent_words = []
    lowest_frequency = histogram[0][1]
    for entry in histogram:
        if entry[1] < lowest_frequency:
            lowest_frequency = entry[1]
            least_frequent_words = [entry[0]]
        elif entry[1] == lowest_frequency:
            least_frequent_words.append(entry[0])
    return least_frequent_words



def find_most_frequent_words(histogram):
    # Returns list of most frequent words
    most_frequent_words = []
    highest_frequency = histogram[0][1]
    for entry in histogram:
        if entry[1] > highest_frequency:
            highest_frequency = entry[1]
            most_frequent_words = [entry[0]]
        elif entry[1] == highest_frequency:
            most_frequent_words.append(entry[0])
    return most_frequent_words