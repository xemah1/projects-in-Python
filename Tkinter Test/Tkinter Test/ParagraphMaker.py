import sys
import os
import random

def paragraph() : 
    k = 0
    with open(os.path.join(sys.path[0], "paragraph.txt"), "r") as f: #paragraph.txt file must be in the same folder as this .py file
        line = f.readline()
        while line : #counts how many lines there are
            k += 1
            line = f.readline()
        i = random.randint(0,k-1)
        k = 0
        f.seek(0)
        line = f.readline()
        while line and k != i : #reads a random line
            k += 1
            line = f.readline()
    #print()
    line = line[:len(line)-2]
    print(line)
    return line