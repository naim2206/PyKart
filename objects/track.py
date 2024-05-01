from ursina import *


class Track(Entity):
    """
    Clase para representar la pista en el juego.

    Hereda de la clase Entity de Ursina.

    Atributos:
    - model (str): El modelo utilizado para representar la pista.
    - scale (Vec3): La escala de la pista en los ejes x, y, z.
    - position (Vec3): La posición inicial de la pista en el mundo.
    - texture (str): La ruta de la textura aplicada a la pista.
    """

    def __init__(self, texture_selected: str):
        """
        Constructor de la clase Track.
        """
        super().__init__()
        self.model = 'cube'
        self.scale = (10, .5, 60)
        self.position = (0, 0)
        self.texture = texture_selected
