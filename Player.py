from world_data import init_inventory
import sys
import helpers as hp

class Player:
    """
    A player has a name
    A player has an inventory
    A player has characteristics (sex, age, race)
    A player has attributes (strength, intelligence, charisma, agility, wisdom)
    """

    # Default characteristics and attributes below can be changed
    characteristics = {
        "age": 25,
        "sex": "m",
        "race": "human"
    }

    attributes = {
        "lvl": 1,
        "hp": 100,
        "str": 10,
        "agi": 10,
        "int": 10,
        "wis": 10,
        "char": 10
    }

    inventory = init_inventory()

    def __init__(self, name):
        self.name = name

    def print_player_menu(self):
        print('1. Inspect Room')
        print('2. View inventory')
        print('3. View character')
        print('4. Exit game')
        print('> ', end='')
        return

    def play(self, room):
        while True:
            self.print_player_menu()
            player_input = int(input())
            if player_input == 1:#inspect room
                r = room.room_menu(self)  # pass in player ref so that we can check inventory
                if r is not None:  # If our room interaction resulted in us changing rooms...
                    return r
                else:
                    continue
            elif player_input == 2:#inspect inventory
                self.print_player_inventory()
                continue
            elif player_input == 3:#View character stats
                self.print_player_characteristics()
                self.print_player_attr()
                continue
            elif player_input == 4:#exit game
                sys.exit()
            else:
                print("Selection unrecognized.")

    def print_player_inventory(self):
        while True:
            hp.rpg_print("In your inventory you currently possess the following:")
            for i, val in enumerate(self.inventory):
                print('{}. {}'.format((i+1), val.name))

            print("Inspect which item? (0 to return)")
            print('> ', end='')
            player_input = int(input()) - 1
            print("*****")
            if player_input < 0:
                return
            elif player_input > len(self.inventory):
                return
            else:
                print(self.inventory[player_input])
                print("Press enter to continue...", end='')
                input()

            print("*****")

    def print_player_characteristics(self):
        print(self.characteristics)
        return

    def print_player_attr(self):
        print(self.attributes)
        return

    # TODO: Make sure that this removes item from Room
    def take_item(self, room, item):
        self.inventory.append(item)
        room.objects.remove(item)
        print('{} {}'.format(item.name, "has been added to your inventory."))
        return

    # This function will take a string. Currently this is used to check if a
    # key needed to open a door exists. returns true/false
    def check_for_item(self, item_name):
        for i in self.inventory:
            if str(i.name) == str(item_name):
                return True

        # if loop completes, return False
        return False

    # add item object to inventory list
    def add_item(self, item):
        self.inventory.append(item)
        print(self.inventory[-1].name + " has been added to your inventory.")
        return

    # Make this more efficient later. How to find item in list with
    # a particular value in its object and remove it?
    def use_key(self, key_name):
        index = None
        for i, val in enumerate(self.inventory):
            if str(val.name) == str(key_name):
                pass
