from ursina import *
import random
from objects.car import Car, CarGroup, PlayerCar
from objects.timer import Timer
from objects.track import Track


def update():
    """
    Función para actualizar la lógica del juego en cada fotograma.

    Esta función maneja la lógica principal del juego, incluyendo la actualización del tiempo,
    la posición de la textura de la pista, la detección de colisiones entre los coches y
    la acción resultante en caso de colisión.
    """
    # global offset, collision, elapsed_time
    global offset

    # car_group.check_for_collision(car0)

    # if not collision:
    #    elapsed_time += time.dt
    #    timer_text.text = f'Time: {elapsed_time:.2f}'

    offset += time.dt * 0.3
    track.texture_offset = (0, offset)


app = Ursina()
# collision = False

# timer_text = Text(text='Time: 0', scale=0.1, origin=(1.5, -8))

# elapsed_time = 0

cars_img = ['assets/car0.png', 'assets/car1.png', 'assets/car2.png',
            'assets/car3.png', 'assets/car4.png']

track = Track()
car_lines = [-0.38, -0.23, -0.09, 0.05, 0.19, 0.33]
car0 = PlayerCar(cars_img[0], (.05, 1, -.12), 0, track)
car1 = Car(cars_img[1], (car_lines[0], 1, random.uniform(3, 5)), 0,
           track, random.uniform(0.2, 0.4))
car2 = Car(cars_img[2], (car_lines[1], 1, random.uniform(1, 1.5)), 0,
           track, random.uniform(0.3, 0.4))
car3 = Car(cars_img[3], (car_lines[2], 1, random.uniform(0.5, 2)), 0,
           track, random.uniform(0.2, 0.45))
car4 = Car(cars_img[4], (car_lines[3], 1, random.uniform(1, 2)), 180,
           track, random.uniform(0.25, 0.45))
car5 = Car(cars_img[1], (car_lines[4], 1, random.uniform(0.5, 2)), 180,
           track, random.uniform(0.2, 0.4))
car6 = Car(cars_img[2], (car_lines[5], 1, random.uniform(3, 5)), 180,
           track, random.uniform(0.2, 0.7))

timer = Timer()
car_group = CarGroup(car0, timer)
car_group.add_car(car1)
car_group.add_car(car2)
car_group.add_car(car3)
car_group.add_car(car4)
car_group.add_car(car5)
car_group.add_car(car6)

offset = 0

camera.position = (0, 8, -26)
camera.rotation_x = 20
app.run()
