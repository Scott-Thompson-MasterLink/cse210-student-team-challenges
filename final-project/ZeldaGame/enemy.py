import arcade
from ZeldaGame.scaling import SCREEN_WIDTH,HEALTHBAR_WIDTH,HEALTHBAR_HEIGHT,HEALTHBAR_OFFSET_Y,HEALTH_NUMBER_OFFSET_X,HEALTH_NUMBER_OFFSET_Y


class Enemy(arcade.Sprite):
    
    def __init__(self, filename, sprite_scaling,max_health):
    
        super().__init__(filename, sprite_scaling)
        self.moving_left = True
        self.moving_right = False

        # Add extra attributes for health
        self.max_health = max_health
        self.cur_health = max_health

    def position_enemy(self, left, bottom):
        self.left = left
        self.bottom = bottom

    def move_horizontally(self, factor, collide_at):

        if self.center_x > collide_at and self.moving_left == True:
            self.moving_right = False
            self.center_x -= factor

        if self.center_x < collide_at:
            self.moving_right = True
        
        if self.moving_right:
            self.moving_left = False
            self.center_x += factor

        if self.center_x > SCREEN_WIDTH - collide_at:
            self.moving_left = True
            self.moving_right = False
            self.center_x -= factor

            
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