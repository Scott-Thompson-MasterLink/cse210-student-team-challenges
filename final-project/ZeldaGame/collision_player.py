import arcade

from ZeldaGame.paths import path_collision_sound


class PlayerCollision:

    def player_collides_with_list(self, player, list, health):
        collision_sound = arcade.load_sound(path_collision_sound)

        if player.collides_with_list(list):
            collision_sound.play()

            if health > 0:
                health -= 1
            # Stop the game and schedule the game close
            else:
                arcade.schedule(lambda delta_time: arcade.close_window(), 1)
            
            return health
        else:
            return health
    
    def player_collides_with_weapon(self, player, list, damage):
        
        if player.collides_with_list(list):
        # Loop through each colliding sprite, remove it, and add to the damage.
        
            for i in list:
                i.remove_from_sprite_lists()
            damage = damage * 2
        return damage

    def player_collides_with_health_box(self, player, list, health):

        if health < 50:
            if player.collides_with_list(list):
                # Loop through each colliding sprite, remove it, and add to the damage.
            
                for i in list:
                    i.remove_from_sprite_lists()
                health = 99
            return health
        else:
            return health

player_collision = PlayerCollision()