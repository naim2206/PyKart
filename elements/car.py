from ursina import *


class Player(EditorCamera):
    def __init__(self, **kwargs):

        self.car = load_texture('./../assets/car.png')
        self.entity = Entity(model='quad', position=Vec3(
            0, 1, 10), scale=1, rotation=Vec3(0, 0, 0), texture=self.car)
        super().__init__(parent=self.entity, rotation=Vec3(10, 0, 0), **kwargs)
