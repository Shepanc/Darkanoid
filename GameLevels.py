import pyray
import Objects

class GameLevel:
    def __init__(self):
        self.items = list()
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
            if not item.isAlive:
                self.items.remove(item)
        pass

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
                self.items.append(Objects.Brick(100 * i+18, 60 * e+20, 60, 15, color=pyray.BLUE))
        pass


