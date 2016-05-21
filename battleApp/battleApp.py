#!/usr/bin/python3
import random
from characters import Soldier, Creature, Dragon, HealthBoost, StrengthBoost


def main():
    #print header
    #initialize actors and map

    #game loop
    game_loop()

def game_loop():
    '''Main game loop'''
    AllCreatures = [
            Creature('Toad', 1, 5),
            Creature("Warrior", 75, 100),
            Creature("Tiger", 10, 200),
            Dragon("Dragon", 100,200, 20, False),
            Dragon("Dragon", 100,200, 40, True)
    ]

    AllPowerups = [
            HealthBoost("Health", 500),
            StrengthBoost("Milk", 10),
            StrengthBoost("Steroids", 100),
            StrengthBoost("HGH", 1000),
            HealthBoost("Dinner", 1000)
    ]

    hero = Soldier('You', 1000, 150)

    while True:
        active_creature = random.choice(AllCreatures) 
        print("{} of health {} appears!".format(active_creature.name, active_creature.health))
        cmd = input("What would you like to do? [A]ttack, [R]unaway, [L]ookaround: ")
        cmd = cmd.upper()

        if(cmd == 'A'):
            attack_sequence(hero, active_creature, AllCreatures)
            if(hero.health <  0): break
        elif(cmd == 'R'):
            running_sequence(hero, AllPowerups)
        elif(cmd == 'L'):
            looking_sequence(AllCreatures)
        else:
            confirmation = input("E[X]it the game? Any other key to continue: ")
            if confirmation.upper() == 'X':
                break

def powerdrop(hero, AllPowerups):

    if(AllPowerups):
        print("dropping powerup")
        random.shuffle(AllPowerups)
        hero.use_powerup(AllPowerups.pop())
    else:
        return None

def running_sequence(hero, AllPowerups):
    powerdrop(hero, AllPowerups)
    print("You ran away")






def looking_sequence(AllCreatures):
    print("Looking around...")
    for c in AllCreatures:
        print("* {} with {} health".format(c.name, c.health))

def attack_sequence(hero, creature, AllCreatures):
    while hero.health > 0:
        print("You attacked {}".format(creature.name))
        hero.attack(creature)
        if(creature.health < 0):
            print("You defeated {}".format(creature.name))
            AllCreatures.remove(creature)
            return None
        elif(hero.health > 0):
            print("Your health is at {}. {} is at {}".format(hero.health, creature.name, creature.health))
            cmd = input("Attack again? [Y]")
            if cmd.upper() == 'Y':
                continue
            else:
                print("You fled the battle scene")
                return None
    print("You died!..")

if __name__ == "__main__":
    main()
