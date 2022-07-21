import os
import sys
import random

def password() :
    rr = phrase()
    numbers = []
    ourword = []
    ourword = word()
    rr.append(ourword[1])
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    length = len(alphabet)
    for k in ourword[1] :
        for i in range(length) :
            if(k == alphabet[i]) :
                numbers.append(i+1)
    print()
    print(rr)
    print(numbers)
    newnumbers = numbers
    newword = ""
    diviser = ""
    length = len(newnumbers)
    multiplier = (rr[1])%(length+1)
    for k in range(length) :
        if (newnumbers[k]>= 22) :
            newnumbers[k] -= 21
        else : 
            newnumbers[k] += 5
    for k in range(length) :
        newword = newword + str((newnumbers[k])*multiplier) + str(ord(alphabet[(newnumbers[k])-1]))
        diviser = diviser + str(newnumbers[k])
    password = (int(newword))%(int(diviser))
    password = str(password)
    print(password)
    return password

def word() :
    k = 0
    with open(os.path.join(sys.path[0], "words.txt"), "r") as f: #words.txt file must be in the same folder as this .py file
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
    print()
    print(line)
    k = 0
    i = 0
    r = 0
    for k in line : 
        if k == "\"" : 
            r += 1 
        i += 1 
        if r == 2 : 
            break 
    if(r != 2) :
        i -= 2
    print("Character Count:",i) 
    character = i
    line = (line.split(None, 1)[0])
    return character,line

def phrase() : 
    k = 0
    with open(os.path.join(sys.path[0], "phrase.txt"), "r") as f: #phrase.txt file must be in the same folder as this .py file
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
    print()
    print(line)
    k = 0
    i = 0
    r = 0
    for k in line : #counts the spaces between words and prints by adding 1 to that
        if k == "\"" : #word counter will be false if quotation format is not followed
            r += 1 #format is: "I am alive."
        if k == " " : #dont use unnecessary spaces after or before ( " ) mark
            i += 1 #anything outside of ("") marks will be ignored
        if r == 2 : #use exactly 2 quotation marks
            break #this is a code that can easily be broken without even touching the code
    print("Word Count:",i+1)
    word = i+1
    k = 0
    i = 0
    r = 0
    for k in line : #counts how many characters are used for the quotation
        if k == "\"" : #character counter will be false if quotation format is not followed
            r += 1 #format is: "I am alive."
        i += 1 #dont use unnecessary characters after or before ( " ) mark
        if r == 2 : #anything outside of ("") marks will be ignored
            break #use exactly 2 quotation marks
    print("Character Count:",i) #this is a code that can easily be broken without even touching the code
    character = i
    rr = [word,character]
    return rr