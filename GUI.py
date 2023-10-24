import pyray

class GUI:
    def __init__(self):
        self.items = list()
    def draw(self):
        for item in self.items:
            item.draw()
        pass

    def update(self):
        for item in self.items:
            item.update()
        pass