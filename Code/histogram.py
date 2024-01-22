import re

with open("../Code/data/histogramtext.txt", 'r', encoding='utf-8') as file:
    #For every line in the file, split each word in the line, and append to words
    words = [re.sub(r'[^a-zA-Z]', '', word) for line in file for word in line.split()]
    
def histogram(text):
    # takes text and returns a dictionary of each word and its occurence in the file.
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
