from flask import Flask
import random
app = Flask(__name__)


@app.route('/')
def hello_world():
    part1 = ["Putin,", "Hillary,", "Obama", "Fake News,",
             "Mexico,", "Arnold Schwarzenegger", "The Democrats"]
    part2 = ["no talent,", "on the way down,", "really poor numbers,",
             "nasty tone,", "looking like a fool,", "bad hombre,"]
    part3 = ["got destroyed by my ratings.", "rigged the election.",
             "had a much smaller crowd.", "will pay for the wall."]
    part4 = ["So sad", "Apologize", "So true", "Media won't report",
             "Big trouble", "Fantastic job", "Stay tuned"]
    best_words = [part1, part2, part3, part4]
    phrase = ""
    for maliste in best_words:
        phrase += random.choice(maliste) + " "
    return phrase
