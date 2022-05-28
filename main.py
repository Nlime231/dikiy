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

class GameSprite_ball(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (40, 40))
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
wall1 = Player(36, 255, 248, 20, 120, -5, 180)
wall2 = Player(36, 255, 248, 20, 120, 685, 180)
ball = GameSprite_ball("ball.png", 350, 230, 3)
window.fill((0,0,255))


mode_speed_x2 = False
mode_speed_x3 = False
fast_ball = False
very_fast_ball = False
slowmode = False
font.init()
font1 = font.Font(None, 35)
font2 = font.Font(None, 20)
font3 = font.Font(None, 15)
scorelist = "0:0"
text_win_score = font1.render(scorelist, 1, (255, 255,255))
text_mode = font2.render("", 1, (255, 255,255))
text_pause = font2.render("", 1, (255, 255,255))
window.blit(text_win_score,(250,10))
text_git = font3.render("Check 'README' on github for keybindings and mods.", 1, (255, 255,255))
#covalent
speed = 10
ball_speed_x = 3
ball_speed_y = 3
winner_score_2 = 0
winner_score_1 = 0
Game = True 
pause = False
while run:
    if Game == False:
        speed = 3
        ball_speed_x = 0
        ball_speed_y = 0
    window.fill((0,0,0))
    keys = key.get_pressed()
    for e in event.get(): 
        if e.type == QUIT: 
            run = False
    keys = key.get_pressed()
    if keys[K_s] and wall1.rect.y < 400:
        wall1.rect.y += speed
    if keys[K_w] and wall1.rect.y > 0:
        wall1.rect.y -= speed

    if keys[K_DOWN] and wall2.rect.y < 400:
        wall2.rect.y += speed
    if keys[K_UP] and wall2.rect.y > 0:
        wall2.rect.y -= speed
    if keys[K_x]:
        if pause == False:
            if mode_speed_x2 == False:
                speed = 10
                ball_speed_x = 3
                ball_speed_y = 3
                speed *= 2
                ball_speed_x *= 2
                ball_speed_y *= 2
                mode_speed_x2 = True
                text_mode = font2.render("Mode: X2 speed all. (off - z)", 1, (255, 255,255))
                mode_speed_x3 = False
                fast_ball = False
                very_fast_ball = False
                slowmode = False
    if keys[K_z]:
        if pause == False:
            speed = 10
            ball_speed_x = 3
            ball_speed_y = 3
            mode_speed_x2 = False
            mode_speed_x3 = False
            text_mode = font2.render("", 1, (255, 255,255))
    if keys[K_c]:
        if pause == False:
            if mode_speed_x3 == False:
                speed = 10
                ball_speed_x = 3
                ball_speed_y = 3
                speed *= 3
                ball_speed_x *= 3
                ball_speed_y *= 3
                mode_speed_x3 = True
                text_mode = font2.render("Mode: X3 speed all. (off - z)", 1, (255, 255,255))
                mode_speed_x3 = True
                mode_speed_x2 = False
                fast_ball = False
                very_fast_ball = False
                slowmode = False
    if keys[K_p]:
        if pause == False:
            last_speed = speed
            last_ball_speed_x = ball_speed_x
            last_ball_speed_y = ball_speed_y
            speed = 0
            ball_speed_x = 0
            ball_speed_y = 0
            text_pause = font2.render("Paused - Unpause [O]", 1, (255, 255,255))
            pause = True
    if keys[K_v]:
        if pause == False:
            if fast_ball == False:
                ball_speed_x = 3
                ball_speed_y = 3
                ball_speed_x = ball_speed_x*2
                ball_speed_y = ball_speed_y*2
                text_mode = font2.render("Mode: FastBall [x2]. (off - z)", 1, (255, 255,255))
                fast_ball = True
    if keys[K_b]:
        if pause == False:
            if very_fast_ball == False:
                ball_speed_x = 3
                ball_speed_y = 3
                ball_speed_x = ball_speed_x*3
                ball_speed_y = ball_speed_y*3
                text_mode = font2.render("Mode: FastBall [x3]. (off - z)", 1, (255, 255,255))
                very_fast_ball = True
                mode_speed_x2 = False
                mode_speed_x3 = False
                fast_ball = False
                slowmode = False
    if keys[K_o]:
        if pause:
            speed = last_speed
            ball_speed_x = last_ball_speed_x
            ball_speed_y = last_ball_speed_y
            text_pause = font2.render("", 1, (255, 255,255))
            pause = False
    if keys[K_n]:
        if slowmode == False:
            speed = 10
            ball_speed_x = 3
            ball_speed_y = 3
            speed = speed*0.5
            ball_speed_x = ball_speed_x*0.5
            ball_speed_y = ball_speed_y*0.5
            text_mode = font2.render("Mode: Slow [x2]. (off - z)", 1, (255, 255,255))
            pause = False
            slowmode = True
            mode_speed_x2 = False
            mode_speed_x3 = False
            fast_ball = False
            very_fast_ball = False
    window.blit(text_git,(10,10))
    ball.rect.x += ball_speed_x
    ball.rect.y += ball_speed_y
    if ball.rect.y > R-50 or ball.rect.y < 0:
        ball_speed_y *= -1
    if ball.rect.y < 0 + 20 or ball.rect.y < 0:
        ball_speed_y *= -1
    if sprite.collide_rect(wall1,ball) or sprite.collide_rect(wall2, ball):
        ball_speed_x *= -1

    if ball.rect.x > W:
        winner_score_1 += 1
        scorelist = f"{winner_score_1}:{winner_score_2}"
        text_win_score = font1.render(scorelist, 1, (255, 255,255))
        ball.rect.x = 350
        ball.rect.y = 230
    if ball.rect.x < 0:
        winner_score_2 += 1
        scorelist = f"{winner_score_1}:{winner_score_2}"
        text_win_score = font1.render(scorelist, 1, (255, 255,255))

        ball.rect.x = 350
        ball.rect.y = 230

    if winner_score_1 == 5:
        text_win = font1.render("Игрок 1 Выйграл", 1, (255, 255,255))
        window.blit(text_win, (260,450))
        Game = False
    if winner_score_2 == 5:
        text_win = font1.render("Игрок 2 Выйграл", 1, (255, 255,255))
        window.blit(text_win, (260,450))
        Game = False
    wall1.draw_wall_picture()
    wall2.draw_wall_picture()
    ball.reset()
    window.blit(text_win_score,(330,10))
    window.blit(text_mode,(500,450))
    window.blit(text_pause,(500,420))
    display.update()
    clock.tick(FPS)