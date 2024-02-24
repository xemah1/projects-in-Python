import player
import dungeon
import altar
import save

def main():
    game = True
    if save.save_exists():
        print("Loading from save file.")
        player.main(True)
        save.load_save()
    else :
        player.main(False)
    while game:
        print(player.get_player_spec())
        print("1. Enter Dungeon | 2. Enter Altar | 3. Exit Game")
        choice = input()
        while choice != "1" and choice != "2" and choice != "3":
            print("Invalid Choice.")
            choice = input("New Input: ")
        if choice == "1":
            game = dungeon.main()
            if game:
                save.create_save()
            else:
                if save.save_exists():
                    save.remove_save()
        if choice == "2":
            altar_result = altar.main(player.get_player_spec())
            player.get_player_spec()["health"] = altar_result["health"]
            save.create_save()
        if choice == "3":
            break
    print(player.get_player_spec())


main()