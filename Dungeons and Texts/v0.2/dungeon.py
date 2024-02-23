import creatures
import player
from random import randint

def start() :
    print("You entered the dungeon.")
    creatures.main()
    enemy = creatures.create(randint(1,creatures.length()-1))
    souls_to_earn = enemy[1]["health"]//50
    print("A/An",enemy[0],"appeared in front of you.")
    while enemy[1]["health"] > 0:
        if player.get_player_spec()["health"] <= 0:
            if player.get_player_spec()["souls"] >= 5:
                player.get_player_spec()["health"] = 1
                player.get_player_spec()["souls"] -= 5
                print("Sacrificed 5 souls.")
                print(player.get_player_spec())
            else:
                break
        print()
        print("YOUR TURN")
        player_damage = player.get_player_spec()["damage"]*(randint(65,110)/100)
        final_damage = player_damage-enemy[1]["armor"]
        if final_damage < 0:
            final_damage = 0
        print("Your Damage:",player_damage,"Enemy Armor:",enemy[1]["armor"],"Final Damage:",final_damage)
        enemy[1]["health"] -= final_damage
        print(enemy)
        if enemy[1]["health"] <= 0:
            break
        
        print()
        print("ENEMY'S TURN")
        enemy_damage = enemy[1]["damage"]*(randint(65,110)/100)
        final_damage = enemy_damage-player.get_player_spec()["armor"]
        if final_damage < 0:
            final_damage = 0
        print("Enemy Damage:",enemy_damage,"Your Armor:",player.get_player_spec()["armor"],"Final Damage:",final_damage)
        player.get_player_spec()["health"] -= final_damage
        print(player.get_player_spec())

        print()
    creatures.reset()
    if player.get_player_spec()["health"] <= 0:
        print("YOU ARE DEAD.")
        return False
    else:
        player.get_player_spec()["souls"] += souls_to_earn
        return True