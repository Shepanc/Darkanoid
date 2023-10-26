import pyray

import Managers
import Objects


class GUI:
    def __init__(self):
        self.items = list() # Все обьекты интерфейса
    def draw(self):
        for item in self.items:
            item.draw()
        pass

    def update(self):
        for item in self.items:
            item.update()
        pass

    # Нужен для переключения выбора в менюшках и тд.
    def controlUpd(self):
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_ENTER):
            self.selectedBtn.onPressEvent()

        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_DOWN):
            for i in range(len(self.items)):
                if self.selectedBtn == self.items[i]:
                    if i == 0:
                        self.selectedBtn = self.items[len(self.items)-1]
                        break
                    else:
                        self.selectedBtn = self.items[i - 1]
                        break
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_UP):
            for i in range(len(self.items)):
                if self.selectedBtn == self.items[i]:
                    if i == len(self.items) - 1:
                        self.selectedBtn = self.items[0]
                        break
                    else:
                        self.selectedBtn = self.items[i + 1]
                        break

        for item in self.items:
            if self.selectedBtn.label.text == item.label.text:
                item.label.color = pyray.RED
            else:
                item.label.color = pyray.WHITE

class GameGUI(GUI):
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
class MenuGUI(GUI):
    def __init__(self):
        super().__init__()
        self.CreateUI()

    def CreateUI(self):
        screenWidth = Managers.AppManager.screenWidth
        screenHeight = Managers.AppManager.screenHeight

        startBtn = Objects.Button(x=screenWidth//2 - screenWidth//13,
                                  y=screenHeight//3 + screenHeight//9,
                                  color=pyray.BLACK,
                                  onPressEvent=Managers.changeStateGame,
                                  label=Objects.Label(text="Start",
                                                      fontsize=30))
        self.items.append(startBtn)
        self.selectedBtn = startBtn

        exitBtn = Objects.Button(x=screenWidth // 2 - 25,
                                 y=screenHeight // 16 * 9,
                                 color=pyray.BLACK,
                                 onPressEvent=lambda: pyray.close_window(),
                                 label=Objects.Label(text="Exit",
                                                     fontsize=30))
        self.items.append(exitBtn)

        infoBtn = Objects.Button(x=screenWidth // 2 - 25,
                                 y=screenHeight // 12*6,
                                 color=pyray.BLACK,
                                 onPressEvent=Managers.changeStateWIP,
                                 label=Objects.Label(text="Info",
                                                     fontsize=30))
        self.items.append(infoBtn)
    def update(self):
        super().update()
        self.controlUpd()

class DeathGUI(GUI):
    def __init__(self):
        super().__init__()
        self.CreateUI()
    def CreateUI(self):
        screenWidth = Managers.AppManager.screenWidth
        screenHeight = Managers.AppManager.screenHeight

        retryBtn = Objects.Button(x=screenWidth // 2 - screenWidth // 13,
                                  y=screenHeight // 3 + screenHeight // 9,
                                  color=pyray.BLACK,
                                  onPressEvent=Managers.restart,
                                  label=Objects.Label(text="Retry",
                                                      fontsize=30))
        self.items.append(retryBtn)
        self.selectedBtn = retryBtn

        exitBtn = Objects.Button(x=screenWidth // 2 - 25,
                                 y=screenHeight // 12*6,
                                 color=pyray.BLACK,
                                 onPressEvent=lambda: pyray.close_window(),
                                 label=Objects.Label(text="Exit",
                                                     fontsize=30))
        self.items.append(exitBtn)
    def update(self):
        super().update()
        self.controlUpd()

class WIPGUI(GUI):
    def __init__(self):
        super().__init__()
        self.CreateUI()
    def CreateUI(self):
        screenWidth = Managers.AppManager.screenWidth
        screenHeight = Managers.AppManager.screenHeight

        retryBtn = Objects.Button(x=screenWidth // 2 - screenWidth // 4,
                                  y=screenHeight // 3 + screenHeight // 9,
                                  color=pyray.BLACK,
                                  onPressEvent=None,
                                  label=Objects.Label(text="Darkonoid project made by Andrei, Lesha, Kirill and Sledge",
                                                      fontsize=30))
        self.items.append(retryBtn)
        self.selectedBtn = retryBtn

        exitBtn = Objects.Button(x=screenWidth // 2 - 25,
                                 y=screenHeight // 12*6,
                                 color=pyray.BLACK,
                                 onPressEvent=Managers.restart,
                                 label=Objects.Label(text="Back",
                                                     fontsize=30))
        self.items.append(exitBtn)
    def update(self):
        self.controlUpd()