import classes

def main():
    global player_spec
    player_spec = dict()
    player_class =  dict()
    player_classes = classes.get_player_classes()
    print("Available Classes:")

    print(player_classes)

    print()
    player_class_choice = input("Choose Your Class: ")

    while player_class_choice not in player_classes.keys():
        print("Invalid Class.")
        player_class_choice = input("New Input: ")

    player_class = player_classes[player_class_choice]
    player_spec = player_classes[player_class_choice]
    print(player_class)

def get_player_spec():
    return player_spec