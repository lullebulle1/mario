from ursina import *
import time
from ursina.prefabs.health_bar import HealthBar
app = Ursina()
#import


class Player(Entity):

    def update(self):
        hp = 100
        hb = HealthBar(bar_color=color.lime, roundness = .5, scale=(.5, .04))
        hb.value = hp

        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a'])
            ).normalized()  # get the direction we're trying to walk in.

        origin = self.world_position + (self.up*.5) # the ray should start slightly up from the ground so we can walk up slopes or walk over small objects.
        hit_info = raycast(origin , self.direction, ignore=(self,), distance=.5, debug=False)
        if not hit_info.hit:
            self.position += self.direction * 5 * time.dt
        if hit_info.hit:
            hp -= 5 
            time.sleep(1)
Player(model='cube', origin_y=-.5, color=color.orange)
wall_left = Entity(model='cube', collider='box', scale_y=3, origin_y=-.5, color=color.azure, x=-4)
wall_right = duplicate(wall_left, x=4)
camera.y = 2



app.run()