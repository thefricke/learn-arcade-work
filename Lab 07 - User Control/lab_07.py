""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player:
    def __init__(self):


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

    def on_draw(self):
        # Background of picture
        arcade.start_render()
        arcade.draw_rectangle_filled(400, 150, 800, 300, arcade.color.GREEN)
        arcade.draw_rectangle_filled(400, 450, 800, 300, arcade.color.BLUE)
        arcade.draw_circle_filled(750, 550, 45, arcade.color.YELLOW)

        #


def main():
    window = MyGame()
    arcade.run()


main()
