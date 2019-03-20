import pyglet
from GameObject import GameObject, preload_image
from pyglet.window import key, FPSDisplay
from pyglet.sprite import Sprite


# Create class for window
# The game window inherits from the pyglet.window.Window
class GameWindow(pyglet.window.Window):
    # args and kwargs are conventions
    # args are used when there's a tuple of data or a whole bunch of data in a list, accepts all
    # the __init__ method is a constructor !
    def __init__(self, *args, **kwargs):
        # super calls pyglet.window.Window constructor !
        super().__init__(*args, **kwargs)

        # set the window's location at a certain point, x-pos, y-pos
        self.set_location(400, 100)
        # set the window's frame-rate, this is 60.0 fps
        self.frame_rate = 1 / 60.0
        # Screen or Window is self.
        self.fps_display = FPSDisplay(self)
        # Make fps display bigger.
        self.fps_display.label.font_size = 50

        self.right = False
        self.left = False
        self.player_speed = 300

        # Auto Shooting
        self.fire = False
        self.player_fire_rate = 0

        # Preload the image so that there is no delay. spr means sprite
        player_spr = Sprite(preload_image('PlayerShip.png'))

        # Create the player as a game object, with parameters of x-position, y-position, and the image name
        self.player = GameObject(500, 100, player_spr)

        self.player_laser = preload_image('laser.png')
        # Empty list of lasers
        self.player_laser_list = []

        # Create the background
        # self.space = GameObject(0, 0, 'space.jpg')

        # Scroll downwards variable velocity
        # self.space.vely = -50

        self.space_list = []
        self.space_img = preload_image('space.jpg')

        # Loop for Background to never be black.
        for i in range(2):
            # Height of the background is 1200
            # 0 * 1200 is to reset the position
            self.space_list.append(GameObject(0, i*1200, Sprite(self.space_img)))


    # IF key is pressed, change velocity
    def on_key_press(self, symbol, modifiers):
        # Change velocity x-position 300
        if symbol == key.RIGHT:
            self.right = True
        # Change velocity x-position -300
        if symbol == key.LEFT:
            self.left = True
        if symbol == key.ESCAPE:
            pyglet.app.exit()
        if symbol == key.SPACE:
            self.fire = True

    # If key is released, set velocity to 0. This works for right, and left
    def on_key_release(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.right = False
        if symbol == key.LEFT:
            self.left = False
        if symbol == key.SPACE:
            self.fire = False


    # overriding draw method
    def on_draw(self):
        self.clear()

        # Draw space.
        for space in self.space_list:
            space.draw()


        # Draw the background before the player.
        # self.space.draw()


        # Draw the Sprite. from GameObject, there's a method called draw.
        self.player.draw()

        for laser in self.player_laser_list:
            laser.draw()

        # Lets draw FPS
        self.fps_display.draw()

    def player_fire(self, dt):
        self.player_fire_rate -= dt
        # Limit fire rate.
        if self.player_fire_rate <= 0:
            self.player_laser_list.append(
                GameObject(self.player.posx + 32, self.player.posy + 96, Sprite(self.player_laser)))
            self.player_fire_rate += 0.2

    def update_space(self, dt):
        # Update every object in space_list to delta time
        for space in self.space_list:
            space.update()
            space.posy -= 50 * dt

            # If game object space is less than or equal to -1300,
            # The image gets removed from the space list
            # And then new one appears a little bit below 1100 on the y-axis :^(
            # That's why it will glitch a bit if we loop through loading image and converting to a sprite

            if space.posy <= -1300:
                self.space_list.remove(space)
                # Changed the image to a pre-loaded image.
                self.space_list.append(GameObject(0, 1100, Sprite(self.space_img)))


    def update_player(self, dt):
        # Update the player's position to delta-time
        self.player.update()
        if self.right and self.player.posx < 1000 - self.player.width:
            self.player.posx += self.player_speed * dt

            # Check left side of screen
        if self.left and self.player.posx > 100:
            self.player.posx -= self.player_speed * dt


    def update_player_laser(self, dt):
        for laser in self.player_laser_list:
            laser.update()
            laser.posy += 400* dt
            # Remove lasers that exit the screen + 50 for good measure
            if laser.posy > self.height + 50:
                self.player_laser_list.remove(laser)



    # overriding update method
    # dt is from the window updating, and it is in relation to time.
    def update(self, dt):
        # Use method update_space to get a loop of the background.
        self.update_player(dt)
        if self.fire:
            self.player_fire(dt)
        self.update_space(dt)
        self.update_player_laser(dt)

        # Update the space background to delta-time
        # self.space.update(dt)



if __name__ == "__main__":
    window = GameWindow(1200, 900, "Space Game", resizable=False)
    # Make sure the clock is the same as the window's update, and the window's frame rate
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()
