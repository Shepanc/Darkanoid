import random
from abc import ABC, abstractmethod
import pyray
import Managers
import vec

class Object(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def onCollision(self):
        pass
class Brick(Object):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y)
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

    def update(self):
        pass

    def onCollision(self):
        pass
class Platform(Object):
    def __init__(self, x, y, width, height, color, speed,t=100):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.t=t

    def draw(self):
        pyray.draw_rectangle(
            self.x,
            self.y,
            self.width,
            self.height,
            self.color
        )

    def update(self):
        if pyray.is_key_down(pyray.KeyboardKey.KEY_D):
            if self.x < Managers.AppManager.screenWidth - self.width:
                self.x += self.speed
            if(self.t<=100):
                self.t+=1
                print(self.t)
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
                print(self.t)
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
        self.vSpeed = vec.Vector2(speed, speed)
        self.vDirection = vec.Vector2(0.5, 1)

    def draw(self):
        pyray.draw_circle(self.x, self.y, self.radius, self.color)

    def update(self):
        self.move()
        pass

    def move(self):
        if self.x <= self.radius or self.x >= Managers.AppManager.screenWidth - self.radius:
            self.vSpeed = vec.Vector2(self.vSpeed.x * -1, self.vSpeed.y)
        if self.y <= self.radius or self.y >= Managers.AppManager.screenHeight - self.radius:
            self.vSpeed = vec.Vector2(self.vSpeed.x, self.vSpeed.y * -1)

        self.x += int(self.vSpeed.x * self.vDirection.x)
        self.y += int(self.vSpeed.y * self.vDirection.y)
        pass

    def onCollision(self):
        rnd = (random.random()+0.6)*1.6
        r = (random.random()+0.4) * 1.6
        if(self.vDirection.y<0):
            self.vDirection = vec.Vector2(rnd, r)
        else:
            self.vDirection = vec.Vector2(rnd, r*-1)
        pass

