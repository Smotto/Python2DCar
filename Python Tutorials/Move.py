from Triangle import Triangle
import Window
import keyboard


# Move the object

class Move(Triangle):
    def __init__(self):
        # Immediate parent class of itself?
        super().__init__()

        # Step 1: Obtain the triangle's vertices
        self.triangle = Window.Triangle

    # Step 2: Move the triangle's vertices according to player's keypress
    def move_up(self):
        while True:
            try:
                if keyboard.is_pressed('x'):
                    for vertex in self.triangle:
                        print("Testing! UP")
                else:
                    # ??????
                    pass
            except:
                break

    def move_down(self):
        for vertex in self.triangle:
            print("Testing! DOWN")

    def move_left(self):
        for vertex in self.triangle:
            print("Testing! LEFT")

    def move_right(self):
        for vertex in self.triangle:
            print("Testing! RIGHT")
