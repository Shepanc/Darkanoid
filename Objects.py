import random
import pyray
import Managers
import vec

class Object():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pass

    def update(self):
        pass


class Rectangle(Object):
    def __init__(self, x, y, width, height, color = pyray.WHITE):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        pyray.draw_rectangle(
            self.x,
            self.y,
            self.width,
            self.height,
            self.color
        )
    def onCollision(self):
        pass

class Brick(Rectangle):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
    def onCollision(self):
        pass
class Platform(Rectangle):
    def __init__(self, x, y, width, height, color, speed):
        super().__init__(x, y, width, height, color)
        self.speed = speed
        self.t = 100

    def update(self):
        if pyray.is_key_down(pyray.KeyboardKey.KEY_D):
            if self.x < Managers.AppManager.screenWidth - self.width:
                self.x += self.speed
            if(self.t<=100):
                self.t+=1
            if pyray.is_key_down(pyray.KeyboardKey.KEY_LEFT_SHIFT):
                if self.x <Managers.AppManager.screenWidth - self.width-20:
                    if(self.t>0):
                        self.x +=15
                        self.t-=20
        if pyray.is_key_down(pyray.KeyboardKey.KEY_A):
            if self.x > 0:
                self.x -= self.speed
            if(self.t<=100):
                self.t+=1
            if pyray.is_key_down(pyray.KeyboardKey.KEY_LEFT_SHIFT):
                if self.x > 20:
                    if (self.t > 0):
                        self.x -=15
                        self.t-=20
    def onCollision(self):
        pass
class Ball(Object):
    def __init__(self, x, y, radius, color, speed):
        super().__init__(x, y)
        self.radius = radius
        self.color = color
        self.speed = speed
        self.vSpeed = vec.Vector2(speed, speed)
        self.vDirection = vec.Vector2(0.01, 1)
        self.firstPunch = False

    def draw(self):
        pyray.draw_circle(self.x, self.y, self.radius, self.color)

    def update(self):
        self.move()
        pass

    def move(self):
        if self.x <= self.radius or self.x >= Managers.AppManager.screenWidth - self.radius:
            self.vSpeed = vec.Vector2(self.vSpeed.x * -1, self.vSpeed.y)

        self.x += int(self.vSpeed.x * self.vDirection.x)
        self.y += int(self.vSpeed.y * self.vDirection.y)
        pass

    def onCollision(self):
        rnd = (random.random()+0.6)*1.6
        r = (random.random()+0.4) * 1.6
        if self.vDirection.y < 0:
            self.vDirection = vec.Vector2(rnd, r)
        else:
            self.vDirection = vec.Vector2(rnd, r*-1)

        if not self.firstPunch:
            self.vSpeed = vec.Vector2(3, 3)
            self.firstPunch = True
class Label(Object):
    def __init__(self, x = 0, y = 0, text = "", fontsize = 20, spacing = 1, color = pyray.WHITE, font = None, name = None):
        super().__init__(x, y)
        self.fontsize = fontsize
        self.text = text
        self.font = font
        self.spacing = spacing
        self.color = color
        self.name = name

    def draw(self):
        if self.font is not None:
            pyray.draw_text_ex(self.font, self.text, pyray.Vector2(self.x, self.y),
                               self.fontsize, self.spacing, self.color)
        else:
            pyray.draw_text(self.text, self.x, self.y, self.fontsize, self.color)

    def update(self):
        pass
class Button(Rectangle):
    def __init__(self, x, y, color, label, onPressEvent, width = 0, height = 0):
        super().__init__(x, y, width, height, color)
        self.label = Label(x=x, y=y,
                           text=label.text, fontsize=label.fontsize,
                           spacing=label.spacing, color=label.color,
                           font=label.font, name=label.name)
        self.onPressEvent = onPressEvent

    def draw(self):
        super().draw()
        self.label.draw()
