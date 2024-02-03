# import the arcade library
import arcade

# Open a window
# Set window title to "Drawing"
# Set dimensions of window
arcade.open_window(800, 600, "Drawing")

# Set the background color
arcade.set_background_color(arcade.color.AZURE)

# Get ready to draw
arcade.start_render()

# Draw the sand
arcade.draw_lrtb_rectangle_filled(0, 800, 300, 0, arcade.color.SAND)

# ---Draw a house---

# Bottom of house
arcade.draw_lrtb_rectangle_filled(50, 250, 220, 20, arcade.color.BROWN)

# Draw top of house
arcade.draw_triangle_filled(50, 220, 250, 220, 150, 320, arcade.color.KOBE)

# Draw Door
arcade.draw_lrtb_rectangle_filled(70, 95, 70, 20, arcade.color.FOREST_GREEN)

# Draw Window
arcade.draw_circle_filled(125, 125, 20, arcade.color.LIGHT_CARMINE_PINK)

# Draw border between top and bottom of house
arcade.draw_line(50, 220, 250, 220, arcade.color.WHITE)

# ---Finish Drawing---
arcade.finish_render()

# Keep window open until closed
arcade.run()
