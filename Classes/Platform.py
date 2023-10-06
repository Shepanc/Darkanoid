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
        pass