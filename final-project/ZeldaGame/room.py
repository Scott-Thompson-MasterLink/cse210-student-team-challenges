import arcade
from ZeldaGame.abstract_object import MainObjects

class Room(MainObjects):

    def __init__(self, background):
        self.__wall_list = arcade.SpriteList()
        self.__list_of_enemies = []
        self.background = arcade.load_texture(f"{background}")
    
    @property
    def sprite_list(self):
        return self.__wall_list
    
    @property
    def list_of_enemies(self):
        return self.__list_of_enemies
    
    def add_sprite(self, sprite_object):
        sprite = sprite_object
        self.__wall_list.append(sprite)

    def remove_walls(self, counter):

        if len(self.__list_of_enemies) == counter:
            for i in self.__wall_list.sprite_list:
                if i.left == 775:
                    self.__wall_list.sprite_list.remove(i)
                    i.visible = False
        else:
            return