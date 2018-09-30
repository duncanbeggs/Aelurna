from helpers import rpg_print, req_player_interaction

class Connection:
    """
    A connection belongs to a room
    It points to another room
    It can be either locked or unlocked
    It can have a lock-toggle condition
    """
    def __init__(self, name, connecting_room, location, descr, locked=False, toggle_condition=None):
        self.name = name
        self.connecting_room = connecting_room
        self.location = location
        self.descr = descr
        self.locked = locked
        self.toggle_condition = toggle_condition

    # Print connection attributes for the player
    def print_conn_descr(self, conn_num):
        rpg_print('{}. {} there is a {}.{}.'.format(conn_num,
                            self.location, self.descr, ' It is locked.' if self.locked else ''))

    # Allow the player to interact with the connection, unlocking or locking it
    # Need this to change Rooms
    def interact_with_conn(self, player):
        if self.toggle_condition is None:
            rpg_print("You can't go through the " + self.name + ".")
            return
        else:  # door has possible passage, if unlocked go through, if locked check inventory
            if self.locked is False:
                return self.connecting_room
            else:
                # check inventory for required item
                # Ask player if want to use item
                # if player yes:
                # use item, remove item, toggle locked, go to next room
                # if player no: pass
                if player.check_for_item(self.toggle_condition):
                    rpg_print("Your {} will open {}. Would you like to use it? (y/n)".format(
                        self.toggle_condition, self.name
                    ))
                    print("Input> ", end='')
                    player_input = str(input()).strip()
                    if player_input == 'y' or 'Y':
                        player.use_key(self.toggle_condition)
                        self.locked = False  # make door unlocked

                        pass # proceed through door, etc
                    else:
                        rpg_print("You have chosen not to leave your current location...")
                        return
                else:
                    rpg_print("{} is locked but you don't have the key.".format(self.name))
                    return
        pass


class Room:
    """
    A room has zero or more objects
    A room contains zero or more non-player characters
    A room has a description
    A room is connected to one or more other rooms
    """

    def __init__(self, name, description, technical_notes, objects, npcs, connections):
        self.name = name
        self.description = description
        self.objects = objects  # list of objects in the room
        self.npcs = npcs  # list of non-player characters in the room
        self.connections = connections  # list of connections to other rooms

    def connection_menu(self, player):
        if not self.connections:
            rpg_print("There don't appear to be any ways out of this room")
        else:  # If there are connections in the room
            for i, c in enumerate(self.connections):
                i += 1
                c.print_conn_descr(i)
            print("Interact with door or exit? (0 for no)")
            print("Door> ", end='')
            player_input = int(input())
            if player_input < 1 or player_input > len(self.connections):  # if input num is in range of connections
                print("EXITING DOOR SELECTION")
                pass
            else:
                return self.connections[player_input - 1].interact_with_conn(player) # player ref is for inv check
        pass

    def add_room_item_to_inv(self, index, player):
        player.add_item(self.objects[index])
        del self.objects[index]

    def object_menu(self, player):
        if not self.objects:
            rpg_print("There doesn't appear to be any unusual objects in the room")
            return
        else:
            for i, o in enumerate(self.objects):
                i += 1
                o.print_obj_descr(i)

                # Ask player if they want to take item. Return true or false.
                # If statement to handle either case
                if req_player_interaction():
                    self.add_room_item_to_inv((i-1), player)
                else:
                    return


    def npc_menu(self):
        pass

    # menu to interact with doors, objects, nps
    def room_menu(self, player):
        self.print_room_descr()
        # Player can interact with objects, NPCs and connections (doors)
        print("What would you like to inspect?")
        rpg_print("1. Doors\n2. Look for interesting objects.\n3. Interact with NPCs. 4. Back to main.")
        player_input = int(input())

        # go to conn menu and if player changes room, return the room back to player.play then world.play
        if (player_input == 1):
            return self.connection_menu(player)
        elif player_input == 2:
            self.object_menu(player)
        elif player_input == 3:
            self.npc_menu()
        elif player_input == 4:
            return self  # Returning to main menu, return room to show no change has ocurred
        else:
            print("What??")
            self.room_menu(player)


    # Print room descr then go to menu
    def print_room_descr(self):
        print("***** {} *****".format(self.name))
        rpg_print(self.description)


