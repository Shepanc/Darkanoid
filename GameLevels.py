import pyray
import Objects
import GUIs


class GameLevel(GUIs.GUI):
    def __init__(self):
        super().__init__()
        self.items.append(Objects.Platform(250, 500, 80, 20, pyray.WHITE, 5))
        self.items.append(Objects.Ball(250, 300, 10, pyray.WHITE, 4))

    def remove(self, item):
        self.items.remove(item)

    @property
    def bricks(self):
        return [item for item in self.items if type(item) is Objects.Brick]

    @property
    def ball(self):
        return [item for item in self.items if type(item) is Objects.Ball][0]

    @property
    def platform(self):
        return [item for item in self.items if type(item) is Objects.Platform][0]


class Level1(GameLevel):
    def __init__(self):
        super().__init__()
        for i in range(5):
            for e in range(3):
                self.items.append(Objects.Brick(100 * i+18, 60 * e + 100, 60, 15, color=pyray.BLUE))
        pass


