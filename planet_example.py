import main, os, sys, time


def example_landed(player):
    os.system('cls')
    main.slowText("\n\nYou have arrived at Planet <Example>. On this planet, there are multiple places that you can go.")
    example_main(player)

def example_main(player):
    repeat = True
    while repeat:
        repeat = False
        main.slowText("\nWhat would you like to do? ")
        choice = input(">").strip().lower()

        if main.otherWords(player, choice):
            repeat = True
        elif choice.find("launch") > -1 or choice.find("pad") > -1 or choice.find("travel") > -1:
            example_launchPad(player)
        else:
            repeat = True
            main.slowText("Sorry that is not a command.")

def example_launchPad(player):
    main.slowText("\n\nWelcome to the Launch Pad on Planet <example>. ")
    repeat = True
    while repeat:
        repeat = False
        main.slowText("\nWould you like to travel or leave the Launch Pad? ")
        choice = input(">").strip().lower()
        if main.otherWords(player, choice):
            repeat = True
        elif choice.find("resupply") > -1 or choice.find("buy fuel") > -1:
            repeat = True
            if player.money < (100-player.fuel):
                amount = player.money
            else:
                amount = 100 - player.fuel
            main.slowText("\nYou can purchase {}% of fuel. How much would you like to purchase? ".format(amount))
            fuel = input(">")
            try:
                player.money -= int(fuel)
                player.fuel += int(fuel)
                main.slowText("\nYou purchased {}% amount of fuel for ${}. Your fuel is now at {}% and you have ${} left.".format(fuel, fuel, player.fuel, player.money))
            except:
                main.slowText("\nSorry but you must type a number in. ")
        elif choice.find("leave") > -1 or choice.find("go away") > -1 or choice.find("go back") > -1:
            main.slowText("\nLeaving the Launch Pad. ")
            example_main(player)
        elif choice.find("travel") > -1 or choice.find("fly") > -1:
            main.slowText("\nYou have the option to travel north, south, east, west, up, or down from Planet Beta-98. Which direction would you like to go? ")
            choice = input(">")
            if main.otherWords(player, choice):
                repeat = True
            elif choice.find("north") > -1:
                main.travel(player, "example", "north")
            elif choice.find("south") > -1:
                main.travel(player, "example", "south")
            elif choice.find("east") > -1:
                main.travel(player, "example", "east")
            elif choice.find("west") > -1:
                main.travel(player, "example", "west")
            elif choice.find("up") > -1:
                main.travel(player, "example", "up")
            elif choice.find("down") > -1:
                main.travel(player, "example", "down")
            else:
                repeat = True
                main.slowText("Sorry that is not a command.")
        else:
            repeat = True
            main.slowText("Sorry that is not a command.")
