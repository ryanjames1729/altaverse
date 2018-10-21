from main import *


def beta98_landed(player):
    os.system('cls')
    slowText("\n\nYou have arrived at Planet Beta-98. On this planet, there are multiple places that you can go. You can go to the Launch Pad, the Supply Store, the Hotel, or to the Cryo-Sleep Station.")
    beta98_main(player)

def beta98_main(player):
    repeat = True
    while repeat:
        repeat = False
        slowText("\nWhat would you like to do? ")
        choice = input(">")
        choice = choice.strip()
        choice = choice.lower()
        if otherWords(player, choice):
            repeat = True
        elif choice.find("launch") > -1 or choice.find("pad") > -1 or choice.find("travel") > -1:
            beta98_launchPad(player)
        elif choice.find("store") > -1 or choice.find("supplies") > -1 or choice.find("buy") > -1:
            beta98_store(player)
        elif choice.find("hotel") > -1 or choice.find("rest") > -1:
            beta98_hotel(player)
        elif choice.find("cryo") > -1 or choice.find("sleep") > -1:
            beta98_cryoSleep(player)
        else:
            repeat = True
            slowText("Sorry that is not a command.")

def beta98_launchPad(player):
    slowText("\n\nWelcome to the Launch Pad on Planet Beta-98. For each planet that you visit, you will use up some of your fuel. Since the distances to each of the planets are not known right now, you will not know the amount of fuel used until you have reached your destination. Some of the planets will have resupply stations and some will not.")
    repeat = True
    while repeat:
        repeat = False
        slowText("\nWould you like to travel or leave the Launch Pad? ")
        choice = input(">").strip().lower()
        if otherWords(player, choice):
            repeat = True
        elif choice.find("resupply") > -1 or choice.find("buy fuel") > -1:
            repeat = True
            if player.money < (100-player.fuel):
                amount = player.money
            else:
                amount = 100 - player.fuel
            slowText("\nYou can purchase {} of fuel. How much would you like to purchase? ".format(amount))
            fuel = input(">")
            try:
                player.money -= int(fuel)
                player.fuel += int(fuel)
                slowText("\nYou purchased {}% amount of fuel for ${}. Your fuel is now at {}% and you have ${} left.".format(fuel, fuel, player.fuel, player.money))
            except:
                slowText("\nSorry but you must type a number in. ")
        elif choice.find("leave") > -1 or choice.find("go away") > -1 or choice.find("go back") > -1:
            slowText("\nLeaving the Launch Pad. ")
            beta98_main(player)
        elif choice.find("travel") > -1 or choice.find("fly") > -1:
            slowText("\nYou have the option to travel north, south, east, west, up, or down from Planet Beta-98. Which direction would you like to go? ")
            choice = input(">")
            if otherWords(player, choice):
                repeat = True
            elif choice.find("north") > -1:
                travel(player, "beta98", "north")
            elif choice.find("south") > -1:
                travel(player, "beta98", "south")
            elif choice.find("east") > -1:
                travel(player, "beta98", "east")
            elif choice.find("west") > -1:
                travel(player, "beta98", "west")
            elif choice.find("up") > -1:
                travel(player, "beta98", "up")
            elif choice.find("down") > -1:
                travel(player, "beta98", "down")
            else:
                repeat = True
                slowText("Sorry that is not a command.")
        else:
            repeat = True
            slowText("Sorry that is not a command.")


def beta98_store(player):
    slowText("\n\nWelcome to the Beta-98 store. We have several items in our store at various prices.")
    repeat = True
    while repeat:
        repeat = False
        slowText("\nWhat would you like to purchase? ")
        choice = input(">").strip().lower()
        if otherWords(player, choice):
            repeat = True
        elif choice.find("leave") > -1 or choice.find("go away") > -1 or choice.find("go back") > -1:
            slowText("\nLeaving the store. ")
            beta98_main(player)
        else:
            if choice.find("food") > -1:
                slowText("\nFood cost $5 per unit. Would you like to purchase a unit of food? ")
                decision = input(">").strip().lower()
                if decision == "y" or decision == "yes":
                    if player.money < 5:
                        slowText("\nI'm sorry but you do not have enough money to buy food. ")
                        repeat = True
                    else:
                        player.currentObjects.append("food")
                        player.money -= 5
                        slowText("\nYou just purchased a unit of food.")
                        repeat = True
                else:
                    repeat = True
            elif choice.find("blaster") > -1:
                slowText("\nBlasters cost $100. Would you like to purchase a blaster? ")
                decision = input(">").strip().lower()
                if decision == "y" or decision == "yes":
                    if player.money < 100:
                        slowText("\nI'm sorry but you do not have enough money to buy a blaster. ")
                        repeat = True
                    else:
                        player.currentObjects.append("blaster")
                        player.money -= 100
                        slowText("\nYou just purchased a blaster.")
                        repeat = True
                else:
                    repeat = True
            elif choice.find("kit") > -1 or choice.find("emergency") > -1:
                slowText("\nEmergency kits cost $50. Would you like to purchase an emergency kit? ")
                decision = input(">").strip().lower()
                if decision == "y" or decision == "yes":
                    if player.money < 50:
                        slowText("\nI'm sorry but you do not have enough money to buy an emergency kit. ")
                        repeat = True
                    else:
                        player.currentObjects.append("emergency kit")
                        player.money -= 50
                        slowText("\nYou just purchased an emergency kit.")
                        repeat = True
                else:
                    repeat = True
            else:
                slowText("\nI'm sorry but we do not have a {}. ".format(choice))
                repeat = True

def beta98_hotel(player):
    #boost health 5% each night, costs $20/night, time.sleep(30)/night
    slowText("\n\nWelcome to the Hotel. You can sleep for as many nights as you can afford. The rate per night is $20 per night.")
    repeat = True
    while repeat:
        repeat = False
        slowText("\nHow many nights would you like to stay for? ")
        choice = input(">").strip().lower()
        if otherWords(player, choice):
            repeat = True
        elif choice.find("leave") > -1 or choice.find("go away") > -1 or choice.find("go back") > -1:
            slowText("\nLeaving the Hotel. ")
            beta98_main(player)
        else:
            try:
                days = int(choice)
                if player.money < days*20:
                    slowText("\nI'm sorry but you do not have enough money to stay for {} nights.".format(days))
                    repeat = True
                else:
                    slowText("\nYou are going to stay here for {} nights. Your stay will cost you ${}.".format(days, days*20))
                    player.money -= int(days*20)
                    time.sleep(days*10)
                    player.health += 5
                    if player.health > 100:
                        player.health = 100
                    slowText("\nThat rest was great, your health is now at {}% and now you have ${}.".format(player.health, player.money))
                    beta98_hotel(player)
            except:
                repeat = True
                slowText("Sorry that is not a command.")


def beta98_cryoSleep(player):
    #boost health to 100
    slowText("\n\nWelcome to the Cryo Sleep Station. You can sleep for as many days as you would like. Since you are a traveler of this new system, there is no charge for the Cryo Sleep, but you will have to wait for the Cryo Sleep to take effect.")
    repeat = True
    while repeat:
        repeat = False
        slowText("\nHow many days would you like to sleep for? ")
        choice = input(">").strip().lower()
        if otherWords(player, choice):
            repeat = True
        elif choice.find("leave") > -1 or choice.find("go away") > -1 or choice.find("go back") > -1:
            slowText("\nLeaving the Cryo Sleep Station. ")
            beta98_main(player)
        else:
            try:
                days = int(choice)
                slowText("\nGet ready, you are about to step into the Cryo Sleep for {} days. Enjoy your rest!".format(days))
                time.sleep(days)
                player.health = 100
                slowText("\nThat rest was great, your health is now at {}%.".format(player.health))
                beta98_cryoSleep(player)
            except:
                repeat = True
                slowText("Sorry that is not a command.")
