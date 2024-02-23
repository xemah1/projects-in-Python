import player
import dungeon
import altar
#import save

def heal_formula():
    if player.get_player_spec()["health"] >= default_player_hp*0.8:
        return default_player_hp
    else:
        return ((default_player_hp - player.get_player_spec()["health"]) // 2) + player.get_player_spec()["health"]

game = True
player.main()
default_player_hp = player.get_player_spec()["health"]
while game:
    print(player.get_player_spec())
    print("1. Enter Dungeon | 2. Enter Altar | 3. Exit Game")
    choice = input()
    while choice != "1" and choice != "2" and choice != "3":
        print("Invalid Choice.")
        choice = input("New Input: ")
    if choice == "1":
        game = dungeon.start()
        if game:
            print("After hard fought battle you rest to heal your wounds.")
            player.get_player_spec()["health"] = heal_formula()
    if choice == "2":
        altar_result = altar.main(player.get_player_spec())
        player.get_player_spec()["health"] = altar_result["health"]
    if choice == "3":
        break
print(player.get_player_spec())
#print(save.get_saveslot())
