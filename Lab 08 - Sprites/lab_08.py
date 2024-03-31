""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_METEOR = 0.4
COIN_COUNT = 50
METEOR_COUNT = 30

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.meteor_list = None

        # Sounds
        self.pickup_sound = arcade.load_sound("pickup.wav")
        self.pickup_sound_player = None
        self.bad_sound = arcade.load_sound("bad.wav")
        self.bad_sound_player = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip1_orange.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            coin = arcade.Sprite(":resources:images/items/coinGold_ul.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Create the meteors
        for i in range(METEOR_COUNT):
            # Create meteor instance
            meteor = arcade.Sprite(":resources:images/space_shooter/meteorGrey_med2.png", SPRITE_SCALING_METEOR)

            # Position meteor
            meteor.center_x = random.randrange(SCREEN_WIDTH)
            meteor.center_y = random.randrange(SCREEN_HEIGHT)

            # Add meteor to the lists
            self.meteor_list.append(meteor)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.meteor_list.draw()
        self.player_list.draw()
        if len(self.coin_list) != 0:
            """Draw Everything"""

            self.coin_list.draw()

            # Put the text on the screen.
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        else:
            self.player_sprite.center_x = SCREEN_WIDTH/4
            self.player_sprite.center_y = SCREEN_HEIGHT/4
            arcade.draw_text("GAME OVER", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.SCARLET, 15)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        if len(self.coin_list) != 0:
            # Move the center of the player sprite to match the mouse x, y
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

        else:
            self.player_sprite.center_x = SCREEN_WIDTH / 4
            self.player_sprite.center_y = SCREEN_HEIGHT / 4

    def update(self, delta_time):
        """ Movement and game logic """

        # Coins and meteors moving
        for coin in self.coin_list:
            coin.center_x += 2
            coin.center_y += 2
            if coin.center_x > SCREEN_WIDTH:
                coin.center_x = 0
                coin.center_y = random.randint(30, SCREEN_HEIGHT - 30)
            if coin.center_y > SCREEN_HEIGHT:
                coin.center_y = 0
                coin.center_x = random.randint(30, SCREEN_WIDTH - 30)

        if len(self.coin_list) != 0:
            for meteor in self.meteor_list:
                meteor.center_x -= 1
                meteor.center_y -= 1
                if meteor.center_x < 0:
                    meteor.center_x = random.randrange(SCREEN_WIDTH + 20, SCREEN_WIDTH + 30)
                    meteor.center_y = random.randrange(SCREEN_HEIGHT)
                if meteor.center_y < 0:
                    meteor.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 30)
                    meteor.center_x = random.randrange(SCREEN_WIDTH)
        else:
            for meteor in self.meteor_list:
                meteor.center_x = meteor.center_x
                meteor.center_y = meteor.center_y
        # Call update on all sprites
        self.coin_list.update()
        self.meteor_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            self.pickup_sound_player = arcade.play_sound(self.pickup_sound)

        meteor_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.meteor_list)

        # Remove sprite and subtract from the score
        for meteor in meteor_hit_list:
            meteor.remove_from_sprite_lists()
            self.score -= 1
            self.bad_sound_player = arcade.play_sound(self.bad_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
