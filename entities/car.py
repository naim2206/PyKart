from ursina import *
import random


class Singleton:
    INSTANCES = {}


def singleton(clase):
    def obtener_instancia(*args, **kwargs):
        if clase not in Singleton.INSTANCES:
            Singleton.INSTANCES[clase] = clase(*args, **kwargs)
        return Singleton.INSTANCES[clase]

    return obtener_instancia


class Car(Entity):
    ENEMY_CAR_SPEED_FRONT = [0.01, 0.09]
    ENEMY_CAR_SPEED_BACK = [0.05, 0.14]
    ENEMY_ACCELERATION = 0.0001

    def __init__(self, img, position, angle, track):
        super().__init__()
        self.parent = track
        self.model = 'cube'
        self.texture = img
        self.scale = (random.uniform(0.07, 0.1), 0.0001, 0.06)
        self.position = position
        self.collider = 'box'
        self.rotation_y = angle

    def update(self):
        # for car1 and car2
        if self.rotation_y == 0:
            self.z -= time.dt * random.uniform(self.ENEMY_CAR_SPEED_FRONT[0],
                                               self.ENEMY_CAR_SPEED_FRONT[1])
            self.ENEMY_CAR_SPEED_FRONT[0] -= self.ENEMY_ACCELERATION
            self.ENEMY_CAR_SPEED_FRONT[1] -= self.ENEMY_ACCELERATION
        else:  # for car3 and car4
            self.z -= time.dt * random.uniform(self.ENEMY_CAR_SPEED_BACK[0],
                                               self.ENEMY_CAR_SPEED_BACK[1])
            self.ENEMY_CAR_SPEED_BACK[0] += self.ENEMY_ACCELERATION
            self.ENEMY_CAR_SPEED_BACK[1] += self.ENEMY_ACCELERATION

        if self.z < -0.3:
            self.z = 0.4
        if self.z > 0.5:
            self.z = -0.3


@singleton
class PlayerCar(Car):
    def __init__(self, img, position, angle, track):
        super().__init__(img, position, angle, track)
        self.scale = (0.2, self.scale_y, self.scale_z)

    def update(self):
        self.x += held_keys['d'] * time.dt * 0.2
        self.x -= held_keys['a'] * time.dt * 0.2

        if self.x >= 0.24:
            self.x = 0.24
        if self.x <= -0.28:
            self.x = -0.28
