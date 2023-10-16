import pyray
import Objects

class GameLevel:
    def __init__(self):
        self.items = []
        self.items.append(Objects.Platform(100, 500, 80, 20, pyray.WHITE, 3))
        self.items.append(Objects.Ball(250, 300, 10, pyray.WHITE, 4))
        pass

    def Draw(self):
        for item in self.items:
            item.Draw()
        pass

    def Update(self):
        for item in self.items:
            item.Update()
        pass

    @property
    def getItems(self):
        return self.items

class Level1(GameLevel):
    def __init__(self):
        super().__init__()
        for i in range(5):
            for e in range(3):
                self.items.append(Objects.Brick(100 * i+18, 60 * e+20, 60, 15, color=pyray.BLUE))
        pass


