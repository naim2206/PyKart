from ursina import *


class Track(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'cube'
        self.scale = (10, .5, 60)
        self.position = (0, 0)
        self.texture = './assets/track.png'
