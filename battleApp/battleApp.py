#!/usr/bin/python3
import random
from characters import Soldier, Creature


def main():
    #print header
    #initialize actors and map
    creatures = [
            Creature('Toad', 1),
            Creature("Warrior", 75),
            Creature("Tiger", 10),
            Creature("Dragon", 100)
    ]

    print(creatures)

    hero = Soldier('You', 78)
    #game loop
    game_loop(hero, creatures)

def game_loop(hero, creatures):
    '''Main game loop'''

    while True:
        active_creature = random.choice(creatures) 
        print("{} of health {} appears!".format(active_creature.name, active_creature.health))
        cmd = input("What would you like to do? [A]ttack, [R]unaway, [L]ookaround: ")
        cmd = cmd.upper()

        if(cmd == 'A'):
            print("Attacking!")
            hero.attack(active_creature)
        elif(cmd == 'R'):
            print("Running away...")
        elif(cmd == 'L'):
            print("Looking around")
        else:
            confirmation = input("E[X]it the game? Any other key to continue: ")
            if confirmation.upper() == 'X':
                break



if __name__ == "__main__":
    main()
