import arcade
from ZeldaGame.scaling import *
from ZeldaGame.room_links import *

class RoomTransitions:
    
    def room_transition_right(self, player, current_room):

        if player.center_x > SCREEN_WIDTH and current_room == 0:
            current_room = 1
            player.center_x = 0

    def room_transition_left(self, player, current_room):
        
        if player.center_x < 0 and current_room == 1:
            current_room = 0
            player.center_x = SCREEN_WIDTH

    def room_transition_up(self, player, current_room):
        
        if player.center_y > SCREEN_HEIGHT and current_room == 0:
            current_room = 1
            player.center_y = 0

    def room_transition_down(self, player, current_room):
        
        if player.center_y < 0 and current_room == 0:
            current_room = 1
            player.center_y = SCREEN_HEIGHT

    # def transition_between_rooms(self, player, current_room):

    #     if player.center_x > SCREEN_WIDTH and current_room == 0:
    #         current_room = 1
    #         player.center_x = 0

    #     elif player.center_x < 0 and current_room == 1:
    #         current_room = 0
    #         player.center_x = SCREEN_WIDTH

    #     elif player.center_x > SCREEN_WIDTH and current_room == 1:
    #         current_room = 2
    #         player.center_x = 0

    #     elif player.center_x < 0 and current_room == 2:
    #         current_room = 1
    #         player.center_x = SCREEN_WIDTH
        
    #     return current_room

    def transition_rooms(self,player,current_room,new_current_room:RoomLinks):
        if player.center_x > SCREEN_WIDTH and new_current_room.links['right'] is not None:
            new_current_room = new_current_room.links['right']
            player.center_x = 0

        elif player.center_x < 0 and new_current_room.links['left'] is not None:
            new_current_room = new_current_room.links['left']
            player.center_x = SCREEN_WIDTH

        elif player.center_y > SCREEN_HEIGHT and new_current_room.links['up'] is not None:
            new_current_room = new_current_room.links['up']
            player.center_y = 0

        elif player.center_y < 0 and new_current_room.links['down'] is not None:
            new_current_room = new_current_room.links['down']
            player.center_y = SCREEN_HEIGHT

        # return new_current_room.room_id
        return new_current_room

transition = RoomTransitions()