"""
In general this program is pretty simple, and I want to finish it tonight, so I can move onto the cool stuff for my brother
Primary steps

Load words
Load pickle of saved data (ledger)
--> Should be able to calculate all values based on just the ledger

Select 5 words out of the bunch - pickle may indicate what the 5 words are
select question
Update all probabilities
Either
- select new question
- add new question
Calculate my stats: % Concepts learned, % Concepts learning, % Concepts 
Repeat until all words learned. 
"""

import pickle
import numpy as np
import os.path
import time

# TUNABLE PARAMETERS
WORKING_MEMORY = 5
Pt = 1.0
process_noise = 1.0 # need to make this an exponential function???
Ps = 1 - Pt

def load_data():
    french_words = []
    english_words = []
    with open("french.txt","r",encoding="utf-8") as f:
        for line in f:
            line_split = line.split()
            line_split.pop(0) # remove the word number
            eng = line_split.pop(-1)
            english_words.append(eng)
            french = "".join(line_split)
            french_words.append(french)
    return french_words, english_words

french_words, english_words = load_data()


if os.path.isfile("model.pickle"):
    ledger = pickle.load_data("model.pickle") # just a list of list of data
else:
    ledger = []

# perform calculations on the ledger to determine parameters:
num_words = len(french_words)
init_prob = 0.01*np.ones(num_words) # 1% chance I know the word beforehand

# Select words
indices = np.random.choice(num_words, WORKING_MEMORY,p=init_prob / sum(init_prob), replace=False)
indices_prob = init_prob[indices,]

# LEARN WORDS
print("q for quit")
while True:
    ind = int(indices[ np.random.choice(len(indices), 1, p=indices_prob / sum(indices_prob)) ])
    french_word = french_words[ ind ] 
    eng_word = english_words[ ind ]
    resp = input(f"Word: {french_word}\n")

    # Record history
    if resp == "q":
        break
    elif resp == eng_word:
        print("CORRECT!")
    else:
        print(f"Nope! {french_word} : {eng_word}")
    time.sleep(1)
    print("########################")