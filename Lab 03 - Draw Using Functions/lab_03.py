# import the arcade library
import arcade


def draw_sand():
    """Draw the sand"""
    arcade.draw_lrtb_rectangle_filled(0, 800, 300, 0, arcade.color.SAND)


def draw_house(x, y):
    """Draw the house"""

    "Draw point for reference"
    arcade.draw_point(x, y, arcade.color.PURPLE, 5)

    "Outline for house"
    arcade.draw_lrtb_rectangle_filled(x - 50, x + 50, y + 50, y - 50, arcade.color.PINK_LACE)
    arcade.draw_triangle_filled(x - 50, y + 50, x + 50, y + 50, x, y + 100, arcade.color.WHITE)

    "Details of house"
    arcade.draw_lrtb_rectangle_filled(x - 10, x + 10, y - 10, y - 50, arcade.color.GREEN)
    arcade.draw_circle_filled(x - 20, y, 5, arcade.color.LIGHT_CARMINE_PINK)
    arcade.draw_circle_filled(x + 20, y, 5, arcade.color.LIGHT_CARMINE_PINK)
    arcade.draw_line(x - 50, y + 50, x + 50, y + 50, arcade.color.BRONZE, 1)


def main():
    # Open a window
    # Set window title to "Drawing"
    # Set dimensions of window
    arcade.open_window(800, 600, "Drawing With Functions")

    # Set the background color
    arcade.set_background_color(arcade.color.AZURE)

    # Get ready to draw
    arcade.start_render()

    draw_sand()
    draw_house(70, 25)
    draw_house(375, 25)

    # ---Finish Drawing---
    arcade.finish_render()

    # Keep window open until closed
    arcade.run()

# Call main function to run program
main()
