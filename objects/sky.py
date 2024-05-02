from ursina import *


class Sky(Entity):
    """
    Clase que representa el cielo en el juego.
    """

    def __init__(self, **kwargs):
        """
         Constructor de la clase Sky.

         Parámetros:
             **kwargs: Argumentos clave adicionales para personalizar el cielo.

         Retorna:
             None
         """
        from ursina.shaders import unlit_shader
        super().__init__(parent=render, name='sky', model='sky_dome',
                         texture='sky.webp', scale=9900, shader=unlit_shader)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self) -> None:
        """
        Método para actualizar la posición y el tamaño del cielo.

        Parámetros:
            None

        Retorna:
            None
        """
        self.world_position = camera.world_position
        self.scale = camera.clip_plane_far / 2
