import pyglet
from pygame import Vector2

# Preload the image for no lag!
def preload_image(image):
    img = pyglet.image.load('res/sprites/' + image)

    return img

def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


class GameObject:
    # Every game object should have itself, position x, and position y. However, not every object has an image
    # Default sprite or image to None.
    def __init__(self, position_x, position_y, rotation = 0, sprite = None):

        # Instance variables
        self.position_x = position_x
        self.position_y = position_y
        self.rotation = rotation

        # Ask if the image is !null
        if sprite is not None:
            # Image is the parameter
            self.sprite = sprite
            # Image is the x position
            self.sprite.x = self.position_x
            # Image is the y position
            self.sprite.y = self.position_y
            # Image has a rotation
            self.sprite.rotation = self.rotation
            # Image has a width
            self.width = self.sprite.width
            # Image has a height
            self.height = self.sprite.height

    # Draw the sprite itself.
    def draw(self):
       # Draw Image
        self.sprite.draw()

    def update(self):
        # Update x position
        self.sprite.x = self.position_x
        # Update y position
        self.sprite.y = self.position_y

        # Update image's rotation
        self.sprite.rotation = self.rotation
