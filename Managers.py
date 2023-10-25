import pyray
import GUIs
import GameLevels

class AppManager:
    screenWidth = 500
    screenHeight = 700
    gameState = "Menu"

    def __init__(self):
        # Конструктор где все обьекты инициализируются сразу. Если тестим функиональность какого нибудь класса
        # то создаем его здесь как поле класса и далле вызываем его методы в соответствующих функциях

        self.level = GameLevels.Level1()
        self.gameGUI = GUIs.GameGUI()
        self.menuGUI = GUIs.MenuGUI()

        self.score = 0
        self.lives = 3

    def Initialization(self):
        pyray.init_window(AppManager.screenWidth, AppManager.screenHeight, 'test1')
        # Ходят слухи, что здесь грузят текстуры. Должен вызывать методы обьетков Initialization.
        # Сам метод вызывается при создании программы.

        pass

    def Update(self):
        pyray.clear_background(pyray.BLACK)
        # Здесь вызываем Update вашего обьекта

        if AppManager.gameState is "Game":
            self.CheckCollision()
            self.level.update()

            self.gameGUI.score = self.score
            self.gameGUI.lives = self.lives
            self.gameGUI.update()
        elif AppManager.gameState is "Menu":
            self.menuGUI.update()

    def Draw(self):
        pyray.begin_drawing()
        # Здесь вызываем Draw вашего обьекта.

        if AppManager.gameState is "Game":
            self.level.draw()
            self.gameGUI.draw()
        elif AppManager.gameState is "Menu":
            self.menuGUI.draw()

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

                self.score += 1

                self.level.remove(brick)
        for border in self.level.borders:
            if pyray.check_collision_circle_rec(pyray.Vector2(ball.x, ball.y), ball.radius,
                                                pyray.Rectangle(border.x, border.y, border.width, border.height)):
                if border.y == 80:
                    ball.onCollision()
                else:
                    self.lives -= 1
                border.onCollision()
        if pyray.check_collision_circle_rec(pyray.Vector2(ball.x, ball.y), ball.radius,
                                            pyray.Rectangle(platform.x, platform.y, platform.width, platform.height)):
            ball.onCollision()
            platform.onCollision()

def changeStateGame():
    AppManager.gameState = "Game"

