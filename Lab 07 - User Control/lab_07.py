""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


class Player2:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take parameters and make them instance variables
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        self.angle = 0
        self.bounce_sound = arcade.load_sound("bounce.wav")
        self.bounce_sound_player = None

    def draw(self):
        """Draw Player2 with instance variables we have"""
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
        arcade.draw_rectangle_filled(self.position_x, self.position_y - (2 * self.radius), (2 * self.radius), (2 * self.radius), self.color, self.angle)

    def update(self):
        # Move the player
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius
            if not self.bounce_sound_player or not self.bounce_sound_player.playing:
                self.bounce_sound_player = arcade.play_sound(self.bounce_sound)

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            if not self.bounce_sound_player or not self.bounce_sound_player.playing:
                self.bounce_sound_player = arcade.play_sound(self.bounce_sound)

        if self.position_y < (2 * self.radius):
            self.position_y = (2 * self.radius)
            if not self.bounce_sound_player or not self.bounce_sound_player.playing:
                self.bounce_sound_player = arcade.play_sound(self.bounce_sound)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            if not self.bounce_sound_player or not self.bounce_sound_player.playing:
                self.bounce_sound_player = arcade.play_sound(self.bounce_sound)


class Player:
    def __init__(self, position_x, position_y, radius, color):

        # Take parameters and make them instance variables
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """Draw the person with the instance variables we have"""
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
        arcade.draw_triangle_filled(self.position_x, self.position_y - self.radius, self.position_x - self.radius, self.position_y - (2 * self.radius), self.position_x + self.radius, self. position_y - (2 * self.radius), self.color)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # Create our person
        self.player = Player(50, 50, 15, arcade.color.RED)
        self.player2 = Player2(350, 350, 0, 0, 15, arcade.color.PURPLE)
        self.target_x = 0
        self.target_y = 0
        self.bounce_sound = arcade.load_sound("bounce.wav")
        self.bounce_sound_player = None
        self.chirp_sound = arcade.load_sound("chirp.wav")
        self.chirp_sound_player = None

    def update(self, delta_time):
        self.player2.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.player2.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player2.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player2.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player2.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player2.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player2.change_y = 0

    def on_draw(self):
        # Background of picture
        arcade.start_render()
        arcade.draw_rectangle_filled(400, 150, 800, 300, arcade.color.GREEN)
        arcade.draw_rectangle_filled(400, 450, 800, 300, arcade.color.BLUE)
        arcade.draw_circle_filled(750, 550, 45, arcade.color.YELLOW)
        self.player.draw()
        self.player2.draw()

        # Update x coordinate
        if self.player.position_x < self.target_x:
            self.player.position_x += 1

        elif self.player.position_x > self.target_x:
            self.player.position_x -= 1

        # Update y coordinate
        if self.player.position_y < self.target_y:
            self.player.position_y += 1

        elif self.player.position_y > self.target_y:
            self.player.position_y -= 1

    # Mouse press movement
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.target_x = x
            self.target_y = y
            # Make a sound when mouse is pressed, but make sure first sound finishes before second begins
            if not self.chirp_sound_player or not self.chirp_sound_player.playing:
                self.chirp_sound_player = arcade.play_sound(self.chirp_sound)


def main():
    window = MyGame()
    arcade.run()


main()
