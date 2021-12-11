import arcade
import random

class RandomCoordinates:
    
    def gen_ran_coor(number):
        coordinates = []
        for i in range(number):
            x_coordinate = random.randint(100, 700)
            y_coordinate = random.randint(100, 500)
            coordinate = [x_coordinate,y_coordinate]

            coordinates.append(coordinate)

        return coordinates


# randomcoordinates = RandomCoordinates.gen_ran_coor(5)

# print(randomcoordinates)