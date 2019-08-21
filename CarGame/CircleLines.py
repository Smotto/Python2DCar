from pyglet.gl import *
import pyglet
from math import *

class CircleLines:
    #Individual Instances of CircleLines
    def __init__(self, num_points, width, height):
        self.vertices = []
        self.vertices_x = []
        self.vertices_y = []

        for i in range(num_points):
            angle = radians(float(i)/num_points * 360)

            x = width*cos(angle) + 800
            y = height*sin(angle) + 450

            self.vertices += [x,y]
            self.vertices_x += [x]
            self.vertices_y += [y]

        # The circle is an object of the class CircleLines
        global circle
        circle = pyglet.graphics.vertex_list(num_points, ('v2f', self.vertices))

    def draw(self):
        global circle
        glColor3f(1, 1, 1)
        # Object(circle) drawn by the Graphics Library
        circle.draw(GL_LINE_LOOP)

class CircleLines2:
    def __init__(self, num_points, width, height):
        self.vertices = []
        self.vertices_x = []
        self.vertices_y = []

        for i in range(num_points):
            angle = radians(float(i)/num_points * 360)

            x = width*cos(angle) + 795
            y = height*sin(angle) + 459

            self.vertices += [x, y]
            self.vertices_x += [x]
            self.vertices_y += [y]

        global circle2
        circle2 = pyglet.graphics.vertex_list(num_points, ('v2f', self.vertices))

    def draw(self):
        global circle2
        glColor3f(1, 1, 1)
        circle2.draw(GL_LINE_LOOP)
