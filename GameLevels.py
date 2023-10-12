import pyray
import Objects
from abc import ABC, abstractmethod

class GameLevel(ABC):
    def __init__(self):
        self.items = []
        self.items.append(Objects.Platform(100, 500, 80, 20, pyray.WHITE, 3))
        self.items.append(Objects.Ball(250, 300, 10, pyray.WHITE))
        pass

    @abstractmethod
    def Draw(self):
        for item in self.items:
            item.Draw()
        pass

    @abstractmethod
    def Update(self):
        for item in self.items:
            item.Update()
        pass


