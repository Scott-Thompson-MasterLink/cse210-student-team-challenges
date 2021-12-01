import arcade
import random

from ZeldaGame.scaling import SCREEN_HEIGHT, SCREEN_WIDTH, SCALING, SPRITE_SCALING

from ZeldaGame.enemy import Enemy
from ZeldaGame.obstacles import Obstacle
from ZeldaGame.room import Room
from ZeldaGame.weapon import Weapon
from ZeldaGame.obstacles_lists import *
from ZeldaGame.player import Player

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
        self.missile_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.physics_engine = None
        self._enemy = Enemy("cse210-student-team-challenges/final-project/images/monster1.png", SPRITE_SCALING,max_health=1)
        self._enemy2 = Enemy("cse210-student-team-challenges/final-project/images/monster3.png", SPRITE_SCALING,max_health=2)
        
        self.player = Player()
        self.health = 99

    def setup(self):
        """Get the game ready to play
        """

         # Set up the player

        #self.player = arcade.Sprite("cse210-student-team-challenges/final-project/images/front_run1.png", SCALING/2.5)
        self.player.center_x = 400
        self.player.center_y = self.height / 2
        self.player.scale = 0.5
        self.player.left = 10
        self.all_sprites.append(self.player)
        self.paused = False

        self.room1 = Room("cse210-student-team-challenges/final-project/images/room1.png")
        self.room2 = Room("cse210-student-team-challenges/final-project/images/room2.png")

        self.rooms_list.append(self.room1)
        self.rooms_list.append(self.room2)

        self.player_direction = 'right'
        self.shoot_direction = 'right'
        

        # Spawn a new enemy in 0 seconds
        arcade.schedule(self.add_enemy, 0)

        # Stablish the path of the boxes
        path_metal_boxes = 'cse210-student-team-challenges/final-project/images/metal_box.png'
        path_blue_boxes = 'cse210-student-team-challenges/final-project/images/bluebox.png'

        # Add the boxes to the current room
        self.rooms_list[self.current_room].add_multiple_sprites(path_blue_boxes, blue_boxes)
        self.rooms_list[self.current_room].add_multiple_sprites(path_metal_boxes, metal_boxes)

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player,
                                                         self.rooms_list[self.current_room].sprite_list)

# ########## Load background music
# ########## Sound source: http://ccmixter.org/files/Apoxode/59262
# ########## License: https://creativecommons.org/licenses/by/3.0/


        self.background_music = arcade.load_sound(
            "cse210-student-team-challenges/final-project/sounds/Apoxode_-_Electric_1.wav"
        )

# ########## Load all the sounds
# ########## Sound sources: Jon Fincher
        self.collision_sound = arcade.load_sound("cse210-student-team-challenges/final-project/sounds/Collision.wav")
        # self.move_up_sound = arcade.load_sound("sounds/Rising_putter.wav")
        # self.move_down_sound = arcade.load_sound("sounds/Falling_putter.wav")


# ########## Play the background music and schedule the loop
        self.play_background_music()
        arcade.schedule(self.play_background_music, 15)

    def play_background_music(self, delta_time: int = 0):
        """Starts playing the background music
    """
        self.background_music.play()

    def add_enemy(self, delta_time: float):
        """Adds a new enemy to the screen
    Arguments:
        delta_time {float} -- How much time has passed since the last call
    """

        if self.paused:
            return

        # Set its position to a random height and off screen right
        self._enemy2.position_enemy(100, 400)

        self._enemy.position_enemy(600, 150)
        
        # Add it to the enemies list
        self.enemies_list.append(self._enemy)
        self.all_sprites.append(self._enemy)
        self.enemies_list.append(self._enemy2)
        self.all_sprites.append(self._enemy2)

            
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

        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        # if symbol == arcade.key.SPACE:

        #     if self.shoot_direction == 'right':
                

        #     elif self.shoot_direction == 'left':
                
               
        #     elif self.shoot_direction == 'down':
                
               
        #     elif self.shoot_direction == 'top':

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

        if self.player.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player,
                                                                self.rooms_list[self.current_room].sprite_list)
            self.player.center_x = 0

        elif self.player.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player,
                                                                self.rooms_list[self.current_room].sprite_list)
            self.player.center_x = SCREEN_WIDTH

        # This line of code prevents player to go through the obstaclees
        self.physics_engine.update()

        self._enemy.update(5, 70)
        self._enemy2.update(5, 70)


        if self.player.collides_with_list(self.enemies_list):
            # if delta_time >=3:
            self.collision_sound.play()

            if self.health > 0:
                self.health -= 1
            # Stop the game and schedule the game close
            else:
                self.paused = True
                arcade.schedule(lambda delta_time: arcade.close_window(), 0.5)

        for enemy in self.enemies_list:
            collisions = enemy.collides_with_list(self.missile_list)

            if collisions:
                self.collision_sound.play()
                           
                enemy.cur_health -= 1
                if enemy.cur_health <= 0:
                    enemy.remove_from_sprite_lists()
                    self.rooms_list[self.current_room].list_of_enemies.append(enemy)
                
                for missile in collisions:                   
                    missile.remove_from_sprite_lists() 
        
        # This removes all the right boxes if the count of enemies died are 2 (just for room1)
        self.room1.remove_walls(2)

        # Update everything
        for sprite in self.all_sprites:
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )
            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )

        if self.player.top > self.height:
            self.player.top = self.height
        elif self.player.bottom < 0:
            self.player.bottom = 0   
    
    def on_draw(self):
        """Draw all game objects
        """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                             self.rooms_list[self.current_room].background)
        # Draw all the walls in this room

        self.rooms_list[self.current_room].sprite_list.draw()
        arcade.draw_text(f"Health: {self.health + 1}", 2, 10, arcade.color.RED, 12)


        self.all_sprites.draw()
        self.player.draw()
        self.enemies_list.draw()

        for enemy in self.enemies_list:
            enemy.draw_health_number()
            enemy.draw_health_bar()


if __name__ == "__main__":
    app = ZeldaGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    app.setup()
    arcade.run()