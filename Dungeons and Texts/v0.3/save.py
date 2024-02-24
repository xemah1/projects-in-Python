import player
import os
import sys

def create_save():
    with open(os.path.join(sys.path[0], "savefile.txt"), "w") as f:
        save = player.get_player_spec()
        for line in save:
            f.write(line + " " + str(save[line]) + "\n")
    return player.get_player_spec()

def load_save():
    save = dict()
    with open(os.path.join(sys.path[0], "savefile.txt"), "r") as f:
        for line in f:
            save[line.split(None, 2)[0]] = int(line.split(None, 2)[1])

    for line in save:
        player.get_player_spec()[line] = save[line]

def remove_save():
    os.remove("savefile.txt")

def save_exists():
    return os.path.exists('./savefile.txt')