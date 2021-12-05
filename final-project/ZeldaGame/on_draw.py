import arcade

class Draw(arcade.Window):

    def __init__(self, *args):
        self.__list_to_draw = args

    def on_draw(self):

        for i in self.__list_to_draw:
            for j in i:
                j.draw()
