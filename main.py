from pygame import *
from random import randint 
 

R = 500
W = 700
window = display.set_mode((W, R))

clock = time.Clock()

FPS = 60

clock.tick(FPS)

display.update()

run = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_x, player_y, player_speed, widght, height):
        super().__init__()
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def __init__(self, color_1, color_2, color_3, wall_width, wall_height, wall_x, wall_y):
        self.color_1 = color_1
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall_picture(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
wall1 = Player(36, 255, 248, 20, 120, 20, 180)
wall2 = Player(36, 255, 248, 20, 120, 660, 180)
window.fill((0,0,255))

#covalent
speed = 10


while run:
    window.fill((255,255,255))

    keys = key.get_pressed()
    for e in event.get(): 
        if e.type == QUIT: 
            run = False
    keys = key.get_pressed()
    if keys[K_s] and wall1.rect.y < 400:
        print(wall1.rect.y)
        wall1.rect.y += speed
    if keys[K_w] and wall1.rect.y > 0:
        print(wall1.rect.y)
        wall1.rect.y -= speed

    if keys[K_DOWN] and wall2.rect.y < 400:
        wall2.rect.y += speed
    if keys[K_UP] and wall2.rect.y > 0:
        wall2.rect.y -= speed

    wall1.draw_wall_picture()
    wall2.draw_wall_picture()

    
    display.update()
    clock.tick(FPS)