import re
import histogram
import sample
import histogram

words = histogram.read_file("../Code/data/histogramtext.txt")
word_histogram = histogram.generate_histogram(words)
test_corpus = "A man, a plan, a canal: Panama! A dog, a panic in a pagoda!"
test_array = test_corpus.split(" ")

# Each word, find a list of words that can happen next, and how many times that happens.
histogram = histogram.generate_histogram(test_array)

def generate_types(word_list):
    types = []
    for word in word_list:
        if word not in types:
            types.append(word)
    return types

def generate_transitions(types, word_list):
    transitions = {}
    for type in types:
        type_transition_object = {type: {}}
        if type[-1] in ['.', '?', '!']:
            type_transition_object[type] = 'empty'
        else:
            for index, word in enumerate(word_list):
                "iterate through corpus"

                if word == type and index < len(word_list) - 1:
                    "If word in the object,find next word"
                    next_word = word_list[index + 1]
                    if next_word in type_transition_object:
                        " check if next_word is in the object's values array"
                        type_transition_object[type][next_word] += 1
                    else:
                        type_transition_object[type][next_word] = 1
        transitions[type] = type_transition_object
    return transitions


def filter_starting_word(histogram):
    capital_words_histogram = {key: value for key, value in histogram.items() if key[0].isupper()}
    return capital_words_histogram

def generate_sentence(word_list, histogram):
    transitions = generate_transitions(generate_types(word_list), word_list)
    sentence = []
    "Filter transitions to index=0 if Cap"
    starting_words_histogram = filter_starting_word(histogram)
    "From there, pick based on sample.weighted_sample"
    first_word = sample.weighted_sample(starting_words_histogram)
    sentence.append(first_word)
    "Trace markov chain using transitions"
    "Select first_word in transitions"
    sentence_finished = False
    while not sentence_finished:
        next_histogram = transitions[sentence[-1]]
        if next_histogram[sentence[-1]] == "empty":
            sentence_finished = True
        else:
            next_word = sample.weighted_sample(next_histogram[sentence[-1]])
            sentence.append(next_word)
    return ' '.join(sentence)

