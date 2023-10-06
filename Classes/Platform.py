import pyray
import Classes
class Platform(Classes.Object):
    def __init__(self,x,y,wight,height,color):
            super().__init__()
            self.x = x
            self.y = y
            self.wight=wight
            self.height = height
            self.color=color
    def draw(self):
        pyray.draw_rectangle(
            self.x,
            self.y,
            self.wight,
            self.height,
            self.color
        )