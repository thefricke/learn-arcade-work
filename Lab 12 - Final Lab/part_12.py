import random
import time


class Player:
    def normal_atk(self):
        attack = random.randint(0, 20)
        return attack

    def spec_attack(self):
        spec_atk = random.randint(30, 45)
        return spec_atk

    def heal(self):
        healing = random.randint(6, 24)
        return healing


def first_go():
    go = random.randint(0, 2)
    if go == 0:
        return 'Comp'
    else:
        return name


player_hp = 100
player_energy = 100
comp_hp = 100
comp_energy = 0

ready = input("Ready to play? Type Y/N: ")
name = input("What is your name: ")
turn = first_go()

player = Player()
comp = Player()

while player_hp > 0 and comp_hp > 0:
    print(f"\n{turn}'s turn")
    if turn != 'Comp':
        action = int(input(f"{name}, please choose an action:\n1) Normal Attack\n2) Special Attack\n3) Heal\n"))
        if action == 1:
            player_normal_attack = player.normal_atk()
            comp_hp = comp_hp - player_normal_attack
            player_energy += 10
            time.sleep(3)
            print(f"\n{name} just did {player_normal_attack} damage!")
            print(f"{name} now has {player_hp} health and {player_energy} energy")
            time.sleep(3)
            print(f"The computer now has {comp_hp} health and {comp_energy} energy")
            turn = 'Comp'
        elif action == 2 and player_energy >= 20:
            player_special_attack = player.spec_attack()
            comp_hp = comp_hp - player_special_attack
            player_energy -= 20
            time.sleep(3)
            print(f"\n{name} just did {player_special_attack} damage!")
            print(f"{name} now has {player_hp} health and {player_energy} energy")
            time.sleep(3)
            print(f"The computer now has {comp_hp} health and {comp_energy} energy")
            turn = 'Comp'
        elif action == 3 and player_energy >= 15:
            player_heal = player.heal()
            player_hp += player_heal
            player_energy -= 15
            time.sleep(3)
            print(f"\n{name} just healed themselves for {player_heal}")
            print(f"{name} now has {player_hp} health and {player_energy} energy")
            turn = 'Comp'
        elif action == 2 or action == 3 and player_energy < 15:
            print(f"\n{name} you have {player_hp} health and {player_energy} energy")
            print(f"\n{name} you do not have enough energy, choose 1) Normal Attack please")
        else:
            print("Please enter a valid action")
    else:
        if comp_energy >= 20:
            comp_spec_attack = comp.spec_attack()
            player_hp = player_hp - comp_spec_attack
            comp_energy -= 20
            time.sleep(3)
            print(f"\nThe computer did {comp_spec_attack} damage")
            print(f"{name} now has {player_hp} health and {player_energy} energy")
            time.sleep(3)
            print(f"The computer now has {comp_hp} health and {comp_energy} energy")
            turn = name
        elif comp_hp < 50 and comp_energy > 15:
            comp_healing = comp.heal()
            comp_hp += comp_healing
            comp_energy -= 15
            time.sleep(3)
            print(f"\nThe computer had healed itself for {comp_healing} health")
            print(f"{name} now has {player_hp} health and {player_energy} energy")
            time.sleep(3)
            print(f"The computer now has {comp_hp} health and {comp_energy} energy")
            turn = name
        else:
            comp_normal_attack = comp.normal_atk()
            player_hp = player_hp - comp_normal_attack
            comp_energy += 10
            time.sleep(3)
            print(f"\n The computer dealt {comp_normal_attack} points of damage")
            print(f"{name} now has {player_hp} health and {player_energy} energy")
            time.sleep(3)
            print(f"The computer now has {comp_hp} health and {comp_energy} energy")
            turn = name
    if player_hp <= 0:
        print("The computer has beaten you.")
    elif comp_hp <= 0:
        print(f"\n{name} has beaten the computer.")
