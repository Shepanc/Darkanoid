from abc import ABC, abstractmethod
import pyray
import Managers
import numpy

class Object(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def onCollision(self):
        pass
class Brick(Object):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        pyray.draw_rectangle(
            self.x,
            self.y,
            self.width,
            self.height,
            self.color
        )

    def update(self):
        pass

    def onCollision(self):
        pass
class Platform(Object):
    def __init__(self, x, y, width, height, color, speed):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def draw(self):
        pyray.draw_rectangle(
            self.x,
            self.y,
            self.width,
            self.height,
            self.color
        )

    def update(self):
        if pyray.is_key_down(pyray.KeyboardKey.KEY_D):
            if self.x < Managers.AppManager.screenWidth-self.width :
                self.x += self.speed
        if pyray.is_key_down(pyray.KeyboardKey.KEY_A):
            if self.x > 0:
                self.x -= self.speed

    def onCollision(self):
        pass
class Ball(Object):
    def __init__(self, x, y, radius, color, speed):
        super().__init__(x, y)
        self.radius = radius
        self.color = color
        self.speed = speed

    def draw(self):
        pyray.draw_circle(self.x, self.y, self.radius, self.color)

    def update(self):

        pass

    def move(self):
        pass

    def onCollision(self):
        pass

