from abc import ABC, abstractmethod
import pyray

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
    def __init__(self, x, y):
        super().__init__(x, y)
class Platform(Object):
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