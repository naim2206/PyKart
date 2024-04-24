from ursina import *

class ForestTrack(Entity):
    def __init__(self):
        super().__init__(
            model = "forest_track.obj", 
            texture = "./../assets/forest_track/forest_track.png", 
            position = (0, -50, 0), 
            rotation = (0, 270, 0), 
            scale = (12, 12, 12), 
            collider = "mesh"
        )

        self.finish_line = Entity(model = "cube", position = (31, -48, 72), rotation = (0, 0, 0), scale = (3, 8, 30), visible = False)
        self.boundaries = Entity(model = "./../assets/forest_track/forest_track_bounds.obj", collider = "mesh", position = (0, -50, 0), rotation = (0, 270, 0), scale = (12, 12, 12), visible = False)

        self.wall1 = Entity(model = "cube", position = (-16, -48, 50), collider = "box", rotation = (0, 90, 0), scale = (5, 30, 50), visible = False)
        self.wall2 = Entity(model = "cube", position = (-16, -48, 23), collider = "box", rotation = (0, 90, 0), scale = (5, 30, 50), visible = False)
        self.wall3 = Entity(model = "cube", position = (5, -48, 33), collider = "box", rotation = (0, 0, 0), scale = (5, 30, 40), visible = False)
        self.wall4 = Entity(model = "cube", position = (-34, -48, 33), collider = "box", rotation = (0, 0, 0), scale = (5, 30, 40), visible = False)
        self.wall5 = Entity(model = "cube", position = (-18, -48, 0), collider = "box", rotation = (0, 90, 0), scale = (5, 30, 50), visible = False)
        self.wall6 = Entity(model = "cube", position = (-18, -48, -30), collider = "box", rotation = (0, 90, 0), scale = (5, 30, 50), visible = False)
        self.wall7 = Entity(model = "cube", position = (-4, -48, -15), collider = "box", rotation = (0, 0, 0), scale = (5, 30, 50), visible = False)
        self.wall8 = Entity(model = "cube", position = (-30, -48, -15), collider = "box", rotation = (0, 0, 0), scale = (5, 30, 50), visible = False)

        self.wall_trigger = Entity(model = "cube", position = (11, -45, -70), rotation = (0, 0, 0), scale = (3, 20, 40), visible = False)

        self.trees = Entity(model = "./../assets/forest_track/trees-forest.obj", texture = "./../assets/forest_track/tree-forest.png", position = (0, -50, 0), scale = 12, rotation_y = 270)
        self.thin_trees = Entity(model = "./../assets/forest_track/thintrees-forest.obj", texture = "./../assets/forest_track/thintree-forest.png", position = (0, -50, 0), scale = 12, rotation_y = 270)

        self.track = [
            self.finish_line, self.boundaries, self.wall1, self.wall2, self.wall3, 
            self.wall4, self.wall5, self.wall6, self.wall7, self.wall8, self.wall_trigger
        ]

        self.details = [
            self.trees, self.thin_trees
        ]
        
        
        self.played = False
        self.unlocked = False
