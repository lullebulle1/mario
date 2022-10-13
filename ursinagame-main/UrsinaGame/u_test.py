from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()


#menuscreen
window.title = "lol"
window.fullscreen = True
player = PlatformerController2d(y=1, z=.01, scale_y = 1, color = color.red)
ground=Entity(model="quad", y = -2, scale_X = 10, collider = "box", color = color.green)

app.run()