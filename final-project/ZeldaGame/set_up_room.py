from ZeldaGame.room import Room
from ZeldaGame.obstacles_lists import *
from ZeldaGame.enemy import Enemy
from ZeldaGame.scaling import SPRITE_SCALING
from ZeldaGame.paths import *

# Room 1
room1 = Room(path_room1)

room1.add_multiple_sprites(path_blue_boxes, little_boxes_right)
room1.add_multiple_sprites(path_blue_boxes, little_boxes_bottom)
room1.add_multiple_sprites(path_blue_boxes, little_boxes_left)
room1.add_multiple_sprites(path_blue_boxes, little_boxes_top)
room1.add_multiple_sprites(path_metal_boxes, corner_boxes)

enemy = Enemy(path_enemy1, SPRITE_SCALING,max_health=1)
enemy2 = Enemy(path_enemy2, SPRITE_SCALING,max_health=2)
enemy2.position_enemy(100, 400)
enemy.position_enemy(600, 150)

room1.list_of_enemies.append(enemy)
room1.list_of_enemies.append(enemy2)

room1.set_enemies_in_room(2)

# Room2
room2 = Room(path_room2)

room2.add_multiple_sprites(path_green_boxes, little_boxes_right)
room2.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
# room2.add_multiple_sprites(path_green_boxes, little_boxes_left)
room2.add_multiple_sprites(path_green_boxes, little_boxes_top)
room2.add_multiple_sprites(path_metal_violet_box, corner_boxes)

enemy3 = Enemy(path_enemy3, SPRITE_SCALING,max_health=10)
enemy4 = Enemy(path_enemy3, SPRITE_SCALING,max_health=10)
enemy3.position_enemy(100, 150)
enemy4.position_enemy(500, 500)

room2.list_of_enemies.append(enemy3)
room2.list_of_enemies.append(enemy4)

room2.set_enemies_in_room(2)