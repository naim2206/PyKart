from ursina import *


class Timer(Text):
    elapsed_time = 0
    collision = False

    def __init__(self, text='Time: 0', scale=0.1,
                 origin=(1.5, -8)):
        super().__init__()
        self.text = text
        self.scale = scale
        self.origin = origin

    def update(self):
        """
        Función para actualizar la lógica del juego en cada fotograma.

        Esta función maneja la lógica principal del juego, incluyendo la actualización del tiempo,
        la posición de la textura de la pista, la detección de colisiones entre los coches y
        la acción resultante en caso de colisión.
        """
        if not self.collision:
            self.elapsed_time += time.dt
            self.text = f'Time: {self.elapsed_time:.2f}'
