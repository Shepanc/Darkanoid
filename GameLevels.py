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

class Level1(GameLevel):
    def __init__(self):
        super().__init__()
        for i in range(5):
            for e in range(3):
                self.items.append(Objects.Brick(80 * i, 50 * e, 60, 15, color=pyray.BLUE))
        pass


