from ursina import *
from elements.forest_track import ForestTrack
from elements.track import Track
from elements.car import Player

ROTATION_SPEED = 50
PLAYER_INITIAL_SPEED = 0
PLAYER_ACCELERATION = 15
PLAYER_DECELERATION = 5
PLAYER_BREAK = 50


def deaccelerate():
    global curr_speed
    if curr_speed > 0:
        curr_speed -= PLAYER_DECELERATION * time.dt
    elif curr_speed < 0:
        curr_speed += PLAYER_DECELERATION * time.dt


app = Ursina()

ground = ForestTrack()

player = Player().entity
curr_speed = PLAYER_INITIAL_SPEED


def update():
    global curr_speed
    if held_keys['w']:
        curr_speed += PLAYER_ACCELERATION * time.dt
        if curr_speed < 0:
            curr_speed += PLAYER_BREAK * time.dt

    if held_keys['s']:
        curr_speed -= PLAYER_ACCELERATION * time.dt
        if curr_speed > 0:
            curr_speed -= PLAYER_BREAK * time.dt
    else:
        deaccelerate()
    player.position += player.forward * curr_speed * time.dt

    if curr_speed > 0:
        if held_keys['a']:
            player.rotation_y -= ROTATION_SPEED * time.dt
            deaccelerate()
        if held_keys['d']:
            player.rotation_y += ROTATION_SPEED * time.dt
            deaccelerate()
    if curr_speed < 0:
        if held_keys['a']:
            player.rotation_y += ROTATION_SPEED * time.dt
            deaccelerate()
        if held_keys['d']:
            player.rotation_y -= ROTATION_SPEED * time.dt
            deaccelerate()

    if curr_speed < 0.05 and curr_speed > -0.05:
        curr_speed = 0


app.run()
