from pyglet.gl import *
import pyglet
from math import *

class CircleLines:
    def __init__(self, num_points, width, height):
        verts = []
        for i in range(num_points):
            angle = radians(float(i)/num_points * 360)

            x = width*cos(angle) + 800
            y = height*sin(angle) + 450

            verts += [x,y]
        global circle
        circle = pyglet.graphics.vertex_list(num_points, ('v2f', verts))

    def draw(self):
        global circle
        glColor3f(1, 1, 1)
        circle.draw(GL_LINE_LOOP)

class CircleLines2:
    def __init__(self, num_points, width, height):
        verts = []
        for i in range(num_points):
            angle = radians(float(i)/num_points * 360)

            x = width*cos(angle) + 795
            y = height*sin(angle) + 459

            verts += [x,y]
        global circle2
        circle2 = pyglet.graphics.vertex_list(num_points, ('v2f', verts))

    def draw(self):
        global circle2
        glColor3f(1, 1, 1)
        circle2.draw(GL_LINE_LOOP)
