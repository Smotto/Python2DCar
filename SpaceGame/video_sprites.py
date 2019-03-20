import pyglet
from pyglet.window import key, FPSDisplay
from random import randint


class GameWindow(pyglet.window.Window):

    # Kind of like calling a main or something
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(400, 100)
        self.frame_rate = 1 / 60.0
        self.fps_display = FPSDisplay(self)
        self.fps_display.label.font_size = 50


        # Can add multiple sprites to one batch, and draw with one call.
        self.main_batch = pyglet.graphics.Batch()

        # Step 1: Load enemy
        enemy_ship = pyglet.image.load("res/sprites/enemyShip_Sh01.png")

        # Step 2: Sequence, 1 row, 15 col, 100 width and height
        enemy_ship_seq = pyglet.image.ImageGrid(enemy_ship, 1, 15, item_width = 100, item_height = 100)

        ## Optional, Step 3: Create texture from it, Texture grid
        ## enemy_ship_texture = pyglet.image.TextureGrid(enemy_ship_seq)

        # Step 4: Animations, 0 to end of list [0:]
        enemy_ship_animation = pyglet.image.Animation.from_image_sequence(enemy_ship_seq[0:], 0.1, loop = True)

        # Step 5: self, for using it in on_draw method, put into batch.
        self.enemy_ship = pyglet.sprite.Sprite(enemy_ship_animation, x = 200, y = 200, batch = self.main_batch)


        # Step 1: Load enemy
        explosion = pyglet.image.load("res/sprites/explosion.png")

        # Step 2: Sequence, 1 row, 15 col, 96 width and height
        explosion_seq = pyglet.image.ImageGrid(explosion, 4, 5, item_width = 96, item_height = 96)

        ## Optional, Step 3: Create texture from it, Texture grid
        ## explosion_texture = pyglet.image.TextureGrid(explosion_seq)

        # Step 4: Animations, 0 to end of list [0:]
        explosion_animation = pyglet.image.Animation.from_image_sequence(explosion_seq[0:], 0.1, loop = True)

        # Step 5: self, for using it in on_draw method, put into batch.
        self.explosion = pyglet.sprite.Sprite(explosion_animation, x = 500, y = 200, batch = self.main_batch)


        # Step 1: Load enemy
        enemy_head = pyglet.image.load('res/sprites/ufoHead_Sh.png')

        # Step 2: Sequence, 1 row, 8 columns, 100 height, 100 width (800 / 8)
        enemy_head_seq = pyglet.image.ImageGrid(enemy_head, 1, 8, item_width = 100, item_height = 100)

        # Step 3: skip step 3

        # Step 4: Animations, 0 to end of list [0:]
        enemy_head_animation = pyglet.image.Animation.from_image_sequence(enemy_head_seq[0:], 0.1, loop = True)

        # Step 5: self, for using it in on_draw method, put into batch
        # Step 5: Create Random Enemies
        self.enemy_list = []
        for i in range(5):
            self.enemy_list.append(pyglet.sprite.Sprite(enemy_head_animation, x = randint(200, 800), y = randint(500, 800), batch = self.main_batch))

        # Text labels on UI
        text = pyglet.text.Label("Hello :^)", x = 600, y = 450, batch = self.main_batch)
        text.italic = True
        text.bold = True
        text.font_size = 40
        # Anchors
        text.anchor_x = "center"
        text.anchor_y = "center"

        # Step 1: Load media file,
        # Streaming means instruct Pyglet to completely decode an audio file to memory at load time
        self.laser_sound = pyglet.media.load("res/sounds/player_gun.wav", streaming = False)




    def on_draw(self):
        self.clear()

        # Two Draw calls, not efficient.
        # self.enemy_ship.draw()
        # self.explosion.draw()

        # for enemy in self.enemy_list:
         #   enemy.draw()

        self.main_batch.draw()
        self.fps_display.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.laser_sound.play()


    def update(self, dt):
        pass

if __name__ == "__main__":
    window = GameWindow(1200, 900, "Enemy?", resizable=False)
    # Make sure the clock is the same as the window's update, and the window's frame rate
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()