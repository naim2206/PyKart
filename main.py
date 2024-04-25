from ursina import *
import random
from entities.car import Car, PlayerCar
from entities.track import Track


def update():
    """
    Función para actualizar la lógica del juego en cada fotograma.

    Esta función maneja la lógica principal del juego, incluyendo la actualización del tiempo,
    la posición de la textura de la pista, la detección de colisiones entre los coches y
    la acción resultante en caso de colisión.
    """
    global offset, collision, elapsed_time

    if not collision:
        elapsed_time += time.dt
        timer_text.text = f'Time: {elapsed_time:.2f}'

    offset += time.dt * 0.3
    track.texture_offset = (0, offset)

    for car in cars:
        if abs(car0.x - car.x) < 0.05:
            if abs(car0.z - car.z) < 0.05:
                collision = True
                Text(text='Game over', scale=0.3, origin=(0, 0))
                car0.disable()


app = Ursina()
# window.color = color.orange
collision = False

timer_text = Text(text='Time: 0', scale=0.1, origin=(1.5, -8))

elapsed_time = 0

cars_img = ['assets/car0.png', 'assets/car1.png', 'assets/car2.png',
            'assets/car3.png', 'assets/car4.png']

track = Track()
car_lines = [0.05, 0.19, -0.09, -0.23]
car0 = PlayerCar(cars_img[0], (.05, 1, -.12), 0, track)
car1 = Car(cars_img[1], (car_lines[0], 1, random.uniform(0.1, 0.2)), 0, track)
car2 = Car(cars_img[2], (car_lines[1], 1, random.uniform(-0.12, 0.2)), 0, track)
car3 = Car(cars_img[3], (car_lines[2], 1, random.uniform(-0.12, 0.2)), 180,
           track)
car4 = Car(cars_img[4], (car_lines[3], 1, random.uniform(-0.12, 0.2)), 180,
           track)

cars = [car1, car2, car3, car4]

offset = 0

camera.position = (0, 8, -26)
camera.rotation_x = 20
app.run()
