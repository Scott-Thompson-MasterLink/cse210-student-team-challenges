import arcade
import random

from ZeldaGame.scaling import SCREEN_HEIGHT, SCREEN_WIDTH, SCALING, SPRITE_SCALING

from ZeldaGame.enemy import Enemy
from ZeldaGame.obstacles import Obstacle
from ZeldaGame.room import Room
from ZeldaGame.weapon import Weapon
from ZeldaGame.obstacles_lists import *
from ZeldaGame.player import Player
from ZeldaGame.room_transitions import transition
from ZeldaGame.on_draw import *
# from ZeldaGame.set_up_room import room1, room2, room3
from ZeldaGame.set_up_room import *
from ZeldaGame.collision_player import player_collision
from ZeldaGame.collision_enemy import enemy_collision


from ZeldaGame.fire import Shooter, ShootUp, ShootDown, ShootLeft, ShootRight

SCREEN_TITLE = "The remixed Legend of Zelda"


class ZeldaGame(arcade.Window):
    
    def __init__(self, width, height, title):
        """Initialize the game
        """

        super().__init__(width, height, title)

        self.enemies_list = arcade.SpriteList()
        self.rooms_list = []
        self.current_room = 0
        self.new_current_room = rooms[0]
        self.missile_list = arcade.SpriteList()
        self.missile_enemy = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.player = Player()
        self.health = 99
        self.damage = 1
        self.frame_count = 0

    def setup(self):
        """Get the game ready to play
        """

        # Set up the player
        self.player.center_x = 400
        self.player.center_y = self.height / 2
        self.player.scale = 0.5
        self.player.left = 10
        self.all_sprites.append(self.player)
        self.paused = False


        for room in rrooms:
            self.rooms_list.append(room)

        # self.rooms_list.append(room1)
        # self.rooms_list.append(room2)
        # self.rooms_list.append(room3)


        self.player_direction = 'right'
        self.shoot_direction = 'right'

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player,
                                                         self.rooms_list[self.current_room].sprite_list)


        self.background_music = arcade.load_sound(
            "cse210-student-team-challenges/final-project/sounds/Apoxode_-_Electric_1.wav"
        )

        # Play the background music and schedule the loop
        self.play_background_music()
        arcade.schedule(self.play_background_music, 15)

    def play_background_music(self, delta_time: int = 0):
        """Starts playing the background music
    """
        self.background_music.play()    

            
    def on_key_press(self, symbol, modifiers):

        """Handle user keyboard input
        Q: Quit the game
        P: Pause/unpause the game
        W/A/S/D: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right
        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """

        if symbol == arcade.key.ESCAPE:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.W:

            self.player_direction = 'top'
            # self.move_up_sound.play()
            self.player.change_y = 5
        elif symbol == arcade.key.A:
            self.player_direction = 'left'
            self.player.change_x = -5
        elif symbol == arcade.key.S:
            self.player_direction = 'down'
            # self.move_down_sound.play()
            self.player.change_y = -5
        elif symbol == arcade.key.D:
            self.player_direction = 'right'
            self.player.change_x = 5

        if symbol == arcade.key.UP:
            self.shoot_direction = 'top'
            # self.move_up_sound.play()
            missile = Weapon("cse210-student-team-challenges/final-project/images/arrow_top.png", SCALING)
            shoot = Shooter(ShootUp())
            shoot.do_shoot(self.player, missile, self.missile_list, self.all_sprites)
            
        elif  symbol == arcade.key.LEFT:
            self.shoot_direction = 'left'
            missile = Weapon("cse210-student-team-challenges/final-project/images/arrow_left.png", SCALING)
            shoot = Shooter(ShootLeft())
            shoot.do_shoot(self.player, missile, self.missile_list, self.all_sprites)
            
        elif symbol == arcade.key.DOWN:
            self.shoot_direction = 'down'
            # self.move_down_sound.play()
            missile = Weapon("cse210-student-team-challenges/final-project/images/arrow_down.png", SCALING)
            shoot = Shooter(ShootDown())
            shoot.do_shoot(self.player, missile, self.missile_list, self.all_sprites)
            
        elif  symbol == arcade.key.RIGHT:
            self.shoot_direction = 'right'
            missile = Weapon("cse210-student-team-challenges/final-project/images/arrow_right.png", SCALING)
            shoot = Shooter(ShootRight())
            shoot.do_shoot(self.player, missile, self.missile_list, self.all_sprites)
                  

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released
        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if (
            symbol == arcade.key.W
            or symbol == arcade.key.S
            or symbol == arcade.key.UP
            or symbol == arcade.key.DOWN
        ):
            self.player.change_y = 0

        if (
            symbol == arcade.key.A
            or symbol == arcade.key.D
            or symbol == arcade.key.LEFT
            or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0

    def on_update(self, delta_time: float):
        """Update all game objects
        """
        if self.paused:
            return

        self.player.update()

        self.frame_count += 1

        if self.frame_count % 15 == 0:
            for i in self.rooms_list[self.current_room].list_of_enemies:
                if i.shoot:
                    new_shoot = i.enemy_shoot()
                    if 'ShootDown' in str(new_shoot._Shooter__weapon):
                        missile = Weapon("cse210-student-team-challenges/final-project/images/fire_down.png", SCALING)
                        new_shoot.do_shoot(i, missile, self.missile_enemy, self.all_sprites)
                    if 'ShootUp' in str(new_shoot._Shooter__weapon):
                        missile = Weapon("cse210-student-team-challenges/final-project/images/fire_top.png", SCALING)
                        new_shoot.do_shoot(i, missile, self.missile_enemy, self.all_sprites)
                    if 'ShootRight' in str(new_shoot._Shooter__weapon):
                        missile = Weapon("cse210-student-team-challenges/final-project/images/fire_right.png", SCALING)
                        new_shoot.do_shoot(i, missile, self.missile_enemy, self.all_sprites)
                    if 'ShootLeft' in str(new_shoot._Shooter__weapon):
                        missile = Weapon("cse210-student-team-challenges/final-project/images/fire_left.png", SCALING)
                        new_shoot.do_shoot(i, missile, self.missile_enemy, self.all_sprites) 


        # These lines allow for room transitions
        # self.current_room = transition.transition_between_rooms(self.player, self.current_room)
        self.new_current_room = transition.transition_rooms(self.player, self.current_room, self.new_current_room)
        self.current_room = self.new_current_room.room_id
        self.physics_engine = arcade.PhysicsEngineSimple(self.player,
                                                            self.rooms_list[self.current_room].sprite_list)
            

        # This line of code prevents player to go through the obstaclees
        self.physics_engine.update()


        # Updates the velocity of the enemies
        for i in self.rooms_list[self.current_room].list_of_enemies:
            velocity = 4 * i.velocity 
            i.move(velocity, 50)

        # Verifies the collision between the player and enemies
        self.health = player_collision.player_collides_with_list(self.player, self.rooms_list[self.current_room].list_of_enemies, self.health)

        # Verifies if an enemy did collide with a missile
        enemy_collision.enemy_collides_with_missile(self.rooms_list[self.current_room].list_of_enemies, self.missile_list, self.rooms_list[self.current_room], self.damage)
        
        if player_collision.player_collides_with_list(self.player, self.missile_enemy, self.health):
            self.health = player_collision.player_collides_with_list(self.player, self.missile_enemy, self.health)



        # This removes all the right boxes if the count of enemies died are the same as the enemy list
        '''
        walls_to_remove_by_room = [
            [little_boxes_left],                                            # Walls to remove for room 1
            [little_boxes_top,little_boxes_right],                          # Walls to remove for room 2
            [little_boxes_top,little_boxes_right,little_boxes_bottom],      # Walls to remove for room 3
            [little_boxes_bottom],                                          # Walls to remove for room 4
            [little_boxes_right,little_boxes_top,little_boxes_left],        # Walls to remove for room 5
            [little_boxes_bottom,little_boxes_left],                        # Walls to remove for room 6
            [little_boxes_top],                                             # Walls to remove for room 7
            [little_boxes_right,little_boxes_top,little_boxes_bottom],      # Walls to remove for room 8
            [little_boxes_left]                                             # Walls to remove for room 9
        ]
        walls_to_remove = walls_to_remove_by_room[self.current_room]
        '''
        wall_removals = {'left':little_boxes_left,'right':little_boxes_right,'up':little_boxes_top,'down':little_boxes_bottom}
        walls_to_remove = [(link,wall_removals[link]) for link,value in self.new_current_room.links.items() if value is not None]
        # self.rooms_list[self.current_room].remove_walls(walls_to_remove)
        for link,wall in walls_to_remove:
            print(self.new_current_room.links)
            # if self.rooms_list[self.current_room].__quantity_of_enemies_died == self.rooms_list[self.current_room].enemies_in_the_room:
            self.rooms_list[self.current_room].remove_walls(wall,link)

        # Update everything
        for sprite in self.all_sprites:
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )
            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )
            
    
    def on_draw(self):
        """Draw all game objects
        """
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                             self.rooms_list[self.current_room].background)

        # self.rooms_list[self.current_room].sprite_list.draw()
        


        self.player.draw()        
        new_draw = Draw(
            self.rooms_list[self.current_room].list_of_enemies, 
            self.rooms_list[self.current_room].sprite_list, 
            self.missile_list,
            self.missile_enemy
        )
        new_draw.on_draw()
        arcade.draw_text(f"Health: {self.health + 1}", 2, 10, arcade.color.YELLOW, 12, bold= True)

        
        for enemy in self.rooms_list[self.current_room].list_of_enemies:
            enemy.draw_health_number()
            enemy.draw_health_bar()


if __name__ == "__main__":
    app = ZeldaGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    app.setup()
    arcade.run()