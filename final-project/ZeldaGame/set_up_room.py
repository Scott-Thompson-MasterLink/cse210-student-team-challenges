from ZeldaGame.room import Room
from ZeldaGame.obstacles_lists import *
from ZeldaGame.enemy import Enemy
from ZeldaGame.scaling import SPRITE_SCALING
from ZeldaGame.paths import *
from ZeldaGame.room_links import RoomLinks

# # Room 1
# room1 = Room(path_room1)

# room1.add_multiple_sprites(path_blue_boxes, little_boxes_right)
# room1.add_multiple_sprites(path_blue_boxes, little_boxes_bottom)
# room1.add_multiple_sprites(path_blue_boxes, little_boxes_left)
# room1.add_multiple_sprites(path_blue_boxes, little_boxes_top)
# room1.add_multiple_sprites(path_metal_boxes, corner_boxes)

# enemy = Enemy(path_enemy1, SPRITE_SCALING,max_health=1, velocity=2)
# enemy2 = Enemy(path_enemy2, SPRITE_SCALING,max_health=2, velocity= 2.5, movement= 1)
# enemy2.position_enemy(100, 400)
# enemy.position_enemy(600, 150)

# room1.list_of_enemies.append(enemy)
# room1.list_of_enemies.append(enemy2)

# room1.set_enemies_in_room(2)

# # Room2
# room2 = Room(path_room2)

# room2.add_multiple_sprites(path_green_boxes, little_boxes_right)
# room2.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
# # room2.add_multiple_sprites(path_green_boxes, little_boxes_left)
# room2.add_multiple_sprites(path_green_boxes, little_boxes_top)
# room2.add_multiple_sprites(path_metal_violet_box, corner_boxes)

# enemy3 = Enemy(path_enemy3, SPRITE_SCALING,max_health=10)
# enemy4 = Enemy(path_enemy3, SPRITE_SCALING,max_health=10, movement= 1)
# enemy3.position_enemy(100, 150)
# enemy4.position_enemy(500, 500)

# room2.list_of_enemies.append(enemy3)
# room2.list_of_enemies.append(enemy4)

# room2.set_enemies_in_room(2)

# #Room3
# room3 = Room(path_room3)

# room3.add_multiple_sprites(path_green_boxes, little_boxes_right)
# room3.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
# # room3.add_multiple_sprites(path_green_boxes, little_boxes_left)
# room3.add_multiple_sprites(path_green_boxes, little_boxes_top)
# room3.add_multiple_sprites(path_metal_violet_box, corner_boxes)

# #Room4
# room4 = Room(path_room3)

# room4.add_multiple_sprites(path_green_boxes, little_boxes_right)
# room4.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
# # room4.add_multiple_sprites(path_green_boxes, little_boxes_left)
# room4.add_multiple_sprites(path_green_boxes, little_boxes_top)
# room4.add_multiple_sprites(path_metal_violet_box, corner_boxes)

# #Room5
# room5 = Room(path_room3)

# room5.add_multiple_sprites(path_green_boxes, little_boxes_right)
# room5.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
# # room5.add_multiple_sprites(path_green_boxes, little_boxes_left)
# room5.add_multiple_sprites(path_green_boxes, little_boxes_top)
# room5.add_multiple_sprites(path_metal_violet_box, corner_boxes)

# #Room6
# room6 = Room(path_room3)

# room6.add_multiple_sprites(path_green_boxes, little_boxes_right)
# room6.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
# # room6.add_multiple_sprites(path_green_boxes, little_boxes_left)
# room6.add_multiple_sprites(path_green_boxes, little_boxes_top)
# room6.add_multiple_sprites(path_metal_violet_box, corner_boxes)

# #Room7
# room7 = Room(path_room3)

# room7.add_multiple_sprites(path_green_boxes, little_boxes_right)
# room7.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
# # room7.add_multiple_sprites(path_green_boxes, little_boxes_left)
# room7.add_multiple_sprites(path_green_boxes, little_boxes_top)
# room7.add_multiple_sprites(path_metal_violet_box, corner_boxes)

# #Room8
# room8 = Room(path_room3)

# room8.add_multiple_sprites(path_green_boxes, little_boxes_right)
# room8.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
# # room8.add_multiple_sprites(path_green_boxes, little_boxes_left)
# room8.add_multiple_sprites(path_green_boxes, little_boxes_top)
# room8.add_multiple_sprites(path_metal_violet_box, corner_boxes)

# #Room9
# room9 = Room(path_room3)

# room9.add_multiple_sprites(path_green_boxes, little_boxes_right)
# room9.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
# # room9.add_multiple_sprites(path_green_boxes, little_boxes_left)
# room9.add_multiple_sprites(path_green_boxes, little_boxes_top)
# room9.add_multiple_sprites(path_metal_violet_box, corner_boxes)

# #Room10
# room10 = Room(path_room3)

# room10.add_multiple_sprites(path_green_boxes, little_boxes_right)
# room10.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
# # room10.add_multiple_sprites(path_green_boxes, little_boxes_left)
# room10.add_multiple_sprites(path_green_boxes, little_boxes_top)
# room10.add_multiple_sprites(path_metal_violet_box, corner_boxes)




# Room 1
# rrooms = [Room()]
rrooms = [Room(f"cse210-student-team-challenges/final-project/images/room{i%5+1}.png") for i in range(10)]
room1 = rrooms[0]
room1.add_multiple_sprites(path_blue_boxes, little_boxes_right)
room1.add_multiple_sprites(path_blue_boxes, little_boxes_bottom)
room1.add_multiple_sprites(path_blue_boxes, little_boxes_left)
room1.add_multiple_sprites(path_blue_boxes, little_boxes_top)
room1.add_multiple_sprites(path_metal_boxes, corner_boxes)

enemy = Enemy(path_enemy1, SPRITE_SCALING,max_health=1, velocity=2)
enemy2 = Enemy(path_enemy2, SPRITE_SCALING,max_health=2, velocity= 2.5, movement= 1)
enemy2.position_enemy(100, 400)
enemy.position_enemy(600, 150)

room1.list_of_enemies.append(enemy)
room1.list_of_enemies.append(enemy2)

room1.set_enemies_in_room(2)

# Room2
room2 = rrooms[1]

# room2.add_multiple_sprites(path_green_boxes, little_boxes_right)
room2.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
room2.add_multiple_sprites(path_green_boxes, little_boxes_left)
room2.add_multiple_sprites(path_green_boxes, little_boxes_top)
room2.add_multiple_sprites(path_metal_violet_box, corner_boxes)

enemy3 = Enemy(path_enemy3, SPRITE_SCALING,max_health=10)
enemy4 = Enemy(path_enemy3, SPRITE_SCALING,max_health=10, movement= 1)
enemy3.position_enemy(100, 150)
enemy4.position_enemy(500, 500)

room2.list_of_enemies.append(enemy3)
room2.list_of_enemies.append(enemy4)

room2.set_enemies_in_room(2)


for room in rrooms[2:-1]:
    enemy3 = Enemy(path_enemy3, SPRITE_SCALING,max_health=10, shoot= True, shot_frequency=4)
    enemy4 = Enemy(path_enemy3, SPRITE_SCALING,max_health=10, movement= 1, shoot=True, shot_frequency=5)
    enemy3.position_enemy(100, 150)
    enemy4.position_enemy(500, 500)

    room.list_of_enemies.append(enemy3)
    room.list_of_enemies.append(enemy4)

    room.set_enemies_in_room(2)

#Room3
room3 = rrooms[2]

room3.add_multiple_sprites(path_green_boxes, little_boxes_right)
# room3.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
room3.add_multiple_sprites(path_green_boxes, little_boxes_left)
room3.add_multiple_sprites(path_green_boxes, little_boxes_top)
room3.add_multiple_sprites(path_metal_violet_box, corner_boxes)

#Room4
room4 = rrooms[3]

room4.add_multiple_sprites(path_green_boxes, little_boxes_right)
# room4.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
room4.add_multiple_sprites(path_green_boxes, little_boxes_left)
room4.add_multiple_sprites(path_green_boxes, little_boxes_top)
room4.add_multiple_sprites(path_metal_violet_box, corner_boxes)

#Room5
room5 = rrooms[4]

room5.add_multiple_sprites(path_green_boxes, little_boxes_right)
room5.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
# room5.add_multiple_sprites(path_green_boxes, little_boxes_left)
room5.add_multiple_sprites(path_green_boxes, little_boxes_top)
room5.add_multiple_sprites(path_metal_violet_box, corner_boxes)

#Room6
room6 = rrooms[5]

room6.add_multiple_sprites(path_green_boxes, little_boxes_right)
room6.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
# room6.add_multiple_sprites(path_green_boxes, little_boxes_left)
room6.add_multiple_sprites(path_green_boxes, little_boxes_top)
room6.add_multiple_sprites(path_metal_violet_box, corner_boxes)

#Room7
room7 = rrooms[6]

room7.add_multiple_sprites(path_green_boxes, little_boxes_right)
room7.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
room7.add_multiple_sprites(path_green_boxes, little_boxes_left)
# room7.add_multiple_sprites(path_green_boxes, little_boxes_top)
room7.add_multiple_sprites(path_metal_violet_box, corner_boxes)

#Room8
room8 = rrooms[7]

room8.add_multiple_sprites(path_green_boxes, little_boxes_right)
# room8.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
room8.add_multiple_sprites(path_green_boxes, little_boxes_left)
room8.add_multiple_sprites(path_green_boxes, little_boxes_top)
room8.add_multiple_sprites(path_metal_violet_box, corner_boxes)

#Room9
room9 = rrooms[8]

room9.add_multiple_sprites(path_green_boxes, little_boxes_right)
room9.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
# room9.add_multiple_sprites(path_green_boxes, little_boxes_left)
room9.add_multiple_sprites(path_green_boxes, little_boxes_top)
room9.add_multiple_sprites(path_metal_violet_box, corner_boxes)

#Room10
room10 = rrooms[9]

room10.add_multiple_sprites(path_green_boxes, little_boxes_right)
# room10.add_multiple_sprites(path_green_boxes, little_boxes_bottom)
room10.add_multiple_sprites(path_green_boxes, little_boxes_left)
room10.add_multiple_sprites(path_green_boxes, little_boxes_top)
room10.add_multiple_sprites(path_metal_violet_box, corner_boxes)








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