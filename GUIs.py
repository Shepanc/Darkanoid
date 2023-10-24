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

class UI(GUI):
    def __init__(self):
        super().__init__()
        self.CreateUI()

        self.score = None
        self.lives = None

    def CreateUI(self):
        screenWidth = Managers.AppManager.screenWidth
        screenHeight = Managers.AppManager.screenHeight

        self.items.append(Objects.Label(screenWidth // 20, screenHeight // 30,
                                        "Score: ", (screenWidth + screenHeight) // 30))
        self.items.append(Objects.Label(screenWidth // 20 * 7, screenHeight // 30,
                                        "0", (screenWidth + screenHeight) // 30, name = "Score"))
        self.items.append(Objects.Label(screenWidth // 20,
                                        screenHeight - screenHeight // 15,
                                        "Lives Remaining: ", (screenWidth + screenHeight) // 30))
        self.items.append(Objects.Label(screenWidth // 20 * 14,
                                        screenHeight - screenHeight // 15,
                                        "3", (screenWidth + screenHeight) // 30, name = "Lives"))
    def update(self):
        for item in self.items:
            if item.name == "Score":
                item.text = str(self.score)
            if item.name == "Lives":
                item.text = str(self.lives)