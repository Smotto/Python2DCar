import pyglet
from pyglet.window import key, FPSDisplay
from GameObject import GameObject, preload_image, center_image
from pyglet.sprite import Sprite
import math

class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

            # set the window's location at a certain point, x-pos, y-pos
        self.set_location(400, 100)
            # set the window's frame-rate, this is 60.0 fps
        self.frame_rate = 1 / 60.0
            # Screen or Window is self.
        self.fps_display = FPSDisplay(self)
            # Make fps display bigger.
        self.fps_display.label.font_size = 25

        # Stand Still For Now
        self.right = False
        self.left = False
        self.forward = False
        self.back = False

        # Set initial speed of car, we should do an acceleration to a certain point of velocity.
        self.car_velocity_y = 0
        self.car_velocity_x = 0

        self.car_max_acceleration = 300
        self.car_max_steering = 30

        # Military start from north
        self.rotation = 0
        self.car_steering = 0

        self.car_acceleration = 0

        # Preload the background
        self.car_background = Sprite(preload_image('CarGameBackground.jpg'))

        # Preload the car
        car = preload_image('carFIXED.png')
        center_image(car)
        sprite_car = pyglet.sprite.Sprite(car)
        self.car = GameObject(135, 425, self.rotation, sprite_car)
        # Oh god.


    def on_draw(self):
        self.clear()

        # Step 1: Draw the background before the car.
        self.car_background.draw()

        # Step 2: Draw the Sprite. from GameObject, there's a method called draw.
        self.car.draw()

        # Step 3: Draw on display FPS
        self.fps_display.draw()

        # IF key is pressed, change velocity
    def on_key_press(self, symbol, modifiers):
        # Change velocity x-position 300
        if symbol == key.RIGHT:
            self.right = True
        # Change velocity x-position -300
        if symbol == key.LEFT:
            self.left = True
        if symbol == key.UP:
            self.forward = True
        if symbol == key.DOWN:
            self.back = True

        # Exit Window/Application
        if symbol == key.ESCAPE:
            pyglet.app.exit()


        # If key is released, set velocity to 0. This works for right, and left
    def on_key_release(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.right = False
        if symbol == key.LEFT:
            self.left = False
        if symbol == key.UP:
            self.forward = False
        if symbol == key.DOWN:
            self.back = False

    def update_car(self, dt):
        # Update the car's position
        self.car.update()

        if self.forward:
            self.car_acceleration = 50

            # Increase velocity
            self.car_velocity_x += self.car_acceleration * dt
            # Increase position based on velocity
            self.car.position_x += self.car_velocity_x * dt

            if self.car_acceleration >= self.car_max_acceleration:
                self.car_acceleration = self.car_max_acceleration
            if self.car_acceleration <= 0:
                self.car_acceleration = 0
            if self.car_velocity_x <= 0:
                self.car_velocity_x = 0


        if not self.forward:

            # Decrease Velocity
            self.car_velocity_x -= self.car_acceleration * dt
            # Increase Position Based on velocity
            self.car.position_x += self.car_velocity_x * dt

            if self.car_acceleration >= self.car_max_acceleration:
                self.car_acceleration = self.car_max_acceleration
            if self.car_acceleration <= 0:
                self.car_acceleration = 0
            if self.car_velocity_x <= 0:
                self.car_velocity_x = 0


        if self.right:
            self.car.rotation += 1
            # When the car is pointing to the right.
            if self.car.rotation >= 90:
                self.car.rotation = 90

        if self.left:
            self.car.rotation -= 1
            if self.car.rotation <= -90:
                self.car.rotation = -90

        # Reset rotation degrees so that it doesn't go to a billion.
        if self.car.rotation == 360 or self.car.rotation == -360:
            self.car.rotation = 0


        print(self.car_acceleration)
        print(self.car_velocity_x)
        print(self.car.position_x)


    def update(self, dt):
        # Update car in order of Delta Time
        self.update_car(dt)

if __name__ == "__main__":
    window = GameWindow(1600, 900, "Auto Car", resizable = False)
    # Make sure the clock is the same as the window's update, and the window's frame rate
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()
