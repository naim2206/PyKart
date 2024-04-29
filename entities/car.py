from ursina import *
import random


class Singleton:
    """
    Clase Singleton que garantiza que solo haya una instancia de cada clase específica.
    
    Atributos:
    - INSTANCES (dict): Un diccionario para almacenar las instancias únicas de las clases.
    """
    INSTANCES = {}

def singleton(clase):
    """
    Decorador para convertir una clase en un Singleton.

    Parámetros:
    - clase (type): La clase que se convertirá en Singleton.

    Retorna:
    - función: La función que maneja la lógica de instancia única para la clase.
    """
    def obtener_instancia(*args, **kwargs):
        """
        Función interna para obtener la instancia única de la clase.

        Parámetros:
        - *args: Argumentos posicionales que se pasan a la clase.
        - **kwargs: Argumentos de palabras clave que se pasan a la clase.

        Retorna:
        - objeto: La instancia única de la clase.
        """
        if clase not in Singleton.INSTANCES:
            Singleton.INSTANCES[clase] = clase(*args, **kwargs)
        return Singleton.INSTANCES[clase]

    return obtener_instancia

class Car(Entity):
    """
    Clase para representar un coche en el juego.

    Atributos:
    - img (str): La ruta de la textura del coche.
    - position (Vec3): La posición inicial del coche.
    - angle (float): El ángulo de rotación inicial del coche.
    - track (Entity): La pista a la que pertenece el coche.
    """
    ENEMY_ACCELERATION = 0.0001

    
    def __init__(self, img, position, angle, track, speed):
        """
        Constructor de la clase Car.

        Parámetros:
        - img (str): La ruta de la textura del coche.
        - position (Vec3): La posición inicial del coche.
        - angle (float): El ángulo de rotación inicial del coche.
        - track (Entity): La pista a la que pertenece el coche.
        """
        super().__init__()
        self.parent = track
        self.model = 'cube'
        self.texture = img
        self.scale = (random.uniform(0.07, 0.1), 0.0001, 0.06)
        self.position = position
        self.collider = 'box'
        self.rotation_y = angle
        self.speed = speed 
        
        # Definir velocidades aleatorias
        self.ENEMY_CAR_SPEED_FRONT = [random.uniform(0.01, 0.09), random.uniform(0.1, 0.2)]
        self.ENEMY_CAR_SPEED_BACK = [random.uniform(0.05, 0.14), random.uniform(0.15, 0.25)]
    
    def update(self):
        """
        Método para actualizar la posición del coche en cada fotograma del juego.
        """
        if self.rotation_y == 0:
            self.z -= time.dt * self.speed
            self.ENEMY_CAR_SPEED_FRONT[0] -= self.ENEMY_ACCELERATION
            self.ENEMY_CAR_SPEED_FRONT[1] -= self.ENEMY_ACCELERATION
        else:  # for car3 and car4
            self.z -= time.dt * self.speed
            self.ENEMY_CAR_SPEED_BACK[0] += self.ENEMY_ACCELERATION
            self.ENEMY_CAR_SPEED_BACK[1] += self.ENEMY_ACCELERATION

        if self.z < -0.3:
            self.speed = random.uniform(0.3, 0.6)
            self.z = 0.4
        if self.z > 0.5:
            self.speed = random.uniform(0.3, 0.6)
            self.z = -0.3


@singleton
class PlayerCar(Car):
    """
    Clase singleton para representar el coche del jugador.

    Hereda de la clase Car.

    Atributos:
    - img (str): La ruta de la textura del coche.
    - position (Vec3): La posición inicial del coche.
    - angle (float): El ángulo de rotación inicial del coche.
    - track (Entity): La pista a la que pertenece el coche.
    """
    def __init__(self, img, position, angle, track):
        """
        Constructor de la clase PlayerCar.

        Parámetros:
        - img (str): La ruta de la textura del coche.
        - position (Vec3): La posición inicial del coche.
        - angle (float): El ángulo de rotación inicial del coche.
        - track (Entity): La pista a la que pertenece el coche.
        """
        super().__init__(img, position, angle, track,0)
        self.scale = (0.2, self.scale_y, self.scale_z)

    def update(self):
        """
        Método para actualizar la posición del coche del jugador en cada fotograma del juego.
        """
        self.x += held_keys['d'] * time.dt * 0.4
        self.x -= held_keys['a'] * time.dt * 0.4

        if self.x >= 0.38:
            self.x = 0.38
        if self.x <= -0.33:
            self.x = -0.33
            
class CarGroup:
    """
    Clase que representa un grupo de coches.
    """
    def __init__(self):
        self._cars = []

    def add_car(self, car):
        """
        Método para añadir un coche al grupo.
        """
        self._cars.append(car)

    def update_all(self):
        """
        Método para actualizar todos los coches en el grupo.
        """
        for car in self._cars:
            car.update()
            
    def check_for_collision(self, car0):
        global collision
        for car in self._cars:
            if abs(car0.x - car.x) < 0.05:
                if abs(car0.z - car.z) < 0.05:
                    collision = True
                    Text(text='Game over', scale=0.3, origin=(0, 0))
                    car0.disable()
