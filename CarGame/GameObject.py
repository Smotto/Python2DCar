import pyglet

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
            self.sprite = sprite
            self.sprite.x = self.position_x
            self.sprite.y = self.position_y
            self.sprite.rotation = self.rotation
            self.width = self.sprite.width
            self.height = self.sprite.height

    # Draw the sprite itself.
    def draw(self):
            self.sprite.draw()

    def update(self):
        self.sprite.x = self.position_x
        self.sprite.y = self.position_y

        self.sprite.rotation = self.rotation
