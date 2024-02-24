import classes
#import save

def main(value):
    global player_classes
    player_classes = classes.get_player_classes()
    global player_spec
    player_spec = dict()
    if value:
        pass
    else:
        choose()
        #player_class =  dict()

        #player_class = player_classes[player_class_choice]
        player_spec = player_classes[player_class_choice]


def choose():
    print("Available Classes:")

    print(player_classes)

    print()
    global player_class_choice
    player_class_choice = input("Choose Your Class: ")

    while player_class_choice not in player_classes.keys():
        print("Invalid Class.")
        player_class_choice = input("New Input: ")

def get_player_spec():
    return player_spec