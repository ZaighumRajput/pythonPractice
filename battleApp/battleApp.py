#!/usr/bin/python3

def main():
    #print header
    #initialize actors and map

    #game loop
    game_loop()

def game_loop():
    '''Main game loop'''
    while True:
        cmd = input("What would you like to do? [A]ttack, [R]unaway, [L]ookaround: ")
        cmd = cmd.upper()

        if(cmd == 'A'):
            print("Attacking!")
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
