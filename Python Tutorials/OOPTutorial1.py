# Python Object-Oriented Programming


class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)


r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

r1.introduce_self()
r2.introduce_self()


class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False


pl = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)

# pl owns r2
pl.robot_owned = r2
p2.robot_owned = r1

pl.robot_owned.introduce_self()
