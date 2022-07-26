import words
import random

print("╔════════════════════════════════════════════════════════════════╗")
print("║When feedback is asked please answer according to the following.║")
print("║\"g\" for green, \"y\" for yellow, \"m\" for miss.\t\t\t ║")
print("╚════════════════════════════════════════════════════════════════╝")
counter = 0 # counts rounds
zabun = 0 # counts words
kraken = 0 # counts yellows
greenFalseSafe = 0 # counts stuff so wrong things dont happen
choice = ""
feedback = ""
recommendation = ["0","0"]
greenList = ["0","0","0","0","0"]
yellowList = []
blackList = []
wordList = words.wordList()
wordList.sort()


while counter < 5 :
    counter += 1
    zabun = 0
    greenFalseSafe = 0
    if (counter == 1) :
        choice = input(str(counter) + "st word you wrote: ")
    elif (counter == 2) :
        choice = input(str(counter) + "nd word you wrote: ")
    elif (counter == 3) :
        choice = input(str(counter) + "rd word you wrote: ")
    elif (counter == 4 or counter == 5) :
        choice = input(str(counter) + "th word you wrote: ")
    while (len(choice) != 5) :
        choice = input("Word length is not supported. Try writing the word again: ")
    choice = choice.lower()

    feedback = input("Wordle's feedback was: ")
    for k in range(len(choice)) :
        if (feedback.split(None, 4)[k] == "g") :
            greenList[k] = choice[k]
            yellowList.append(choice[k])
            yellowList = list(dict.fromkeys(yellowList))

        elif (feedback.split(None, 4)[k] == "y") :
            yellowList.append(choice[k])

        else :
            blackList.append(choice[k])

    # determines what to do with some complicate "green" or "yellow" scenarios.
    for k in range(len(wordList)) :
        word = wordList[k]
        for i in range(len(greenList)) :
            for r in range(len(word)) :
                if (word[r] == greenList[i] and i != r and len(word) > 3) :
                    for j in range(len(blackList)) :
                        if(greenList[i] == blackList[j]) :
                            wordList[k] = "0"
        for i in range(len(yellowList)) :
            if (feedback.split(None, 4)[i] == "y") :
                if (len(word) == 5) :
                    if (word[i] == choice[i]) :
                        wordList[k] = "0"

    blackList = list(set(blackList) - set(greenList))
    blackList = list(set(blackList) - set(yellowList))

    #main for loop to process wordle's feedback
    for k in range(len(wordList)) :
        kraken = 0
        if (wordList[k] == "0") :
            continue
        else :
            word = wordList[k]

            # processes information about green tiles
            for i in range(len(choice)) :
                if (greenList[i] != "0") :
                    if (word[i] != greenList[i]) :
                        wordList[k] = "0"

            # processes information about yellow tiles
            if (len(yellowList) != 0) :
                for i in range(len(choice)) :
                    for j in range(len(yellowList)) :
                        if (word[i] == yellowList[j]) :
                            kraken += 1
                if (kraken < len(yellowList)) :
                    wordList[k] = "0"

            # processes information about black/gray/miss tiles
            for i in range(len(choice)) :
                for j in range(len(blackList)) :
                    if (len(word) == 5) :
                        if (word[i] == blackList[j]) :
                            wordList[k] = "0"
        if (wordList[k] != "0") :
            zabun += 1
    if (zabun <= 100) :
        if (zabun == 1) :
            for k in wordList :
                if (k != "0") :
                    print()
                    print("╔═════════╗")
                    print("║  " + k.upper() + "  ║<<<════════")
                    print("╚═════════╝")
            counter = 5
        elif (zabun == 0) :
            print("║ ", end= " ║")

        else :
            print("╔══════════════════╗")
            print("║ Possible Answers ║")
            print("╚══════════════════╝")
            print("║ ",end="")
        for k in wordList :
            if (k != "0" and zabun != 1) :
                print(k.upper(), end= " ║ ")
        print()

    # produces recommendations from available words
    else :
        recommendation[0] = wordList[random.randint(0,len(wordList) - 1)]
        recommendation[1] = wordList[random.randint(0,len(wordList) - 1)]
        while recommendation[0] == "0" or recommendation[0] == recommendation[1]:
            recommendation[0] = wordList[random.randint(0,len(wordList) - 1)]
        while recommendation[1] == "0" :
            recommendation[1] = wordList[random.randint(0,len(wordList) - 1)]
        print("There are still " + str(zabun) + " possible answers. Recommendation: " + recommendation[0] + " , " + recommendation[1])
    print()
    print("Greenlist: ",end="")
    print(greenList)
    print("Yellowlist: ",end="")
    print(yellowList)
    print("Blacklist: ",end="")
    print(blackList)
    print("══════════════════════════════════════════════════════════════════")