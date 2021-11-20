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

def get_selection_probs(arr):
    return (1 - arr) / (len(arr) - sum(arr))

class WorkingMemory:
    def __init__(self, probs, indices, ledger):
        self.probs = probs # Probability I know each index
        self.indices = indices # index of words in working memory
        self.ledger = ledger # user responses

    def update_prob(self, ind, new_prob):
        assert new_prob < 1.0
        self.probs[ind] = new_prob
    
    @property
    def indices_probs(self):
        return self.probs[self.indices]

    def get_guess_probability(self): # TODO make more complex, weighted based on number of words I've seen
        # This may actually be an overestimate
        num_words_in_memory = len(self.indices)
        return 1 / num_words_in_memory
    
FILENAME = "last_working_memory.pickle"

# TUNABLE PARAMETERS
WORKING_MEMORY_SIZE_START = 5
pT = 0.15 # Chance I learned the word, after this example --> this may be dependent on working memory size
pS = 0.2 # Slip probability, chance I screw up even though I know a word

process_noise = 1.0 # TODO need to make this an exponential function?

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
NUM_WORDS = len(french_words)

if os.path.isfile(FILENAME):
    work_mem = pickle.load_data(FILENAME)
else:
    init_probs = 0.01*np.ones(NUM_WORDS) # 1% chance I know the word beforehand
    sel_probs = get_selection_probs(init_probs)
    indices = np.random.choice(NUM_WORDS, WORKING_MEMORY_SIZE_START,p=sel_probs, replace=False).astype(int)
    work_mem = WorkingMemory(init_probs, indices, [])

# LEARN WORDS
print("q for quit")
while True:
    sel_probs = get_selection_probs(work_mem.indices_probs)
    ind = int( indices[ np.random.choice(len(indices), 1, p=sel_probs) ] )
    french_word = french_words[ ind ] 
    eng_word = english_words[ ind ]
    resp = input(f"Word: {french_word}\n")

    pG = work_mem.get_guess_probability()
    prior = work_mem.probs[ind]

    # Record history
    if resp == "q":
        break
    elif resp == eng_word:
        print("CORRECT!")
        likelihood = (prior * (1 - pS)) / ( prior*(1-pS) + (1 - prior)*pG )
    else:
        print(f"Nope! {french_word} : {eng_word}")
        likelihood = (prior * pS) / ( prior*pS + (1 - prior)*(1-pG) )
    post = likelihood + (1-likelihood)*pT
    print(f"{prior} -> {post}")
    work_mem.update_prob(ind, post)
    time.sleep(1)
    print("########################")

with open(FILENAME, "wb") as output_file:
    pickle.dump(work_mem, output_file)
    print("Working Memory Saved")