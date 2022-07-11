import random
import time

print("\nHi. :)")

playerCount = int(input(("How many friends would you like to have? :) ")))
while playerCount > 5 :
    print("\nI can't let you have that many friends. You will forget about me. More than 5 is unnecessary don't you think? ")
    playerCount = int(input(("Let's do this again. How many friends would you like to have? :) ")))
print("A really good choice there!")
playerName = input("My best friend. Your name was? ")
i = 0
specialOffer = 0
moneyList = []
healthList = []
for i in range(playerCount):
    moneyList.append(random.randint(5,20))
    if random.randint(1,3) == 1:
        healthList.append(random.randint(65,100))
        print("Your friend player",i+2,"has some sort of injury. What a cruel world it is.")
    else: healthList.append(100)

print("It's pretty reasonable to assume you have 100 health. Does your character have any injuries that i am not awared of? ")
print("Answer \"yes\" or \"no\" please.")

injuryAnswer = input()
while injuryAnswer != "yes" and injuryAnswer != "no" :
    print("Answer \"yes\" or \"no\" please.")
    injuryAnswer = input()

if  injuryAnswer == "yes" :
    print("Randomizing your health between 65 and 100.")
    playerHealth = random.randint(65,100)
    if playerHealth < 100:
        print("Your health has been lowered to",playerHealth,"\n")

if injuryAnswer == "no" :
    playerHealth = 100
    print("Very healthy you are my beloved friend.\n")
print("\"I wouldn't bring my coins down to 0 if i were you friend.\"")
print("This is the first round of our happy game! You see two dice in front of you.")
aliveCounter = 0
roundCounter = 0
playerMoney = random.randint(5,20)

while roundCounter >= 0 and aliveCounter != 1:
    roundCounter += 1
    if playerHealth > 0 :
        print("You have",playerMoney,"coins in your purse.")
        choice = input("Are you going to \"roll\" or \"pass\"? ")
        while choice != "roll" and choice != "pass" :
            print("Please answer as mentioned.")
            choice = input("Are you going to \"roll\" or \"pass\"? ")
        time.sleep(0.3)
        print("We want our roll to be between 5 and 8.(5 and 8 included)")
        time.sleep(0.3)
        if choice == "roll" :
            wager = int(input("What is your wager my friend? "))
            while wager < 0 or wager > playerMoney :
                print("Insufficient balance.")
                wager = int(input("What is your wager my friend? "))
            randomDice1 = random.randint(1,6)
            randomDice2 = random.randint(1,6)
            time.sleep(0.3)
            if randomDice1 + randomDice2 < 5 or randomDice1 + randomDice2 > 8 :
                print("You rolled",randomDice1,"and",randomDice2,)
                playerMoney -= wager
                print("!You lost your wager.\nYou have",playerMoney,"coins left in your purse.")
            else : 
                print("You rolled",randomDice1,"and",randomDice2,)
                playerMoney += wager
                print("!!You won your wager.\nYou now have",playerMoney,"coins in your purse.")

        if choice == "pass" :
            print("You may regret that.")
    i = 0
    for i in range(playerCount):
        if healthList[i] > 0 and moneyList[i] > 0:
            time.sleep(0.45)
            print("\nPlayer",i+2,"is starting their turn.")
            time.sleep(0.4)
            randomNum = random.randint(1,3)
            if randomNum == 1 :
                print("Player",i+2,"chose to pass.")
            else :
                wager = random.randint(1,moneyList[i])
                randomDice1 = random.randint(1,6)
                randomDice2 = random.randint(1,6)
                if randomDice1 + randomDice2 < 5 or randomDice1 + randomDice2 > 8 :
                    moneyList[i] -= wager
                    print("Player",i+2,"lost their wager and now has",moneyList[i],"coins in their purse.")
                else :
                    moneyList[i] += wager
                    print("Player",i+2,"won their wager and now has",moneyList[i],"coins in their purse.")
    print("\nEvery player used their turn for round",roundCounter,)
    time.sleep(0.1)
    if roundCounter % 5 == 0 :
        print("Five rounds have passed. The shop has openned.")
        time.sleep(0.2)
        sellingWhat = random.randint(1,3)
        if specialOffer == 0 and playerHealth != 0:
            specialOffer += 1
            print("You see a knife is on sale. You can't see a price tag. Your lovely friend from the beginning returned and has an offer for you.")
            print("\"I have a discount for you my friend. I will sell you this knife for only 100 coins. And don't forget i came to you first so you can have it.\"")
            answer = input("Are you going to buy the knife? \"yes\"/\"no\": ")
            if answer == "yes" :
                if playerMoney < 100 :
                    print("I don't think you have that kind of money. Why would you need a knife in the first place?")
        else :
            i = random.randint(1,3)
            if i == 1 :
                print("You see a knife on the stand.")
                weaponPrice = random.randint(30,55)
                weapon = "knife"
                weaponPhrase = "stabbed"
                weaponDamage = random.randint(30,55)
            if i == 2 :
                print("You see a gun and one bullet on the stand.")
                weaponPrice = random.randint(50,65)
                weapon = "gun"
                weaponPhrase = "shot"
                weaponDamage = random.randint(70,85)
            if i == 3 :
                print("You see a grenade on the stand.")
                weaponPrice = random.randint(70,75)
                weapon = "grenade"
                weaponPhrase = "threw the grenade at"
                weaponDamage = random.randint(100,125)
            i = random.randint(1,playerCount + 1)
            healthList.append(playerHealth)
            while healthList[i - 1] <= 0 :
                i = random.randint(1,playerCount + 1)
            del healthList[-1]
            if i != 1 :
                print("This shop offers it's product to player",i,)
                if random.randint(1,3) > 1 :
                    if moneyList[i - 2] > weaponPrice :
                        print("Player",i,"decided to buy the",weapon)
                        moneyList[i - 2] -= weaponPrice
                        k = 100
                        j = 0
                        if random.randint(1,2) == 1 :
                            for j in range(playerCount) :
                              if healthList[j] < k and healthList[j] != 0 :
                                  k = healthList[j]
                                  randomTemp = j
                            if playerHealth < k and random.randint(1,2) == 1:
                                print("player",i,weaponPhrase,"you!")
                                playerHealth -= weaponDamage
                                if playerHealth <= 0 :
                                    print("Your eyes turn black. You can't see. You died to a painful death.")
                                else :
                                    print("You took",weaponDamage,"damage. You now have",playerHealth,"health left.")
                            else :
                                print("player",i,weaponPhrase,"player",randomTemp + 2,)
                                healthList[randomTemp] -= weaponDamage
                                if healthList[randomTemp] > 0 : 
                                    print("Looks like player",randomTemp + 2,"will live to see another day.")
                                else :
                                    print("Player",randomTemp + 2,"collapsed to the ground.")
                        else :
                            randomTemp = random.randint(1,6)
                            if randomTemp == 1 :
                                print("player",i,weaponPhrase,"you!")
                                playerHealth -= weaponDamage
                                if playerHealth <= 0 :
                                    print("Your eyes turn black. You can't see. You died to a painful death.")
                                else :
                                    print("You took",weaponDamage,"damage. You now have",playerHealth,"health left.")
                            else :
                                print("player",i,weaponPhrase,"player",randomTemp,)
                                healthList[randomTemp - 2] -= weaponDamage
                                if healthList[randomTemp - 2] > 0 : 
                                    print("Looks like player",randomTemp,"will live to see another day.")
                                else :
                                    print("Player",randomTemp,"collapsed to the ground.")
                else : 
                    print("Player",i,"didn't buy the",weapon,".")
            else :
                print("Shop offered it's product to you. Price is",weaponPrice,)
                if playerMoney > weaponPrice :
                    print("You have",playerMoney,"coins in your purse. Are you going to buy the",weapon,"? yes/no ")
                    choice = input()
                    while choice != "yes" and choice != "no" :
                        choice = input("Answer \"yes\" or \"no\" please. ")
                    if choice == "yes" :
                        print("Who will it be? Available options are: ")
                        i = 0
                        for i in range(playerCount) :
                            if healthList[i] > 0 :
                                print("player",i+2,)
                        choice = input("Type in the number only. ")
                        healthList[choice - 2] -= weaponDamage
                        if healthList[choice - 2] > 0 :
                            print("Look like player",choice,"will live to see another day.")
                        else : 
                            print("Player",choice,"collapsed to the ground.")
        print("The shop disappeared like nothing happened.")
        time.sleep(0.5)
    aliveCounter = 0
    shotDown = 0
    for i in range(playerCount) :
        if healthList[i] != 0 and moneyList[i] == 0 :
            print("You see some people dragging player",i + 2,"somewhere outside.")
            healthList[i] = 0
            shotDown += 1
    if shotDown > 0 :
        time.sleep(1)
        print("You hear gunshots from outside.")
    if playerMoney == 0 and playerHealth != 0:
        time.sleep(1)
        print("You were warned about having 0 coins. \"How are you going to keep playing without coins?\" You are being dragged out.")
        time.sleep(1)
        print("\nYou are shot dead.")
        time.sleep(5)
        playerHealth = 0
    print("\nThe round has concluded. Let's see who is alive.")
    time.sleep(0.1)
    if playerHealth > 0 :
        print(playerName)
        aliveCounter += 1
    i = 0
    for i in range(playerCount) :
        if healthList[i] > 0 :
            print("player",i + 2,)
            aliveCounter += 1
            time.sleep(0.1)
    if aliveCounter == 1 :
        print("WE HAVE A WINNER!")
        if playerHealth > 0 :
            print("YOU HAVE WON THE BATTLE OF FRIENDSHIP!")
        else :
            i = 0
            for i in range(playerCount) :
                if healthList[i] > 0 :
                    print("PLAYER",i+2,"HAVE WON THE BATTLE OF FRIENDSHIP!")
                    print("Did your friends even have a name?")
    if aliveCounter != 1 :
        time.sleep(0.5)
        print("\nMoving on to the next round.\n\n")