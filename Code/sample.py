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


    

# 100% = len(words)
# word weight = word_histogram[word] / len(words)
def weighted_sample(histogram):
    list_of_words = []
    list_of_occurences = list(histogram.values())
    for entry in histogram:
        list_of_words.append(entry)
    selected_word = random.choices(list_of_words, list_of_occurences, k=1)[0]
    return selected_word

# def test_weighted_sample():
#     samples = {}
#     for i in range(0, 10000):
#         sample = weighted_sample(word_histogram)
#         if sample in samples:
#             samples[sample] += 1
#         else:
#             samples[sample] = 1
#     return samples

# print(test_weighted_sample())