from ursina import *


class Timer(Text):
    """
    Clase que representa un temporizador de juego.

    Esta clase hereda de la clase Text del módulo Ursina y se utiliza para mostrar
    el tiempo transcurrido en la pantalla durante el juego.
    """
    elapsed_time = 0
    collision = False

    def __init__(self, text='Time: 0', scale=2, origin=(0, 0)):
        """
        Constructor de la clase Timer.

        Args:
            text (str): El texto inicial que se mostrará en el temporizador.
            scale (float): Escala del texto del temporizador.
            origin (tuple): Coordenadas (x, y) del origen del texto del
            temporizador.

        Este constructor inicializa un temporizador con el texto, la escala y
        la posición especificados (o los valores predeterminados si no se
        proporcionan).
        """
        super().__init__()
        self.text = text
        self.scale = scale
        self.origin = origin
        self.y = 0.4
        self.x = -0.6
        self.color = color.black

    def update(self) -> None:
        """
        Función para actualizar la lógica del juego en cada fotograma.

        Esta función maneja la lógica principal del juego, incluyendo la
        actualización del tiempo, la posición de la textura de la pista,
        la detección de colisiones entre los coches y la acción resultante
        en caso de colisión.
        """
        if not self.collision:
            self.elapsed_time += time.dt
            self.text = f'Time: {self.elapsed_time:.2f}'
