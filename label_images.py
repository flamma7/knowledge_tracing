from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import string
import sys
import shutil

fig=plt.figure()

# Viewingfile = sys.argv[1]
Viewingfile = "images/action/000001.jpg"

# TODO LEFT OFF ON READING IMAGES IN AND SELECTING THE BEST OR IGNORING


for test_file in open(Viewingfile, "r").readlines(): 

    fig.set_tight_layout(True)
    plt.ion()
    image=mpimg.imread(test_file + ".ps.png")
    ax = fig.add_subplot(1, 1, 1)
    imgplot = plt.imshow(image)
    plt.show()

    print test_file
    a = raw_input('Next plot?\n')
    if a == "1":
        print "Do something..I've skipped these details"
    plt.clf()

plt.close()