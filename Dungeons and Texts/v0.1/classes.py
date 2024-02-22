class main():
    global player_classes
    player_classes = {
        "default": {
            "health": 100 ,
            "damage": 25 ,
            "armor": 0
        } ,
        "glasscannon": {
            "health": 25 ,
            "damage": 100 ,
            "armor": 0
        }
    }

def get_player_classes():
    return player_classes