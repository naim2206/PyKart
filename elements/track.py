from ursina import *


class Track(Entity):
    def __init__(self):
        self.track = load_texture('./../assets/track1.jpg')
        super().__init__(model='plane', scale=(100, 100, 100), texture=self.track)
