import arcade
import random

from ZeldaGame.scaling import SCALING, SCREEN_WIDTH,HEALTHBAR_WIDTH,HEALTHBAR_HEIGHT,HEALTHBAR_OFFSET_Y,HEALTH_NUMBER_OFFSET_X,HEALTH_NUMBER_OFFSET_Y, SCREEN_HEIGHT
from ZeldaGame.fire import *
from ZeldaGame.weapon import Weapon

class Enemy(arcade.Sprite):
    
    def __init__(self, filename, sprite_scaling, max_health, movement = 0, velocity = 1, shoot = False, shot_frequency = 1):
    
        super().__init__(filename, sprite_scaling)
        self.moving_left = True
        self.moving_right = False
        self.moving_up = True
        self.moving_down = False

        # Add extra attributes for health
        self.max_health = max_health
        self.cur_health = max_health
        self.movement = movement
        self.velocity = velocity
        self.shoot = shoot
        self.shot_frequency = shot_frequency
        self.shots = [ShootUp(), ShootDown(), ShootLeft(), ShootRight()]

    def position_enemy(self, left, bottom):
        self.left = left
        self.bottom = bottom

    def move(self, factor, collide_at):
        
        if self.movement == 0:
            self.moving_up = False

            if self.center_x > collide_at and self.moving_left == True:
                self.moving_right = False
                self.center_x -= factor

            if self.left < collide_at:
                self.moving_right = True
            
            if self.moving_right:
                self.moving_left = False
                self.center_x += factor

            if self.right > SCREEN_WIDTH - collide_at:
                self.moving_left = True
                self.moving_right = False
                self.center_x -= factor

        elif self.movement == 1:

            self.moving_left = False

            if self.center_y > collide_at and self.moving_up == True:
                self.moving_down = False
                self.center_y -= factor

            if self.bottom < collide_at:
                self.moving_down = True

                
            if self.moving_down:
                self.moving_up = False
                self.center_y += factor

            if self.top > SCREEN_HEIGHT - collide_at:
                self.moving_up = True
                self.moving_down = False
                self.center_y -= factor

        elif self.movement == 3:
            self.moving_up = False

            if self.center_x > collide_at and self.moving_left == True:
                self.moving_right = False
                self.center_x -= factor

            if self.left < collide_at:
                self.moving_down = True

            if self.moving_down:
                self.moving_left = False
                self.center_y -= factor

            if self.top > SCREEN_HEIGHT - collide_at:
                self.moving_left = False
                self.moving_down = False
                self.center_x -= factor

            if self.right > SCREEN_WIDTH - collide_at:
                self.moving_up = True
                self.moving_right = False
                self.center_y += factor

            if self.bottom < collide_at:
                self.moving_right = True
                self.moving_down = False
                self.center_x += factor

    def enemy_shoot(self):
        
        new_shot = random.choice(self.shots)
        new_shot.velocity = 150 * self.shot_frequency
        shot = Shooter(new_shot)
        return shot
            
    def draw_health_number(self):
        """ Draw how many hit points we have """

        health_string = f"{self.cur_health}/{self.max_health}"
        arcade.draw_text(health_string,
                         start_x=self.center_x + HEALTH_NUMBER_OFFSET_X,
                         start_y=self.center_y + HEALTH_NUMBER_OFFSET_Y,
                         font_size=12,
                         color=arcade.color.WHITE)

    def draw_health_bar(self):
        """ Draw the health bar """

        # Draw the 'unhealthy' background
        if self.cur_health < self.max_health:
            arcade.draw_rectangle_filled(center_x=self.center_x,
                                         center_y=self.center_y + HEALTHBAR_OFFSET_Y,
                                         width=HEALTHBAR_WIDTH,
                                         height=3,
                                         color=arcade.color.RED)

        # Calculate width based on health
        health_width = HEALTHBAR_WIDTH * (self.cur_health / self.max_health)

        arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (HEALTHBAR_WIDTH - health_width),
                                     center_y=self.center_y - 10,
                                     width=health_width,
                                     height=HEALTHBAR_HEIGHT,
                                     color=arcade.color.GREEN)