from ursina import *


class Player(EditorCamera):
    def __init__(self, **kwargs):
        self.car = load_texture('./../assets/sports-red.png')
        self.entity = Entity(model='./../assets/sports-car.obj', position=Vec3(
            0, 0, 4), scale=1, rotation=Vec3(0, 0, 0), texture=self.car, collider= "box")
        super().__init__(parent=self.entity, rotation=Vec3(10, 0, 0), **kwargs)
