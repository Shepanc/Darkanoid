import pyray
import Objects

class GameLevel:
    def __init__(self):
        self.items = []
        self.items.append(Objects.Platform(100, 500, 80, 20, pyray.WHITE, 3))
        self.items.append(Objects.Ball(250, 300, 10, pyray.WHITE, 4))
        pass

    def draw(self):
        for item in self.items:
            item.draw()
        pass

    def update(self):
        for item in self.items:
            item.update()
        pass

    @property
    def Items(self):
        return self.items

class Level1(GameLevel):
    def __init__(self):
        super().__init__()
        for i in range(5):
            for e in range(3):
                self.items.append(Objects.Brick(100 * i+18, 60 * e+20, 60, 15, color=pyray.BLUE))
        pass


