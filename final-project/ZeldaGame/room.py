import arcade
from ZeldaGame.abstract_object import MainObjects
from ZeldaGame.obstacles import Obstacle
from ZeldaGame.scaling import SPRITE_SCALING

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
            for i in self.__wall_list:
                if i.left == 775:
                    self.__wall_list.remove(i)
                    i.visible = False
        else:
            return

    def add_multiple_sprites(self, path, coordinates_list):

        for box in coordinates_list:
            blue_box = Obstacle(path, SPRITE_SCALING)
            blue_box.position_obstacle(box[0], box[1])
            self.add_sprite(blue_box)
