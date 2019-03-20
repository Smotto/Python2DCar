import pyglet
from pyglet.gl import *
import GameObject


# Create Car Lines.
class CollisionDetection:
    def __init__(self, object, wall, wall2):
        self.width = object.width
        self.height = object.height
        self.wall = wall
        self.wall2 = wall2

    def draw_line(self):
        glBegin(GL_LINES)

        #first line
        glVertex2i(self.width, self.height)
        glVertex2i(50, 100)

        glEnd()