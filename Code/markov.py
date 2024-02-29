import re
import histogram
import sample
import random

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
    """Generates an object with words, and a histogram of next words and its occurences"""
    transitions = {}
    for type in types:
        type_transition_object = {type: {}}
        if type[-1] in ['.', '?', '!']:
            "if the word ends in ending punctuation, object is empty."
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


# nth Markov Chains
def generate_n_grams(word_list, n):
    n_grams = []
    for word_index in range(len(word_list) - n + 1):
        n_gram = tuple(word_list[word_index:word_index+n])
        n_grams.append(n_gram)
    return n_grams

def generate_gram_transitions(n_grams):
    """Generates an object with words, and a histogram of next grams and its occurences as values."""
    transitions = {}
    for i in range(len(n_grams) - 1):
        gram = n_grams[i]
        next_word = n_grams[i + 1][-1]
        if gram not in transitions:
            transitions[gram] = {}
        if next_word in transitions[gram]:
            transitions[gram][next_word] += 1
        else:
            transitions[gram][next_word] = 1
    return transitions



# def generate_gram_sentence(starting_gram, transitions, sentence_length=20):
#     """Generate sentences using nth grams based on a max sentence length."""
#     current_gram = starting_gram
#     sentence = list(current_gram)
#     for word in range(sentence_length - len(current_gram)):
#         if current_gram in transitions:
#             possible_next_words = transitions[current_gram]
#             next_word = weighted_sample(possible_next_words)
#             sentence.append(next_word)
#             current_gram = tuple(sentence[-len(current_gram):]) 
#         else:
#             break  
#     if not sentence[-1].endswith('.'):
#         sentence[-1] += '.'
#     return ' '.join(sentence)


def generate_gram_sentence(transitions):
    """Generate sentences using nth grams based on a max sentence length."""
    current_gram = random.choice(list(transitions.keys()))
    sentence = list(current_gram)
    sentence_finished = False
    while not sentence_finished:
        if current_gram in transitions:
            possible_next_words = transitions[current_gram]
            next_word = sample.weighted_sample(possible_next_words)
            sentence.append(next_word)
            if next_word.endswith('.'):
                sentence_finished = True
            current_gram = tuple(sentence[-len(current_gram):]) 
        else:
            sentence_finished = True
    sentence[0] = sentence[0].capitalize()
    if not sentence[-1].endswith('.'):
        sentence[-1] += '.'
    return ' '.join(sentence)
