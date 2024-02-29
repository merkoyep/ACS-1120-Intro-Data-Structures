"""Main script, uses other modules to generate sentences."""
from flask import Flask
import histogram
import markov
import random
app = Flask(__name__)

# Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
words = histogram.read_file("../Code/data/histogramtext.txt")
word_histogram = histogram.generate_histogram(words)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    generated_text = markov.generate_sentence(words, word_histogram)
    return generated_text

@app.route("/nth_order/<nth>")
def higher_order(nth):
    """Route that returns a web page containing the generated text using an nth order markov chain."""
    order = int(nth)
    n_grams = markov.generate_n_grams(words, order)
    transitions = markov.generate_gram_transitions(n_grams)
    sentence = markov.generate_gram_sentence(transitions)
    return sentence

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
