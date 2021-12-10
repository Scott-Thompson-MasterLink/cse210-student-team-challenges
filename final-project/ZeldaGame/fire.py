from abc import ABC, abstractmethod

class Fire(ABC):

    def __init__(self):
        self.velocity = 500

    @abstractmethod
    def shoot(self):
        pass

class Shooter:

    def __init__(self, weapon):
        self.__weapon = weapon

    def do_shoot(self, player, artillery, artillery_list, all_sprites):
        result = self.__weapon.shoot(player, artillery, artillery_list, all_sprites)
        return result


class ShootUp(Fire):

    def __init__(self):
        super().__init__()

    def shoot(self, player, artillery, artillery_list, all_sprites):
        artillery.center_x = player.center_x
        artillery.center_y = player.center_y - 5
        artillery.change_y = self.velocity
        artillery.change_angle = 90

        artillery_list.append(artillery)
        all_sprites.append(artillery)

class ShootDown(Fire):

    def __init__(self):
        super().__init__()

    def shoot(self, player, artillery, artillery_list, all_sprites):
    
        artillery.center_x = player.center_x
        artillery.center_y = player.center_y - 5
        artillery.change_y = -self.velocity
        artillery.change_angle = 90

        artillery_list.append(artillery)
        all_sprites.append(artillery)

class ShootLeft(Fire):

    def __init__(self):
        super().__init__()

    def shoot(self, player, artillery, artillery_list, all_sprites):
        artillery.center_x = player.center_x
        artillery.center_y = player.center_y - 5
        artillery.change_x = -self.velocity
        artillery.change_angle = 180

        artillery_list.append(artillery)
        all_sprites.append(artillery)

class ShootRight(Fire):

    def __init__(self):
        super().__init__()
    
    def shoot(self, player, artillery, artillery_list, all_sprites):
        artillery.center_x = player.center_x
        artillery.center_y = player.center_y - 5
        artillery.velocity = (self.velocity, 0)

        artillery_list.append(artillery)
        all_sprites.append(artillery)