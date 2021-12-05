import arcade
from ZeldaGame.scaling import *

class RoomTransitions:
    
    def transition_between_rooms(self, player, current_room):

        if player.center_x > SCREEN_WIDTH and current_room == 0:
            current_room = 1
            player.center_x = 0

        elif player.center_x < 0 and current_room == 1:
            current_room = 0
            player.center_x = SCREEN_WIDTH

        elif player.center_x > SCREEN_WIDTH and current_room == 1:
            current_room = 2
            player.center_x = 0

        elif player.center_x < 0 and current_room == 2:
            current_room = 1
            player.center_x = SCREEN_WIDTH
        
        return current_room

transition = RoomTransitions()