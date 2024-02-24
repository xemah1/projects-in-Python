import creatures
import player
from random import randint

def main() :
    default_player_hp = player.get_player_spec()["health"]
    threat_level = 15
    if player.get_player_spec()["level"] + player.get_player_spec()["souls"] >= threat_level:
        print("Boss creatures might appear.")
    game = start(threat_level)
    if game:
        print("\nAfter hard fought battle you rest to heal your wounds.")
        player.get_player_spec()["health"] = heal_formula(default_player_hp)
    return game


def start(threat_level) :
    print("You entered the dungeon.")
    creatures.main()
    global enemy
    enemy = creatures.create(randint(0,creatures.length()-1))
    while player.get_player_spec()["level"] + player.get_player_spec()["souls"] < threat_level and enemy[1]["boss"]:
        enemy = creatures.create(0)
        enemy[1]["boss"] = False
        enemy = creatures.create(randint(0,creatures.length()-1))

    souls_to_earn = enemy[1]["health"]//50 + enemy[1]["armor"]//5
    souls_to_life = 10

    print("A/An",enemy[0],"appeared in front of you.")
    while enemy[1]["health"] > 0:
        if player.get_player_spec()["health"] <= 0:
            if player.get_player_spec()["souls"] >= souls_to_life:
                player.get_player_spec()["health"] = 1
                player.get_player_spec()["souls"] -= souls_to_life
                print("Sacrificed",souls_to_life,"souls.")
                print(player.get_player_spec())
            else:
                break

        player_action()
        if enemy[1]["health"] <= 0:
            break
        enemy_action()


        print()
    creatures.reset()
    if player.get_player_spec()["health"] <= 0:
        print("YOU ARE DEAD.")
        return False
    else:
        player.get_player_spec()["souls"] += souls_to_earn
        return True


def player_action():
    print()
    print("YOUR TURN")
    if randint(1,100) <= player.get_player_spec()["critical_chance"]:
        print("CRITICAL HIT")
        player_damage = int(player.get_player_spec()["damage"]*(randint(165,210)/100))
    else:
        player_damage = int(player.get_player_spec()["damage"]*(randint(65,110)/100))
    final_damage = int(player_damage-enemy[1]["armor"])
    if final_damage < 0:
        final_damage = 0
    print("Your Damage:",player_damage,"Enemy Armor:",enemy[1]["armor"],"Final Damage:",final_damage)
    enemy[1]["health"] -= final_damage
    print(enemy)


def enemy_action():
    print()
    print("ENEMY'S TURN")
    enemy_damage = int(enemy[1]["damage"]*(randint(65,110)/100))
    final_damage = int(enemy_damage-player.get_player_spec()["armor"])
    if final_damage < 0:
        final_damage = 0
    print("Enemy Damage:",enemy_damage,"Your Armor:",player.get_player_spec()["armor"],"Final Damage:",final_damage)
    player.get_player_spec()["health"] -= final_damage
    print(player.get_player_spec())


def heal_formula(default_player_hp):
    if player.get_player_spec()["health"] >= default_player_hp*0.8:
        return int(default_player_hp)
    else:
        return int(((default_player_hp - player.get_player_spec()["health"]) // 2) + player.get_player_spec()["health"])