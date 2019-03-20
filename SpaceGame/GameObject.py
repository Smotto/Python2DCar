import pyglet

# Preload the image for no lag!
def preload_image(image):
    img = pyglet.image.load('res/sprites/' + image)
    return img


class GameObject:
    # Every game object should have itself, position x, and position y. However, not every object has an image
    # Default sprite or image to None.
    def __init__(self, posx, posy, sprite = None):

        # Instance variables
        self.posx = posx
        self.posy = posy

        # Velocity initialized to a stand-still.
        self.velx = 0
        self.vely = 0

        # Ask if the image is !null
        if sprite is not None:
            self.sprite = sprite
            self.sprite.x = self.posx
            self.sprite.y = self.posy
            self.width = self.sprite.width
            self.height = self.sprite.height

            # When the Game Window or main file is run, it needs to load the image, and convert to a Sprite.
            # This is a costly process.
            # Set image variable to load the image from the folder res/sprites
            # image = pyglet.image.load('res/sprites/' + image)

            # Create the sprite
            # self.sprite = pyglet.sprite.Sprite(image, x = self.posx, y = self.posy)

    # Helper function for the main.py file.
    def draw(self):
            self.sprite.draw()


    def update(self):

        # It moves to the right.
        # multiply the correct deltaTime with the velocity taken from the main.py file.

        # self.posx += self.velx * dt
        # self.posy += self.vely * dt

        self.sprite.x = self.posx
        self.sprite.y = self.posy




