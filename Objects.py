from abc import ABC, abstractmethod
import pyray
import Managers

class Object(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def Draw(self):
        pass

    @abstractmethod
    def Update(self):
        pass
class Brick(Object):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.color = color

    def Draw(self):
        pyray.draw_rectangle(
            self.x,
            self.y,
            self.width,
            self.height,
            self.color
        )

    def Update(self):
        pass
class Platform(Object):
    def __init__(self, x, y, width, height, color, speed):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def Draw(self):
        pyray.draw_rectangle(
            self.x,
            self.y,
            self.width,
            self.height,
            self.color
        )

    def Update(self):
        if pyray.is_key_down(pyray.KeyboardKey.KEY_D):
            if self.x<Managers.AppManager.screenWidth-self.width :
                self.x += self.speed
        if pyray.is_key_down(pyray.KeyboardKey.KEY_A):
            if self.x>0:
                self.x -= self.speed
class Ball(Object):
    def __init__(self, x, y, radius, color, speed):
        super().__init__(x, y)
        self.radius = radius
        self.color = color
        self.speed = speed

    def Draw(self):
        pyray.draw_circle(self.x, self.y, self.radius, self.color)

    def Update(self):
        pass
    def move(self):
        self.x+=self.speed
        self.y += self.speed

