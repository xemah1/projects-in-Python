import player

def main():
    global saveslot
    saveslot = {
        "in_dungeon": False ,
        "player": player.get_player_spec()
    }

def get_saveslot():
    return saveslot