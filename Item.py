from helpers import rpg_print

class Item:
    def __init__(self, name, description, type, weight=0, room_descr=None):
        self.name = name
        self.description = description
        self.type = type
        self.weight = weight
        self.room_descr = room_descr


    def print_obj_descr(self, obj_num):
        rpg_print('{}. {} Would you like to take the {}?'.format(obj_num,
                            self.room_descr, self.name))


    def __str__(self):
        return '{}: {}\nType: {} || Weight: {}'.format(
            self.name, self.description, self.type, self.weight)