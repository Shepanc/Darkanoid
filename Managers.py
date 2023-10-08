import pyray
import Objects
class AppManager:
    def __init__(self):
        self.screenWidth = 800
        self.screenHeight = 600

        self.platform = Objects.Platform(100, 100, 50, 20, pyray.BLUE)

    def Initialization(self):
        pyray.init_window(self.screenWidth, self.screenHeight, 'test1')

        pass

    def Update(self):
        pyray.clear_background(pyray.BLACK)

        self.platform.Update()
        pass

    def Draw(self):
        pyray.begin_drawing()

        self.platform.Draw()

        pyray.end_drawing()
        pass

