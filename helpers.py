import time
import sys


# Take a room as an argument and print its description

def rpg_print(output_text):
    time.sleep(.1)
    sys.stdout.flush()
    for s in output_text:
        print(s, end='')
        # time.sleep(1.2)
        # sys.stdout.flush()
    sys.stdout.flush()
    print("\n*****")
    time.sleep(0.4)
    return


def print_startup(first_room):
    rpg_print("You awaken from unpleasant, vague dreams. Your body hurts from the sleep.")
    rpg_print(first_room.description)
    pass


def startup_room():
    rpg_print("You come to your senses and look around the room. You don't know where you "
              "are but you know that you want to get out")


def request_name():
    rpg_print("As you rub your head you think you can remember your name...")
    print("Name> ", end='')
    name = input()
    rpg_print('{} {} {}'.format("You remember that your name is", name,
                                "but all other details of your life are shrouded in fog."))
    return name


def req_player_interaction():
    while True:
        print("y/n")
        player_input = str(input()).lower()
        if player_input == 'y':
            return True
        elif player_input == 'n':
            return False
        else:
            print("What??")
            continue
