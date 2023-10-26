import pyray
import GUIs
import GameLevels

class AppManager:
    screenWidth = 500
    screenHeight = 700
    gameState = "Menu"
    appManager = None
    def clearData(self):
        self.score = 0
        self.lives = 3

        self.level = GameLevels.Level1()

        self.gameGUI = GUIs.GameGUI()
        self.menuGUI = GUIs.MenuGUI()
        self.deathGUI = GUIs.DeathGUI()
        self.wipGUI = GUIs.WIPGUI()


    def __init__(self):
        # Конструктор где все обьекты инициализируются сразу. Если тестим функиональность какого нибудь класса
        # то создаем его здесь как поле класса и далле вызываем его методы в соответствующих функциях

        self.clearData()
        AppManager.appManager = self
    def Initialization(self):
        pyray.init_window(AppManager.screenWidth, AppManager.screenHeight, 'Game')
        # Ходят слухи, что здесь грузят текстуры. Должен вызывать методы обьетков Initialization.
        # Сам метод вызывается при создании программы.

    def Update(self):
        pyray.clear_background(pyray.BLACK)
        # Здесь вызываем Update вашего обьекта

        if AppManager.gameState is "Game":
            self.CheckCollision()
            self.level.update()
            if self.lives == 0:
                AppManager.gameState = "Death"
            else:
                self.gameGUI.score = self.score
                self.gameGUI.lives = self.lives
                self.gameGUI.update()
        elif AppManager.gameState is "Menu":
            self.menuGUI.update()
        elif AppManager.gameState is "Death":
            self.deathGUI.update()
        elif AppManager.gameState is "WIP":
            self.wipGUI.update()
    def Draw(self):
        pyray.begin_drawing()
        # Здесь вызываем Draw вашего обьекта.

        if AppManager.gameState is "Game":
            self.level.draw()
            self.gameGUI.draw()
        elif AppManager.gameState is "Menu":
            self.menuGUI.draw()
        elif AppManager.gameState is "Death":
            self.deathGUI.draw()
        elif AppManager.gameState is "WIP":
            self.wipGUI.draw()

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
                                                pyray.Rectangle(border.x+1, border.y, border.width, border.height)):
                if border.y == 80:
                    ball.onCollision()
                else:
                    self.lives -= 1
                    self.level.onPosition()
                border.onCollision()
        if pyray.check_collision_circle_rec(pyray.Vector2(ball.x, ball.y), ball.radius,
                                            pyray.Rectangle(platform.x, platform.y, platform.width, platform.height)):
            flag=True
            ball.onCollision(platform.y, flag)
            platform.onCollision()


def changeStateGame():
    AppManager.gameState = "Game"
def restart():
    AppManager.gameState = "Menu"
    AppManager.appManager.clearData()
def changeStateWIP():
    AppManager.gameState = "WIP"