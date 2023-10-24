import pyray

import Managers
import Objects


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

class Menu(GUI):
    def __init__(self):
        super().__init__()
        self.CreateMenu()

    def CreateMenu(self):
        screenWidth = Managers.AppManager.screenWidth
        screenHeight = Managers.AppManager.screenHeight
        self.items.append(Objects.Label(screenWidth // 20, screenHeight // 30,
                                        "Score: ", (screenWidth + screenHeight) // 30))

        self.items.append(Objects.Label(screenWidth // 20,
                                        screenHeight - screenHeight // 15,
                                        "Lives Remaining: ", (screenWidth + screenHeight) // 30))
