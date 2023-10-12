import pyray
import Objects
class AppManager:
    def __init__(self):
        # Конструктор где все обьекты инициализируются сразу. Если тестим функиональность какого нибудь класса
        # то создаем его здесь как поле класса и далле вызываем его методы в соответствующих функциях
        self.screenWidth = 500
        self.screenHeight = 700

        self.items = []
        for i in range(5):
            for e in range(3):
                self.items.append(Objects.Brick(100 * i + 25, 50 * e, 50, 25, pyray.BLUE))
        self.items.append(Objects.Platform(100, 500, 80, 20, pyray.WHITE, 3))
        self.items.append(Objects.Ball(250, 300, 10, pyray.WHITE))


    def Initialization(self):
        pyray.init_window(self.screenWidth, self.screenHeight, 'test1')
        # Здесь ничего можно не писать. Теоретически может потом понадобится. Но лучше пока об этом не думать.
        pass

    def Update(self):
        pyray.clear_background(pyray.BLACK)
        # Здесь вызываем Update вашего обьекта

        for item in self.items:
            item.Update()

        pass

    def Draw(self):
        pyray.begin_drawing()
        # Здесь вызываем Draw вашего обьекта.

        for item in self.items:
            item.Draw()

        pyray.end_drawing()
        pass

