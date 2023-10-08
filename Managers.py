import pyray
import Objects
class AppManager:
    def __init__(self):
        # Конструктор где все обьекты инициализируются сразу. Если тестим функиональность какого нибудь класса
        # то создаем его здесь как поле класса и далле вызываем его методы в соответствующих функциях
        self.screenWidth = 800
        self.screenHeight = 600

        self.platform = Objects.Platform(100, 100, 50, 20, pyray.BLUE) # Пример тестового класса. Синяя платформа без логики

    def Initialization(self):
        pyray.init_window(self.screenWidth, self.screenHeight, 'test1')
        # Здесь ничего можно не писать. Теоретически может потом понадобится. Но лучше пока об этом не думать.
        pass

    def Update(self):
        pyray.clear_background(pyray.BLACK)
        # Здесь вызываем Update вашего обьекта
        self.platform.Update()
        pass

    def Draw(self):
        pyray.begin_drawing()
        # Здесь вызываем Draw вашего обьекта.
        self.platform.Draw()

        pyray.end_drawing()
        pass

