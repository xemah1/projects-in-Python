from random import randint

def main(player_spec):
    print("You have",player_spec["souls"],"souls. Sacrifice them to level up.")
    print("1. Accept | 2. Refuse")
    choice = input()
    while choice != "1" and choice != "2":
        print("Invalid Choice.")
        choice = input("New Input: ")
    if choice == "1":
        souls = player_spec["souls"]
        if souls == 0:
            print("Nothing happened.")
        else:
            if randint(0,1):
                player_spec["souls"] -= souls
                player_spec["health"] += souls
                player_spec["level"] += souls
                print("You feel the sudden rush of blood in your veins.\n")
            else:
                player_spec["souls"] -= souls
                player_spec["damage"] += souls
                player_spec["level"] += souls
                print("You feel more power in your muscles.\n")
    return player_spec