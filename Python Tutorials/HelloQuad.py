from pyglet.gl import *


# Always check the vertex_list_index, because they can easily ruin your day.
class Quad:
    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list_indexed(4, [0, 1, 2,
                                                                2, 3, 0],
                                                            ('v3f', [-0.5, -0.5, 0.0,
                                                                     0.5, -0.5, 0.0,
                                                                     0.5, 0.5, 0.0,
                                                                     -0.5, 0.5, 0.0]),  # Don't Forget the comma
                                                            ('c3f', [1.0, 0.0, 0.0,  # Color, 3, f
                                                                     0.0, 1.0, 0.0,
                                                                     0.0, 0.0, 1.0,
                                                                     1.0, 1.0, 1.0])
                                                            )


class Quad2:
    def __init__(self):
        self.indices = [0, 1, 2,
                        2, 3, 0]

        self.vertex = [-0.5, -0.5, 0.0,
                       0.5, -0.5, 0.0,
                       0.5, 0.5, 0.0,
                       -0.5, 0.5, 0.0]

        self.color = [1.0, 0.0, 0.0,  # Color, 3, f
                      0.0, 1.0, 0.0,
                      0.0, 0.0, 1.0,
                      1.0, 1.0, 1.0]

        # Much more readable than Quad...
        self.vertices = pyglet.graphics.vertex_list_indexed(4, self.indices, ('v3f', self.vertex), ('c3f', self.color))


class Quad3:
    def __init__(self):
        self.indices = [0, 1, 2,
                        2, 3, 0]

        self.vertex = [-0.5, -0.5, 0.0,
                       0.5, -0.5, 0.0,
                       0.5, 0.5, 0.0,
                       -0.5, 0.5, 0.0]

        self.color = [1.0, 0.0, 0.0,  # Color, 3, f
                      0.0, 1.0, 0.0,
                      0.0, 0.0, 1.0,
                      1.0, 1.0, 1.0]

    def render(self):
        # Much more readable than Quad...
        self.vertices = pyglet.graphics.draw_indexed(4, GL_TRIANGLES, self.indices, ('v3f', self.vertex), ('c3f', self.color))


class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(400, 300)
        glClearColor(0.2, 0.3, 0.2, 1.0)

        self.quad = Quad()
        self.quad2 = Quad2()
        self.quad3 = Quad3()

    # Draw the Quad
    def on_draw(self):
        self.clear()
        # self.quad.vertices.draw(GL_TRIANGLES)
        # self.quad2.vertices.draw(GL_TRIANGLES)
        self.quad3.render()

    # Be able to resize the Triangle
    def on_resize(self, width, height):
        glViewport(0, 0, width, height)


if __name__ == "__main__":
    window = MyWindow(1280, 720, "My Pyglet Window", resizable=True)
    window.on_draw()
    pyglet.app.run()
