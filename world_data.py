from Room import Room, Connection
from Item import Item


def aelurna_description():
    description = "Aelurna is a world full of adventures and possiblities."
    return description


def init_inventory():
    inv = [Item("Dirty Pants", "Pants with holes, covered in mud and smell like a hobo", "Clothes", 4),
           Item("Rusty Dagger", "This \"dagger\" is only about 3 inches long and very rusty", "One-Handed", 2),
           Item("Faded sketching", "The flimsy piece of paper is dirty but the sketching of the beautiful "
                                   "young woman looks like it was sketched by a skilled artist.", "Misc")]
    return inv


def load_rooms():
    """
    A room has description, technical_notes, objects, npcs, connections
    A room is a dictionary object with its name as the index
    and the rest of the items stored as a list
    """
    items = [Item("Rusty Key", "a heavy key covered in rust.", "Misc", 1,
                  "You found a loose brick on the floor. Uncovering it reveals a key covered in damp mold."),
             Item("Smelly sock", "a foul smelling moldy sock.", "Misc", 2,
                  "In the corner of the room there is a moldy sock. It doesn't look very useful.")
             ]

    # name, connecting_room, location, descr, locked=False, toggle_condition=None
    connections = [Connection("Prison cell door", "Deep Dungeon Corridor", "On the wall",
                              "heavy wooden door wrapped in iron", True, "Rusty Cell Key"),
                   Connection("Prison cell window", None, "Opposite the door", "small round, barred window. "
                              "No light comes through but you can a hear a dripping sound. Unfortunately the window is very small.", False),
                   Connection("Wide Open Door", "Dungeon Corridor", "Ready for you", "come on through. ", False, "Open")
                   ]
    rooms = {
        "Prisoner's Cell": Room(
            "Prisoner's Cell",
            "The floor of this cramped room is a hard stone surface. There is barely any light. The air is dank, musty and has a smell of death. "
            "In the dim light you can make out chains on the wall.",
            "This is the room where the game starts.",
            items,  # objects in room
            None,  # NPCs in room
            connections  # Connections to other rooms
        ),
        "Dungeon Corridor": Room(
            "Dungeon Corridor",
            "YOU MADE IT!! ",
            "test test",
            None,  # objects in room
            None,  # NPCs in room
            None  # Connections to other rooms
        )
    }


    return rooms

# Define the first room. Must be available above in load_rooms.
def get_first_room():
    return "Prisoner's Cell"
