#!/usr/bin/python3
def header(character, lengthOfLines, appName):
    header = character*lengthOfLines + "\n" +  appName + "\n" + character*lengthOfLines
    return header 

def helloWorldApp():
    print(header("-", 10, "HelloWorldApp"))
    name = input("What is your name? ")
    greeting = "Hello, " + name
    print(greeting)



if __name__ == "__main__":
    helloWorldApp()
