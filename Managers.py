import pyray

import GUIs
import GameLevels
import random

class AppManager:
    screenWidth = 500
    screenHeight = 700
    def __init__(self):
        # Конструктор где все обьекты инициализируются сразу. Если тестим функиональность какого нибудь класса
        # то создаем его здесь как поле класса и далле вызываем его методы в соответствующих функциях

        self.level = GameLevels.Level1()
        self.menu = GUIs.Menu()

    def Initialization(self):
        pyray.init_window(AppManager.screenWidth, AppManager.screenHeight, 'test1')
        # Ходят слухи, что здесь грузят текстуры. Должен вызывать методы обьетков Initialization.
        # Сам метод вызывается при создании программы.

        pass

    def Update(self):
        pyray.clear_background(pyray.BLACK)
        # Здесь вызываем Update вашего обьекта

        self.CheckCollision()
        self.level.update()
        self.menu.update()

        pass

    def Draw(self):
        pyray.begin_drawing()
        # Здесь вызываем Draw вашего обьекта.

        self.level.draw()
        self.menu.draw()

        pyray.end_drawing()
        pass

    def CheckCollision(self):
        ball = self.level.ball
        platform = self.level.platform

        for brick in self.level.bricks:
            if pyray.check_collision_circle_rec(pyray.Vector2(ball.x, ball.y), ball.radius,
                                                pyray.Rectangle(brick.x, brick.y, brick.width, brick.height)):
                ball.onCollision()
                brick.onCollision()
                self.level.remove(brick)
        if pyray.check_collision_circle_rec(pyray.Vector2(ball.x, ball.y), ball.radius,
                                            pyray.Rectangle(platform.x, platform.y, platform.width, platform.height)):
            ball.onCollision()
            platform.onCollision()


