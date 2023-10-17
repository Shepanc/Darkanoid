import pyray
import GameLevels
class AppManager:
    screenWidth = 500
    screenHeight = 700
    def __init__(self):
        # Конструктор где все обьекты инициализируются сразу. Если тестим функиональность какого нибудь класса
        # то создаем его здесь как поле класса и далле вызываем его методы в соответствующих функциях

        self.level = GameLevels.Level1()


    def Initialization(self):
        pyray.init_window(AppManager.screenWidth, AppManager.screenHeight, 'test1')
        # Здесь ничего можно не писать. Теоретически может потом понадобится. Но лучше пока об этом не думать.
        pass

    def Update(self):
        pyray.clear_background(pyray.BLACK)
        # Здесь вызываем Update вашего обьекта

        self.level.update()

        pass

    def Draw(self):
        pyray.begin_drawing()
        # Здесь вызываем Draw вашего обьекта.

        self.level.draw()

        pyray.end_drawing()
        pass


    def CheckCollision(self):
        pass


