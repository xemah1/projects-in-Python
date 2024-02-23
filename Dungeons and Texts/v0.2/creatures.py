def main():
    global entities
    entities = {
        "placeholder": {
            "health": 100 ,
            "damage": 25 ,
            "armor": 0
        } ,
        "zombie": {
            "health": 100 ,
            "damage": 52 ,
            "armor": 5
        } ,
        "goblin": {
            "health": 105 ,
            "damage": 27 ,
            "armor": 35
        } ,
        "vampire": {
            "health": 350 ,
            "damage": 52 ,
            "armor": 50
        }
    }

def length():
    return len(entities)

def create(selection):
    copy = list(entities.items())[selection]
    return copy

def reset():
    main()