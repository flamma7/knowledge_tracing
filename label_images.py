import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import sys
import pickle

"""
My goal is to create a single python dictionary
word -> {"audio" -> "filepath", "image" -> "filepath"}

Want
words/$word/[image.jpg, audio.mp3]

And can give Davis a Python dictionary. Key won't be in the file if it doesn't have an image
word -> {"audio" -> "filepath", "image" -> "filepath"}
"""

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

getch = _Getch()

def get_decision(word):
    # Returns filename, empty string or None for removing the word
    global getch

    dir_path = f"images_renamed/{word}/"
    options = os.listdir(dir_path)
    ind = 0
    while True:
        image_file = dir_path + options[ind]
        print(image_file)
        try:
            img = mpimg.imread(image_file)
        
            plt.text(0,0, word)
            plt.ion()
            imgplot = plt.imshow(img)

            plt.show()
            plt.pause(0.01)
            os.system("wmctrl -a flamma@precision") # Use wm to 
            print("What's the label?")
            char = getch()
            plt.close()

            # Decide what to do with input
            if char == "w": # ACCEPT WORD
                return image_file
            elif char == "d": # Next image
                ind = (ind + 1) % len(options)
            elif char == "a":
                ind = (ind - 1) % len(options)
            elif char == "s":
                return None
            elif char == "f":
                return ""
            elif char == "q":
                return "q"
            else:
                print(f"Unrecognized Input: {char}. Skipping")
        except SyntaxError as se:
            ind = (ind + 1) % len(options)
        
# Check if pickle exists and load it
FILENAME = "labeled_images.pickle"
if os.path.isfile(FILENAME):
    with open (FILENAME, "rb") as f:
        labeled_images = pickle.load(f)
    print(labeled_images)
else:
    labeled_images = {}

for word in os.listdir("images_renamed"):

    if word in labeled_images:
        print(f"{word} already labeled")
        continue

    # Let's work on this image
    decision = get_decision(word)
    if decision is None: # Removing word
        print(f"removing {word}")
        labeled_images[word] = {}
    elif decision == "q":
        break
    elif decision == "":
        print("no image associated")
        labeled_images[word] = {"audio" : f"audio_renamed/{word}.mp3"}
    else:
        print(f"Saving: {decision}")
        labeled_images[word] = {"audio" : f"audio_renamed/{word}.mp3", "image" : f"{decision}"}
    with open(FILENAME, 'wb') as f:
        pickle.dump(labeled_images, f)
    
    
