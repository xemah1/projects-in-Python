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
                if player_spec["health"] < 150:
                    player_spec["health"] += int(souls * 0.03 * player_spec["health"])
                elif player_spec["health"] < 500:
                    player_spec["health"] += int(souls * 0.01 * player_spec["health"])
                else:
                    player_spec["health"] += int(souls * 0.001 * player_spec["health"])

                player_spec["level"] += souls
                print("You feel the sudden rush of blood in your veins.\n")
            else:
                player_spec["souls"] -= souls
                player_spec["damage"] += souls * 3
                player_spec["level"] += souls
                print("You feel more power in your muscles.\n")
    return player_spec