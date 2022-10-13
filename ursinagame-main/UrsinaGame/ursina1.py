#imports
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d


#setup
app = Ursina()

#classes

class Music:
    def init(self):
        pass

    def maintheme(self):
        Audio(sound_file_name="sounds/kurikitakati.mp3", pitch = 1, loop = True, autoplay = True)
        



class Player:
    def init(self):
        pass

    def body(self):
        player = PlatformerController2d(texture = "img/sprites/pngegg.png",y=-2, scale_y=2)
        camera.add_script(SmoothFollow(target=player, offset=[0,5,-45], speed=4))

class key:
    def update(key):                 
        if key == 'w': # checking particular key
            Audio(sound_file_name="sounds/mexico.mp3", pitch = 1, loop = True)
    
                
class Grounds:
    def innit(self):
        pass

    def ground(self):
        Entity(model='quad', y=-4, scale_x=40, collider='box', texture = "img/gameobjects/ground.png")

    def box_line(self):
        Entity(model='cube', color=color.white, y=20, x=35, scale_y=10, scale=(2.5,2.5), collider="box", texture= "img/gameobjects/woodcrate.jpg")
        Entity(model='cube', color=color.white, y=20, x=37.5, scale_y=10, scale=(2.5,2.5), collider="box", texture= "img/gameobjects/woodcrate.jpg")
        Entity(model='cube', color=color.white, y=20, x=40, scale_y=10, scale=(2.5,2.5), collider="box", texture= "img/gameobjects/woodcrate.jpg")
        Entity(model='cube', color=color.white, y=20, x=42.5, scale_y=10, scale=(2.5,2.5), collider="box", texture= "img/gameobjects/woodcrate.jpg")
        

    def box(self):
        #varje övre rad hoppar med 4.5
        #varje undre rad hoppar med 4.5
        #alla x hoppar med 5 åt de hållet man vill att nästa låda ska vara. 
        Entity(model='cube', color=color.white, y=-2.5, x=5, scale_y=10, scale=(2.5,2.5), collider="box", texture= "img/gameobjects/woodcrate.jpg")
        Entity(model='cube', color=color.white, y=0, x=5, scale_y=10, scale=(2.5,2.5), collider="box", texture= "img/gameobjects/woodcrate.jpg")

        Entity(model='cube', color=color.white, y=2, x=10, scale_y=10, scale=(2.5,2.5), collider="box", texture= "img/gameobjects/woodcrate.jpg")
        Entity(model='cube', color=color.white, y=4.5, x=10, scale_y=10, scale=(2.5,2.5), collider="box", texture= "img/gameobjects/woodcrate.jpg")

        Entity(model='cube', color=color.white, y=6.5, x=15, scale_y=10, scale=(2.5,2.5), collider="box", texture= "img/gameobjects/woodcrate.jpg")
        Entity(model='cube', color=color.white, y=9, x=15, scale_y=10, scale=(2.5,2.5), collider="box", texture= "img/gameobjects/woodcrate.jpg")

        Entity(model='cube', color=color.white, y=11, x=20, scale_y=10, scale=(2.5,2.5), collider="box", texture= "img/gameobjects/woodcrate.jpg")
        Entity(model='cube', color=color.white, y=13.5, x=20, scale_y=10, scale=(2.5,2.5), collider="box", texture= "img/gameobjects/woodcrate.jpg")
        
        Entity(model='cube', color=color.white, y=15.5, x=25, scale_y=10, scale=(2.5,2.5), collider="box", texture= "img/gameobjects/woodcrate.jpg")
        Entity(model='cube', color=color.white, y=18, x=25, scale_y=10, scale=(2.5,2.5), collider="box", texture= "img/gameobjects/woodcrate.jpg")
        
        Entity(model='cube', color=color.white, y=20, x=30, scale_y=10, scale=(2.5,2.5), collider="box", texture= "img/gameobjects/woodcrate.jpg")
        Entity(model='cube', color=color.white, y=22.4, x=30, scale_y=10, scale=(2.5,2.5), collider="box", texture= "img/gameobjects/woodcrate.jpg")






m = Music()
p = Player()
g = Grounds()
k = key()

#gameloop
if __name__ == "__main__":
    Sky()
    m.maintheme()
    g.box()
    g.box_line()
    g.ground()
    p.body()
    k.update()
    



    app.run()