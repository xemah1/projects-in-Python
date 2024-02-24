def main():
    global entities
    entities = {
        "zombie": {
            "health": 100 ,
            "damage": 52 ,
            "armor": 5 ,
            "boss": False
        } ,
        "goblin": {
            "health": 105 ,
            "damage": 27 ,
            "armor": 22 ,
            "boss": False
        } ,
        "vampire": {
            "health": 350 ,
            "damage": 52 ,
            "armor": 50 ,
            "boss": True
        }
    }

def length():
    return len(entities)

def create(selection):
    copy = list(entities.items())[selection]
    return copy

def reset():
    main()