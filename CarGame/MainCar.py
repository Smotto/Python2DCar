import pyglet
import math
from pyglet.window import key, FPSDisplay
from GameObject import GameObject, preload_image, center_image
from pyglet.sprite import Sprite
from pyglet.gl import *
from pygame import Vector2
from CircleLines import *


class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        # Refers to pyglet.window.Window
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
        self.car_max_velocity = 300
        # Initial sprite position, rotation, image
        self.car = GameObject(135, 425, self.rotation, sprite_car)
        self.car_vector_position = Vector2(self.car.position_x, self.car.position_y)
        self.car_vector_velocity = Vector2(0, 0)

        # Two New Objects that are Circles.
        self.circle = CircleLines(200, 690, 288)
        self.circle2 = CircleLines2(200, 581, 227)

        # Death Counter
        self.death_counter = 0

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

    # Draw on Window
    def on_draw(self):
        death_label = pyglet.text.Label(str(self.death_counter),
                                             font_name='Times New Roman',
                                             font_size=36,
                                             x=1500, y=800,
                                             anchor_x='center', anchor_y='center')
        # Check Collisions and position
        self.check_position()
        # Step 0: Clear the area.
        self.clear()
        # Step 1: Draw the background before the car.
        self.car_background.draw()
        # Step 2: Draw the Sprite. from GameObject, there's a method called draw.
        self.car.draw()
        # Outer
        self.circle.draw()
        # Inner
        self.circle2.draw()
        # Step 3: Draw on display FPS
        self.fps_display.draw()
        # Step 4: Draw the death counter
        death_label.draw()

        print(self.death_counter)

    def update_car(self, dt):
        self.check_collision()
        self.car.update()
        self.car_acceleration = 50
        if self.forward:
            self.check_velocity()
            self.check_acceleration()
            self.change_velocity(self.car_acceleration, dt)
            self.change_position(dt)

        if not self.forward:
            self.check_velocity()
            self.check_acceleration()
            self.change_velocity_negative(self.car_acceleration, dt)
            self.change_position(dt)

        if self.left:
            self.car.rotation -= 2

        if self.right:
            self.car.rotation += 2

        if self.back:
            self.brake_car(self.car_acceleration, dt)

        self.check_rotation()

    def brake_car(self, acceleration, dt):
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

    def check_collision(self):

        # Pythagorean Theorem
        def get_distance(x1, y1, x2, y2):
            xDistance = x2 - x1
            yDistance = y2 - y1
            return math.floor(math.sqrt(math.pow(xDistance, 2) + math.pow(yDistance, 2)))

        # Reset Position and Velocity
        # Enumerates through two lists at the same time, and compares the positions through each sharing index.
        def reset_position_velocity(circleX, circleY):
            for i, number_x in enumerate(circleX):
                number_y = circleY[i]
                distance_from_wall = get_distance(self.car.position_x, self.car.position_y, number_x, number_y)

                # Check this number to see how well it works with AI
                if distance_from_wall < 7.0:
                    self.car_vector_position = [135, 450]
                    self.car_vector_velocity = [0, 0]
                    self.death_counter += .5

        reset_position_velocity(self.circle.vertices_x, self.circle.vertices_y)
        reset_position_velocity(self.circle2.vertices_x, self.circle2.vertices_y)

    def check_position(self):
        if self.car.position_x < 0:
            self.car.position_x = 0
        if self.car.position_x > 1600:
            self.car.position_x = 1600
        if self.car.position_y > 900:
            self.car.position_y = 900
        if self.car.position_y < 0:
            self.car.position_y = 0

    def change_velocity(self, acceleration, dt):
        self.car_vector_velocity += (acceleration * dt, 0)

    def change_velocity_negative(self, acceleration, dt):
        if self.car_vector_velocity != [0, 0]:
            self.car_vector_velocity -= (acceleration * dt, 0)

    def check_velocity(self):
        self.car_vector_velocity_x, self.car_vector_velocity_y = self.car_vector_velocity

        if self.car_vector_velocity_x < 0:
            self.car_vector_velocity_x = 0
        if self.car_vector_velocity_y < 0:
            self.car_vector_velocity_y = 0
        if self.car_vector_velocity_x > self.car_max_velocity:
            self.car_vector_velocity_x = self.car_max_velocity
        if self.car_vector_velocity_y > self.car_max_velocity:
            self.car_vector_velocity_y = self.car_max_velocity

        self.car_vector_velocity = Vector2(self.car_vector_velocity_x, self.car_vector_velocity_y)

    def check_rotation(self):
        # Reset rotation degrees so that it doesn't go to a billion.
        if self.car.rotation == 360 or self.car.rotation == -360:
            self.car.rotation = 0

    def update(self, dt):
        self.check_collision()
        # Update car in order of Delta Time
        self.update_car(dt)


if __name__ == "__main__":
    window = GameWindow(1600, 900, "Auto Car", resizable=False)
    # Make sure the clock is the same as the window's update, and the window's frame rate
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()
