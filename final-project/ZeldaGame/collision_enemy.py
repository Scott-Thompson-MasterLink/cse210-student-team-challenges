import arcade

from ZeldaGame.paths import path_collision_sound


class EnemyCollision:

    def enemy_collides_with_missile(self, enemies_list, missile_list, current_room, damage):
        for enemy in enemies_list:
            collisions = enemy.collides_with_list(missile_list)

            if collisions:
                collision_sound = arcade.load_sound(path_collision_sound)
                collision_sound.play()

                enemy.cur_health -= damage

                if enemy.cur_health <= 0:
                    enemy.remove_from_sprite_lists()
                    current_room.set_died_enemy(1)
                
                for missile in collisions:                   
                    missile.remove_from_sprite_lists() 

enemy_collision = EnemyCollision()