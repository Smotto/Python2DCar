from pyglet.gl import *
import ctypes


class Triangle:
    def __init__(self):
        self.triangle = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,  # Vertex Placement
                         0.5, -0.5, 0.0, 0.0, 1.0, 0.0,  # Vertex Placement
                         0.0, 0.5, 0.0, 0.0, 0.0, 1.0]  # Vertex PLacement, Upper Part of Tri.
        # We have 3 rows * 6 columns = 18 while use n times 4bytes = 72bytes

        self.vertex_shader_source = b"""
        #version 330
        in layout(location = 0) vec3 position;
        in layout(location = 1) vec3 color;
        
        out vec3 newColor;
        void main()
        {
            gl_Position = vec4(position, 1.0f);
            newColor = color;
        }
        """

        # b = binary

        self.fragment_shader_source = b"""
        #version 330
        in vec3 newColor;
        
        out vec4 outColor;
        void main()
        {
            outColor = vec4(newColor, 1.0f);
        }
        """

        # PyOpenGL Model...
        '''
        shader = OpenGL.GL.shaders.compileProgram(OpenGL.shaders.compileShader(self.vertex_shader_source,
                                                                               GL_VERTEX_SHADER),
                                                  OpenGL.GL.shaders.compileShader(self.fragment_shader_source,
                                                                                  GL_FRAGMENT_SHADER))
        
        
        '''
        # Casting vertex_buff into Glchar
        vertex_buff = ctypes.create_string_buffer(self.vertex_shader_source)
        c_vertex = ctypes.cast(ctypes.pointer(ctypes.pointer(vertex_buff)), ctypes.POINTER(ctypes.POINTER(GLchar)))
        vertex_shader = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(vertex_shader, 1, c_vertex, None)
        glCompileShader(vertex_shader)

        fragment_buff = ctypes.create_string_buffer(self.fragment_shader_source)
        c_fragment = ctypes.cast(ctypes.pointer(ctypes.pointer(fragment_buff)), ctypes.POINTER(ctypes.POINTER(GLchar)))
        fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(fragment_shader, 1, c_fragment, None)
        glCompileShader(fragment_shader)

        shader = glCreateProgram()
        glAttachShader(shader, vertex_shader)
        glAttachShader(shader, fragment_shader)
        glLinkProgram(shader)

        # Everything below do not edit.

        glUseProgram(shader)

        vbo = GLuint(0)
        glGenBuffers(1, vbo)

        # Send data to the GPU
        # Create GL Float Array * the length of the triangles,
        # and unpacks the values of the triangle to the array of GL floats
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, 72, (GLfloat * len(self.triangle))(*self.triangle), GL_STATIC_DRAW)

        # positions, three values of type GL_FLOAT
        # 24, because 6 columns * 4 bytes per column
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        # colors Normalized = GL_FALSE
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)
