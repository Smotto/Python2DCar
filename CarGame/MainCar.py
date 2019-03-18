import pyglet
import math
from pyglet.window import key, FPSDisplay
from GameObject import GameObject, preload_image, center_image
from pyglet.sprite import Sprite
from pyglet.gl import *
from pygame import Vector2

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

        # Preload the background
        self.car_background = Sprite(preload_image('CarGameBackground.jpg'))
        # Preload the car
        car = preload_image('carFIXED.png')
        # Center the car's rotation at its center.
        center_image(car)
        # Transfer car to a sprite
        sprite_car = pyglet.sprite.Sprite(car)

        self.rotation = 0
        self.car_acceleration = 0
        self.car_max_acceleration = 300


        # Initial sprite position, rotation, image
        self.car = GameObject(125, 425, self.rotation, sprite_car)

        self.car_vector_position = Vector2(self.car.position_x, self.car.position_y)
        self.car_vector_velocity = Vector2(0, 0)

        # Keys
        self.right = False
        self.left = False
        self.forward = False
        self.back = False

     # KEY PRESS
    def on_key_press(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.right = True
        if symbol == key.LEFT:
            self.left = True
        if symbol == key.UP:
            self.forward = True
        if symbol == key.DOWN:
            self.back = True
        # Exit Window/Application
        if symbol == key.ESCAPE:
            pyglet.app.exit()

        # KEY RELEASE
    def on_key_release(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.right = False
        if symbol == key.LEFT:
            self.left = False
        if symbol == key.UP:
            self.forward = False
        if symbol == key.DOWN:
            self.back = False

    def on_draw(self):
        # Step 0: Clear the area.
        self.clear()
        # Step 1: Draw the background before the car.
        self.car_background.draw()
        # Step 2: Draw the Sprite. from GameObject, there's a method called draw.
        self.car.draw()
        # Step 3: Draw on display FPS
        self.fps_display.draw()

    def update_car(self, dt):
        self.car.update()

        self.car_acceleration = 50

        if self.forward:
            self.change_velocity(self.car_acceleration, dt)
            self.check_velocity()
            self.change_position(dt)
            self.check_acceleration()

        if not self.forward:
            self.change_velocity_negative(self.car_acceleration, dt)
            self.check_velocity()
            self.change_position(dt)
            self.check_acceleration()

        if self.left:
            self.car.rotation -= 2

        if self.right:
            self.car.rotation += 2

        if self.back:
            self.brake_car(self.car_acceleration, dt)

        self.check_rotation()

        print(self.car_vector_position)
        print(self.car_vector_velocity)

    def brake_car(self,acceleration, dt):
        self.car_vector_velocity -= (acceleration * dt * 5, 0)

    def check_acceleration(self):
        if self.car_acceleration >= self.car_max_acceleration:
            self.car_acceleration = self.car_max_acceleration
        if self.car_acceleration <= 0:
            self.car_acceleration = 0

    def change_position(self, dt):
        # Figure out what is going on with the math here.
        self.car_vector_position += self.car_vector_velocity.rotate(-self.car.rotation) * dt
        self.car.position_x, self.car.position_y = self.car_vector_position

    def change_velocity(self, acceleration, dt):
        self.car_vector_velocity += (acceleration * dt, 0)

    def change_velocity_negative(self, acceleration, dt):
        self.car_vector_velocity -= (acceleration * dt, 0)

    def check_velocity(self):
        self.car_vector_velocity_x, self.car_vector_velocity_y = self.car_vector_velocity

        if self.car_vector_velocity_x < 0:
            self.car_vector_velocity_x = 0
        if self.car_vector_velocity_y < 0:
            self.car_vector_velocity_y = 0

        self.car_vector_velocity = Vector2(self.car_vector_velocity_x, self.car_vector_velocity_y)
        pass

    def check_rotation(self):
        # Reset rotation degrees so that it doesn't go to a billion.
        if self.car.rotation == 360 or self.car.rotation == -360:
            self.car.rotation = 0

    def update(self, dt):
        # Update car in order of Delta Time
         self.update_car(dt)

if __name__ == "__main__":
    window = GameWindow(1600, 900, "Auto Car", resizable = False)
    # Make sure the clock is the same as the window's update, and the window's frame rate
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()
