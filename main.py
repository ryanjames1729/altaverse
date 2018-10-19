import time, sys, os
from planet_beta98 import *

class Player:
    def __init__(self):
        self.name = ""
        self.fuel = 100
        self.health = 100
        self.currentObjects = []
        self.money = 500.00


player = Player()

def slowText(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.06)


def travel(player, currentPlanet, direction):
    if currentPlanet == "beta98":
        if destinationPlanet == "north":
            #slowText("\nAfter your trip you will have {}% fuel left.".format(player.fuel))
            beta98_landed()
    slowText("\n\nTravel is not working at this time.")
    beta98_landed(player)

def beginGame():
    slowText("\n\n\nWelcome to the Altaverse, a newly discovered planetary system that has a man-made planet that is within traveling distance to the surrounding unchartered 8 planets.")
    slowText("\nEnter your name for game play. ")
    player.name = input(">")
    slowText("\n\n{}, let's get started. You will start on the man-made planet named Beta-98.".format(player.name))
    beta98_landed(player)

def endGame():
    slowText("\n\nWe are so sorry to see you go. We would love if you come and play our game again.\n")
    rollCredits()
    pass

def rollCredits():
    print("This was made by Ryan James, 2018")

def getHealth(player):
    slowText("\nYour health is currently at {}%.".format(player.health))

def getFuel(player):
    slowText("\nYour fuel is currently at {}%.".format(player.fuel))

def getMoney(player):
    slowText("\nYour money is currently at ${}.".format(player.money))

def getObjects(player):
    slowText("\nYour currently have {} objects.".format(player.currentObjects))

def otherWords(player, choice):
    if choice.find("health") > -1:
        getHealth(player)
        return True
    elif choice.find("fuel") > -1:
        getFuel(player)
        return True
    elif choice.find("money") > -1:
        getMoney(player)
        return True
    elif choice.find("objects") > -1:
        getObjects(player)
        return True
    return False




# Start the game
if __name__ == "__main__":
    os.system('cls')
    beginGame()
