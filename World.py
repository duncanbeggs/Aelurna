import world_data
from Player import Player
import helpers as hlp

class World:
    """
    A world has a player
    A world has a name
    A world has many zones
    """

    # ***** INITIALIZATION METHODS *****
    def __init__(self, name):
        self.name = name
        self.description = world_data.aelurna_description()
        self.player = None # To be added in main loop
        self.rooms = world_data.load_rooms() # list of rooms
        self.current_room = self.rooms[world_data.get_first_room()] # to be set in init_rooms()

    def init_player(self):
        self.player = Player(hlp.request_name())

    # ***** PLAY GAME METHODS *****
    def get_current_room(self):
        return self.current_room

    # Play game, change room if changed
    def play(self):
        r = self.player.play(self.current_room)
        self.current_room = self.rooms[r]
