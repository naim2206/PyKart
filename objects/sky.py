from ursina import *

class Sky(Entity):

    def __init__(self, **kwargs):
        from ursina.shaders import unlit_shader
        super().__init__(parent=render, name='sky', model='sky_dome', texture='sky.webp', scale=9900, shader=unlit_shader)

        for key, value in kwargs.items():
            setattr(self, key, value)


    def update(self):
        self.world_position = camera.world_position
        self.scale = camera.clip_plane_far / 2

if __name__  == '__main__':
    app = Ursina()
    Sky(texture='sky_sunset')
    camera.fov = 90
    EditorCamera()
    app.run()