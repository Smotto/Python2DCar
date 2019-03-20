from pyglet.gl import *
from Triangle import Triangle
import Move


class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(400, 300)
        glClearColor(0.2, 0.3, 0.2, 1.0)

        # Create object
        self.triangle = Triangle()

    # Draw the Quad
    def on_draw(self):
        self.clear()
        glDrawArrays(GL_TRIANGLES, 0, 3)

        # self.quad.vertices.draw(GL_TRIANGLES)
        # self.quad2.vertices.draw(GL_TRIANGLES)
        # self.quad3.render()

    # Be able to resize the Triangle
    def on_resize(self, width, height):
        glViewport(0, 0, width, height)


if __name__ == "__main__":
    window = MyWindow(1280, 720, "My Pyglet Window", resizable=True)
    window.on_draw()
    pyglet.app.run()
