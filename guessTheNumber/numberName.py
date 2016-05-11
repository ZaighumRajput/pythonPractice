#!/usr/bin/python3
def header(character, lengthOfLines, appName):
    header = character*lengthOfLines + "\n\t" +  appName + "\n" + character*lengthOfLines
    return header 

def GuessTheNumberApp():
    print(header("-", 30, "GUESS THE NUMBER!"))

    from random import seed, randint
    seed(88)
    secretNumber = randint(0,100)
    userGuess = -1
    while(secretNumber != userGuess):
        userGuess = int(input("Guess a number between 0 and 100: "))
        if (userGuess > secretNumber):
            print("Guess is too high")
        elif (userGuess < secretNumber):
            print("Guess is too low")
    print("You got it right!")



if __name__ == "__main__":
    GuessTheNumberApp()
