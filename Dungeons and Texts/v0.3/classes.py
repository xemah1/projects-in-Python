class main():
    global player_classes
    player_classes = {
        "default": {
            "health": 100 ,
            "damage": 45 ,
            "critical_chance": 25 ,
            "armor": 0 ,
            "level": 0 ,
            "souls": 0
        } ,
        "glasscannon": {
            "health": 40 ,
            "damage": 100 ,
            "critical_chance": 75 ,
            "armor": 0 ,
            "level": 0 ,
            "souls": 0
        }
    }

def get_player_classes():
    return player_classes