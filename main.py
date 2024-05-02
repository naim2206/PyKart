from ursina import *
import random
from objects.car import Car, CarGroup, PlayerCar
from objects.timer import Timer
from objects.track import Track

CAR_LINES = [-0.38, -0.23, -0.09, 0.05, 0.19, 0.33]


def update() -> None:
    """
    Función para actualizar la lógica del juego en cada fotograma.

    Esta función maneja la lógica principal del juego, incluyendo la
    actualización del tiempo, la posición de la textura de la pista,
    la detección de colisiones entre los coches y
    la acción resultante en caso de colisión.
    """
    global offset, track

    offset += time.dt * 0.3
    track.texture_offset = (0, offset)

    if held_keys['1']:
        track.texture = 'assets/track1.jpg'
    if held_keys['2']:
        track.texture = 'assets/track2.jpg'
    if held_keys['3']:
        track.texture = 'assets/track3.jpg'


def main() -> None:
    """
    Función principal del juego.

    Esta función inicializa el juego después de hacer clic en el botón de jugar.
    """
    global offset, track, app, play_button, track1, track2, track3
    destroy(play_button)
    destroy(track1)
    destroy(track2)
    destroy(track3)
    cars_img = ['assets/car0.png', 'assets/car1.png', 'assets/car2.png',
                'assets/car3.png', 'assets/car4.png']

    track.texture = texture

    car0 = PlayerCar(cars_img[0], (.05, 1, -.12), 0, track)
    car1 = Car(cars_img[1], (CAR_LINES[0], 1, random.uniform(3, 5)), 0,
               track, random.uniform(0.2, 0.4))
    car2 = Car(cars_img[2], (CAR_LINES[1], 1, random.uniform(1, 1.5)), 0,
               track, random.uniform(0.3, 0.4))
    car3 = Car(cars_img[3], (CAR_LINES[2], 1, random.uniform(0.5, 2)), 0,
               track, random.uniform(0.2, 0.45))
    car4 = Car(cars_img[4], (CAR_LINES[3], 1, random.uniform(1, 2)), 180,
               track, random.uniform(0.25, 0.45))
    car5 = Car(cars_img[1], (CAR_LINES[4], 1, random.uniform(0.5, 2)), 180,
               track, random.uniform(0.2, 0.4))
    car6 = Car(cars_img[2], (CAR_LINES[5], 1, random.uniform(3, 5)), 180,
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
    sky = Sky()


def show_menu() -> None:
    """
     Muestra el menú inicial del juego.

     Esta función configura y muestra los botones de inicio del juego.
     """
    global offset, track, play_button, track1, track2, track3, texture
    offset = 0
    track = Track(texture)

    play_button = Button('Play', on_click=main, scale=(0.2, 0.1), y=0.3)
    play_button.text_entity.scale *= 2
    track1 = Button(texture='./assets/track1',
                    on_click=lambda: change_texture(1),
                    scale=(
                        0.2, 0.2),
                    x=-0.5, color=color.blue)
    track2 = Button(texture='./assets/track2',
                    on_click=lambda: change_texture(2),
                    scale=(0.2, 0.2),
                    x=0, color=color.blue)
    track3 = Button(texture='./assets/track3',
                    on_click=lambda: change_texture(3),
                    scale=(0.2, 0.2),
                    x=0.5, color=color.blue)
    track1.color = color.green
    track2.color = color.white
    track3.color = color.white


def change_texture(track_number: int) -> None:
    """
    Cambia la textura de la pista.

    Esta función cambia la textura de la pista según el botón de textura
    seleccionado.
    """
    global texture, track1, track2, track3

    texture_paths = ['./assets/track1.jpg', './assets/track2.jpg',
                     './assets/track3.jpg']
    texture = texture_paths[track_number - 1]
    for i, button in enumerate([track1, track2, track3]):
        button.color = color.green if i == (
                track_number - 1) else color.white


if __name__ == '__main__':
    app = Ursina()
    window.fullscreen = True
    play_button = None
    offset = None
    track = None
    track1 = None
    track2 = None
    track3 = None
    texture = './assets/track1.jpg'
    show_menu()

    app.run()
