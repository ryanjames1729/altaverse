import time, sys, os
from planet_beta98 import *
from planet_example import *
import planet_beta98
import planet_example


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
    distanceTraveled = 0
    if currentPlanet == "beta98":
        if direction == "north":
            repeat = True
            while repeat:
                repeat = False
                distanceTraveled += 10
                player.fuel -= 10
                if player.fuel <= 0:
                    slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                    endGame()
                slowText("\nYou have used 10% of your fuel but have not found a planet. Would you like to keep traveling North or turn around? ")
                choice = input(">").strip().lower()
                if choice.find("turn") > -1 or choice.find("around") > -1 or choice.find("back") > -1:
                    slowText("\nTurning around to travel back home.")
                    while distanceTraveled > 0:
                        distanceTraveled -= 10
                        player.fuel -= 10
                        if player.fuel <= 0:
                            slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                            endGame()
                    planet_beta98.beta98_landed(player)
                else:
                    repeat = True
        elif direction == "south":
            repeat = True
            while repeat:
                repeat = False
                distanceTraveled += 10
                player.fuel -= 10
                if player.fuel <= 0:
                    slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                    endGame()
                slowText("\nYou have used 10% of your fuel but have not found a planet. Would you like to keep traveling South or turn around? ")
                choice = input(">").strip().lower()
                if choice.find("turn") > -1 or choice.find("around") > -1 or choice.find("back") > -1:
                    slowText("\nTurning around to travel back home.")
                    while distanceTraveled > 0:
                        distanceTraveled -= 10
                        player.fuel -= 10
                        if player.fuel <= 0:
                            slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                            endGame()
                            break
                    planet_beta98.beta98_landed(player)
                else:
                    repeat = True
        elif direction == "east":
            repeat = True
            while repeat:
                repeat = False
                distanceTraveled += 10
                player.fuel -= 10
                if player.fuel <= 0:
                    slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                    endGame()
                slowText("\nYou have used 10% of your fuel but have not found a planet. Would you like to keep traveling East or turn around? ")
                choice = input(">").strip().lower()
                if choice.find("turn") > -1 or choice.find("around") > -1 or choice.find("back") > -1:
                    slowText("\nTurning around to travel back home.")
                    while distanceTraveled > 0:
                        distanceTraveled -= 10
                        player.fuel -= 10
                        if player.fuel <= 0:
                            slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                            endGame()
                            break
                    planet_beta98.beta98_landed(player)
                else:
                    repeat = True
        elif direction == "west":
            repeat = True
            while repeat:
                repeat = False
                distanceTraveled += 10
                player.fuel -= 10
                if player.fuel <= 0:
                    slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                    endGame()
                slowText("\nYou have used 10% of your fuel but have not found a planet. Would you like to keep traveling West or turn around? ")
                choice = input(">").strip().lower()
                if choice.find("turn") > -1 or choice.find("around") > -1 or choice.find("back") > -1:
                    slowText("\nTurning around to travel back home.")
                    while distanceTraveled > 0:
                        distanceTraveled -= 10
                        player.fuel -= 10
                        if player.fuel <= 0:
                            slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                            endGame()
                            break
                    planet_beta98.beta98_landed(player)
                else:
                    repeat = True
        elif direction == "up":
            repeat = True
            while repeat:
                repeat = False
                distanceTraveled += 10
                player.fuel -= 10
                if distanceTraveled >= 20:
                    example_landed(player)
                else:
                    slowText("\nYou have used 10% of your fuel but have not found a planet. Would you like to keep traveling Up or turn around? ")
                    player.fuel -= 10
                    choice = input(">").strip().lower()
                    if choice.find("turn") > -1 or choice.find("around") > -1 or choice.find("back") > -1:
                        slowText("\nTurning around to travel back home.")
                        while distanceTraveled > 0:
                            distanceTraveled -= 10
                            player.fuel -= 10
                            if player.fuel <= 0:
                                slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                                endGame()
                        planet_beta98.beta98_landed(player)
                    else:
                        repeat = True
        elif direction == "down":
            repeat = True
            while repeat:
                repeat = False
                distanceTraveled += 10
                player.fuel -= 10
                if player.fuel <= 0:
                    slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                    endGame()
                slowText("\nYou have used 10% of your fuel but have not found a planet. Would you like to keep traveling Down or turn around? ")
                choice = input(">").strip().lower()
                if choice.find("turn") > -1 or choice.find("around") > -1 or choice.find("back") > -1:
                    slowText("\nTurning around to travel back home.")
                    while distanceTraveled > 0:
                        distanceTraveled -= 10
                        player.fuel -= 10
                        if player.fuel <= 0:
                            slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                            endGame()
                            break
                    planet_beta98.beta98_landed(player)
                else:
                    repeat = True
    elif currentPlanet == "example":
        if direction == "north":
            repeat = True
            while repeat:
                repeat = False
                distanceTraveled += 10
                player.fuel -= 10
                if player.fuel <= 0:
                    slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                    endGame()
                slowText("\nYou have used 10% of your fuel but have not found a planet. Would you like to keep traveling North or turn around? ")
                choice = input(">").strip().lower()
                if choice.find("turn") > -1 or choice.find("around") > -1 or choice.find("back") > -1:
                    slowText("\nTurning around to travel back home.")
                    while distanceTraveled > 0:
                        distanceTraveled -= 10
                        player.fuel -= 10
                        if player.fuel <= 0:
                            slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                            endGame()
                    planet_example.example_landed(player)
                else:
                    repeat = True
        elif direction == "south":
            repeat = True
            while repeat:
                repeat = False
                distanceTraveled += 10
                player.fuel -= 10
                if player.fuel <= 0:
                    slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                    endGame()
                slowText("\nYou have used 10% of your fuel but have not found a planet. Would you like to keep traveling South or turn around? ")
                choice = input(">").strip().lower()
                if choice.find("turn") > -1 or choice.find("around") > -1 or choice.find("back") > -1:
                    slowText("\nTurning around to travel back home.")
                    while distanceTraveled > 0:
                        distanceTraveled -= 10
                        player.fuel -= 10
                        if player.fuel <= 0:
                            slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                            endGame()
                    planet_example.example_landed(player)
                else:
                    repeat = True
        elif direction == "east":
            repeat = True
            while repeat:
                repeat = False
                distanceTraveled += 10
                player.fuel -= 10
                if player.fuel <= 0:
                    slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                    endGame()
                slowText("\nYou have used 10% of your fuel but have not found a planet. Would you like to keep traveling East or turn around? ")
                choice = input(">").strip().lower()
                if choice.find("turn") > -1 or choice.find("around") > -1 or choice.find("back") > -1:
                    slowText("\nTurning around to travel back home.")
                    while distanceTraveled > 0:
                        distanceTraveled -= 10
                        player.fuel -= 10
                        if player.fuel <= 0:
                            slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                            endGame()
                    planet_example.example_landed(player)
                else:
                    repeat = True
        elif direction == "west":
            repeat = True
            while repeat:
                repeat = False
                distanceTraveled += 10
                player.fuel -= 10
                if player.fuel <= 0:
                    slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                    endGame()
                slowText("\nYou have used 10% of your fuel but have not found a planet. Would you like to keep traveling West or turn around? ")
                choice = input(">").strip().lower()
                if choice.find("turn") > -1 or choice.find("around") > -1 or choice.find("back") > -1:
                    slowText("\nTurning around to travel back home.")
                    while distanceTraveled > 0:
                        distanceTraveled -= 10
                        player.fuel -= 10
                        if player.fuel <= 0:
                            slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                            endGame()
                    planet_example.example_landed(player)
                else:
                    repeat = True
        elif direction == "up":
            repeat = True
            while repeat:
                repeat = False
                distanceTraveled += 10
                player.fuel -= 10
                if player.fuel <= 0:
                    slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                    endGame()
                slowText("\nYou have used 10% of your fuel but have not found a planet. Would you like to keep traveling Up or turn around? ")
                choice = input(">").strip().lower()
                if choice.find("turn") > -1 or choice.find("around") > -1 or choice.find("back") > -1:
                    slowText("\nTurning around to travel back home.")
                    while distanceTraveled > 0:
                        distanceTraveled -= 10
                        player.fuel -= 10
                        if player.fuel <= 0:
                            slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                            endGame()
                    planet_example.example_landed(player)
                else:
                    repeat = True
        elif direction == "down":
            repeat = True
            while repeat:
                repeat = False
                distanceTraveled += 10
                player.fuel -= 10
                if player.fuel <= 0:
                    slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                    endGame()
                if distanceTraveled >= 20:
                    planet_beta98.beta98_landed(player)
                else:
                    slowText("\nYou have used 10% of your fuel but have not found a planet. Would you like to keep traveling Up or turn around? ")
                    player.fuel -= 10
                    choice = input(">").strip().lower()
                    if choice.find("turn") > -1 or choice.find("around") > -1 or choice.find("back") > -1:
                        slowText("\nTurning around to travel back home.")
                        while distanceTraveled > 0:
                            distanceTraveled -= 10
                            player.fuel -= 10
                            if player.fuel <= 0:
                                slowText("\n\nUnfortunately you have ran out of fuel and will die a lonely death in cold space.")
                                endGame()
                        planet_example.example_landed(player)
                    else:
                        repeat = True

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
    sys.exit()

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
    elif choice.find("fuel") > -1 and not (choice.find("buy fuel") > -1):
        getFuel(player)
        return True
    elif choice.find("money") > -1:
        getMoney(player)
        return True
    elif choice.find("objects") > -1:
        getObjects(player)
        return True
    elif choice.find("quit")  > -1:
        sys.exit()
    return False




# Start the game
if __name__ == "__main__":
    os.system('cls')
    beginGame()
