"""
This program is an RPG.
It will be a text based RPG in a fantasy setting.
The player will start out with one character and progress from one area to another.
Each area will have a text description and some options. The purpose of the game
will be to find your way out of a dungeon and to find hopefully discover, why you are there.
"""
from World import World
import helpers as hlp

def main():
    # setup phase
    world = World("Aelurna")

    # set current_room, prev_room to the first room in the game
    current_room = world.get_current_room()
    prev_room = current_room

    hlp.print_startup(current_room)

    # initialize the player and request a name
    world.init_player()

    # Print player
    hlp.startup_room()

    while True:
        current_room = world.play()


if __name__ == '__main__':
    print("***** START *****")
    main()

