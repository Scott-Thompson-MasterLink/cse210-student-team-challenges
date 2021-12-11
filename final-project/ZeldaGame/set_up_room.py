from random import randint
import arcade
import random

from ZeldaGame.room import Room
from ZeldaGame.obstacles_lists import *
from ZeldaGame.enemy import Enemy
from ZeldaGame.scaling import *
from ZeldaGame.paths import *
from ZeldaGame.room_links import RoomLinks
from ZeldaGame.weapon import Weapon
from ZeldaGame.random_obstacles import *


def create_weapon(x,y,room):
    weapon =  arcade.Sprite("cse210-student-team-challenges/final-project/images/arrow.png", SCALING/4)
    weapon.center_x = x
    weapon.center_y = y
    room.list_of_weapons.append(weapon)

def create_health(x,y,room):
    health_box =  arcade.Sprite("cse210-student-team-challenges/final-project/images/box_health.png", SCALING/4)
    health_box.center_x = x
    health_box.center_y = y
    room.list_of_health_box.append(health_box)

def create_enemy_with_shoot(room, enemy_path, velocity, up_down_around, health, frequency):
    enemy = Enemy(enemy_path, SPRITE_SCALING, max_health=health, velocity=velocity, movement=up_down_around, shoot=True, shot_frequency=frequency)
    enemy.position_enemy(random.choice(range(100,650)), random.choice(range(100, 450)))
    room.list_of_enemies.append(enemy)

def create_enemy(room, enemy_path, velocity, up_down_around, health):
    enemy = Enemy(enemy_path, SPRITE_SCALING, max_health=health, velocity=velocity, movement=up_down_around,)
    enemy.position_enemy(random.choice(range(100,650)), random.choice(range(100, 450)))
    room.list_of_enemies.append(enemy)


# Room 1
# rrooms = [Room()]
rrooms = [Room(f"cse210-student-team-challenges/final-project/images/room{i%10+1}.png") for i in range(10)]
room1 = rrooms[0]
room1.add_multiple_sprites(path_blue_boxes, little_boxes_right)
room1.add_multiple_sprites(path_blue_boxes, little_boxes_bottom)
room1.add_multiple_sprites(path_blue_boxes, little_boxes_left)
room1.add_multiple_sprites(path_blue_boxes, little_boxes_top)
room1.add_multiple_sprites(path_metal_boxes, corner_boxes)
room1.add_multiple_sprites(path_blue_boxes, random_boxes[0])

create_enemy(room1, path_enemy1, velocity=2, up_down_around=0, health=1)
create_enemy(room1, path_enemy2,velocity=6, up_down_around=1, health=1)
create_enemy_with_shoot(room1, path_enemy3, velocity=2, up_down_around=3, health=1, frequency=5)

create_weapon(300,500,room1)

room1.set_enemies_in_room(3)

# Room2
room2 = rrooms[1]

# room2.add_multiple_sprites(path_green_boxes, little_boxes_right)
room2.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
room2.add_multiple_sprites(path_green_boxes, little_boxes_left)
room2.add_multiple_sprites(path_green_boxes, little_boxes_top)
room2.add_multiple_sprites(path_metal_violet_box, corner_boxes)
room2.add_multiple_sprites(path_blue_boxes, random_boxes[1])


create_enemy(room2, path_enemy1, velocity=2, up_down_around=0, health=1)
create_enemy(room2, path_enemy2,velocity=6, up_down_around=1, health=1)
create_enemy_with_shoot(room2, path_enemy3, velocity=2, up_down_around=3, health=1, frequency=5)

create_health(100, 100, room2)

room2.set_enemies_in_room(3)

#Room3
room3 = rrooms[2]

room3.add_multiple_sprites(path_cyan_boxes, little_boxes_right)
# room3.add_multiple_sprites(path_cyan_boxes, little_boxes_bottom)
room3.add_multiple_sprites(path_cyan_boxes, little_boxes_left)
room3.add_multiple_sprites(path_cyan_boxes, little_boxes_top)
room3.add_multiple_sprites(path_metal_brown_box, corner_boxes)
room3.add_multiple_sprites(path_blue_boxes, random_boxes[2])

create_enemy(room3, path_enemy4, velocity=2, up_down_around=0, health=1)
create_enemy(room3, path_enemy4,velocity=6, up_down_around=1, health=1)
create_enemy_with_shoot(room3, path_enemy5, velocity=2, up_down_around=3, health=1, frequency=5)

room3.set_enemies_in_room(3)

#Room4
room4 = rrooms[3]

room4.add_multiple_sprites(path_red_boxes, little_boxes_right)
# room4.add_multiple_sprites(path_red_boxes, little_boxes_bottom)
room4.add_multiple_sprites(path_red_boxes, little_boxes_left)
room4.add_multiple_sprites(path_red_boxes, little_boxes_top)
room4.add_multiple_sprites(path_metal_red_box, corner_boxes)
room4.add_multiple_sprites(path_blue_boxes, random_boxes[3])

create_enemy(room4, path_enemy5, velocity=2, up_down_around=0, health=1)
create_enemy(room4, path_enemy6,velocity=6, up_down_around=1, health=1)
create_enemy_with_shoot(room4, path_enemy6, velocity=2, up_down_around=3, health=1, frequency=5)

create_weapon(100,100,room4)

room4.set_enemies_in_room(3)

#Room5
room5 = rrooms[4]

room5.add_multiple_sprites(path_pink_boxes, little_boxes_right)
room5.add_multiple_sprites(path_pink_boxes, little_boxes_bottom)
# room5.add_multiple_sprites(path_pink_boxes, little_boxes_left)
room5.add_multiple_sprites(path_pink_boxes, little_boxes_top)
room5.add_multiple_sprites(path_metal_black_box, corner_boxes)
room5.add_multiple_sprites(path_blue_boxes, random_boxes[4])

create_enemy(room5, path_enemy6, velocity=2, up_down_around=0, health=1)
create_enemy(room5, path_enemy1,velocity=2, up_down_around=1, health=1)
create_enemy(room5, path_enemy1,velocity=2, up_down_around=1, health=1)
create_enemy(room5, path_enemy4,velocity=6, up_down_around=2, health=20)
create_enemy(room5, path_enemy4,velocity=6, up_down_around=3, health=10)
create_enemy(room5, path_enemy2,velocity=6, up_down_around=3, health=10)
create_enemy_with_shoot(room5, path_enemy7, velocity=2, up_down_around=3, health=10, frequency=5)
create_enemy_with_shoot(room5, path_enemy7, velocity=2, up_down_around=2, health=30, frequency=10)

room5.set_enemies_in_room(8)


#Room6
room6 = rrooms[5]

room6.add_multiple_sprites(path_oranje_boxes, little_boxes_right)
room6.add_multiple_sprites(path_oranje_boxes, little_boxes_bottom)
# room6.add_multiple_sprites(path_oranje_boxes, little_boxes_left)
room6.add_multiple_sprites(path_oranje_boxes, little_boxes_top)
room6.add_multiple_sprites(path_metal_cyan_box, corner_boxes)
room6.add_multiple_sprites(path_blue_boxes, random_boxes[5])

create_enemy(room6, path_enemy1, velocity=2, up_down_around=0, health=1)
create_enemy(room6, path_enemy2,velocity=2, up_down_around=1, health=1)
create_enemy(room6, path_enemy7,velocity=2, up_down_around=1, health=1)
create_enemy(room6, path_enemy3,velocity=6, up_down_around=2, health=20)
create_enemy(room6, path_enemy7,velocity=6, up_down_around=3, health=10)
create_enemy(room6, path_enemy6,velocity=6, up_down_around=3, health=10)
create_enemy_with_shoot(room6, path_enemy7, velocity=2, up_down_around=3, health=10, frequency=5)
create_enemy_with_shoot(room6, path_enemy3, velocity=2, up_down_around=2, health=30, frequency=10)
create_enemy_with_shoot(room6, path_enemy7, velocity=2, up_down_around=3, health=30, frequency=10)

room6.set_enemies_in_room(9)

#Room7
room7 = rrooms[6]

room7.add_multiple_sprites(path_cyan_boxes, little_boxes_right)
room7.add_multiple_sprites(path_cyan_boxes, little_boxes_bottom)
room7.add_multiple_sprites(path_cyan_boxes, little_boxes_left)
# room7.add_multiple_sprites(path_cyan_boxes, little_boxes_top)
room7.add_multiple_sprites(path_metal_red_box2, corner_boxes)
room7.add_multiple_sprites(path_blue_boxes, random_boxes[6])

create_enemy(room7, path_enemy7, velocity=3, up_down_around=0, health=1)
create_enemy(room7, path_enemy7,velocity=3, up_down_around=1, health=1)
create_enemy(room7, path_enemy5,velocity=3, up_down_around=1, health=1)
create_enemy(room7, path_enemy6,velocity=7, up_down_around=2, health=20)
create_enemy(room7, path_enemy8,velocity=8, up_down_around=3, health=10)
create_enemy(room7, path_enemy8,velocity=9, up_down_around=3, health=10)
create_enemy_with_shoot(room7, path_enemy2, velocity=3, up_down_around=3, health=10, frequency=5)
create_enemy_with_shoot(room7, path_enemy1, velocity=3, up_down_around=2, health=40, frequency=10)
create_enemy_with_shoot(room7, path_enemy8, velocity=3, up_down_around=3, health=40, frequency=10)

create_weapon(250,300,room7)


room7.set_enemies_in_room(9)

#Room8
room8 = rrooms[7]

room8.add_multiple_sprites(path_blue_boxes, little_boxes_right)
# room8.add_multiple_sprites(path_blue_boxes, little_boxes_bottom)
room8.add_multiple_sprites(path_blue_boxes, little_boxes_left)
room8.add_multiple_sprites(path_blue_boxes, little_boxes_top)
room8.add_multiple_sprites(path_metal_brown_box, corner_boxes)
room8.add_multiple_sprites(path_blue_boxes, random_boxes[7])

create_enemy(room8, path_enemy8, velocity=3, up_down_around=0, health=1)
create_enemy(room8, path_enemy8, velocity=3, up_down_around=0, health=1)
create_enemy(room8, path_enemy1, velocity=3, up_down_around=0, health=1)
create_enemy(room8, path_enemy1,velocity=3, up_down_around=1, health=1)
create_enemy(room8, path_enemy1,velocity=3, up_down_around=1, health=1)
create_enemy(room8, path_enemy6,velocity=7, up_down_around=2, health=20)
create_enemy(room8, path_enemy6,velocity=8, up_down_around=3, health=10)
create_enemy(room8, path_enemy6,velocity=9, up_down_around=3, health=10)
create_enemy_with_shoot(room8, path_enemy8, velocity=3, up_down_around=3, health=10, frequency=5)
create_enemy_with_shoot(room8, path_enemy8, velocity=3, up_down_around=2, health=40, frequency=10)

create_health(500, 400, room8)

room8.set_enemies_in_room(10)

#Room9
room9 = rrooms[8]

room9.add_multiple_sprites(path_red_boxes, little_boxes_right)
room9.add_multiple_sprites(path_red_boxes, little_boxes_bottom)
# room9.add_multiple_sprites(path_red_boxes, little_boxes_left)
room9.add_multiple_sprites(path_red_boxes, little_boxes_top)
room9.add_multiple_sprites(path_metal_red_box2, corner_boxes)
room9.add_multiple_sprites(path_blue_boxes, random_boxes[8])

create_enemy(room9, path_enemy6, velocity=3, up_down_around=0, health=1)
create_enemy(room9, path_enemy8, velocity=3, up_down_around=0, health=1)
create_enemy(room9, path_enemy5, velocity=3, up_down_around=0, health=1)
create_enemy(room9, path_enemy1,velocity=3, up_down_around=1, health=1)
create_enemy(room9, path_enemy5,velocity=3, up_down_around=1, health=1)
create_enemy(room9, path_enemy6,velocity=7, up_down_around=2, health=20)
create_enemy(room9, path_enemy7,velocity=8, up_down_around=3, health=10)
create_enemy(room9, path_enemy4,velocity=9, up_down_around=3, health=10)
create_enemy_with_shoot(room9, path_enemy9, velocity=3, up_down_around=3, health=10, frequency=5)
create_enemy_with_shoot(room9, path_enemy8, velocity=3, up_down_around=2, health=40, frequency=10)
create_enemy_with_shoot(room9, path_enemy9, velocity=3, up_down_around=3, health=40, frequency=10)

create_weapon(500,500,room9)
create_health(100, 500, room9)

room9.set_enemies_in_room(11)

#Room10
room10 = rrooms[9]

room10.add_multiple_sprites(path_green_boxes, little_boxes_right)
#room10.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
room10.add_multiple_sprites(path_green_boxes, little_boxes_left)
room10.add_multiple_sprites(path_green_boxes, little_boxes_top)
room10.add_multiple_sprites(path_metal_red_box, corner_boxes)

create_enemy_with_shoot(room10, path_enemy11, velocity=10, up_down_around=0, health=100, frequency=6)
create_enemy(room10, path_enemy11, velocity=5, up_down_around=0, health=100)
create_enemy_with_shoot(room10, path_enemy11, velocity=7, up_down_around=3, health=100, frequency=6)
create_enemy(room10, path_enemy11, velocity=15, up_down_around=2, health=100)
create_enemy_with_shoot(room10, path_enemy11, velocity=2, up_down_around=2, health=100, frequency=6)
create_enemy(room10, path_enemy11, velocity=3, up_down_around=3, health=100)
create_enemy_with_shoot(room10, path_enemy11, velocity=8, up_down_around=1, health=100, frequency=6)
create_enemy(room10, path_enemy11, velocity=9, up_down_around=3, health=100)
create_enemy_with_shoot(room10, path_enemy11, velocity=3, up_down_around=2, health=100, frequency=9)
create_enemy_with_shoot(room10, path_enemy11, velocity=1, up_down_around=3, health=100, frequency=9)
create_enemy(room10, path_enemy11, velocity=11, up_down_around=3, health=100)
create_enemy_with_shoot(room10, path_enemy11, velocity=12, up_down_around=1, health=100, frequency=9)
create_enemy_with_shoot(room10, path_enemy11, velocity=13, up_down_around=3, health=100, frequency=13)
create_enemy_with_shoot(room10, path_enemy11, velocity=14, up_down_around=3, health=100, frequency=13)
create_enemy(room10, path_enemy11, velocity=10, up_down_around=3, health=100)
create_enemy_with_shoot(room10, path_enemy11, velocity=4, up_down_around=0, health=100, frequency=13)
create_enemy(room10, path_enemy11, velocity=5, up_down_around=3, health=100)
create_enemy_with_shoot(room10, path_enemy11, velocity=6, up_down_around=0, health=100, frequency=13)
create_enemy(room10, path_enemy11, velocity=7, up_down_around=3, health=100)
create_enemy_with_shoot(room10, path_enemy11, velocity=8, up_down_around=3, health=100, frequency=13)
create_enemy_with_shoot(room10, path_enemy10, velocity=15, up_down_around=0, health=500, frequency=20)

room10.set_enemies_in_room(21)



rooms = {i:RoomLinks(i) for i in range (10)}

rooms[0].link_room('left',rooms[1])
rooms[1].link_room('up',rooms[2])
rooms[2].link_room('up',rooms[3])
rooms[2].link_room('right',rooms[4])
rooms[4].link_room('right',rooms[5])
rooms[5].link_room('down',rooms[6])
rooms[4].link_room('up',rooms[7])
rooms[7].link_room('right',rooms[8])
rooms[7].link_room('up',rooms[9])