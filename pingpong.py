from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width-80:
            self.rect.y += self.speed
    
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width-80:
            self.rect.y += self.speed

win_height = 500
win_width = 600
clock = time.Clock()
FPS = 60
speed_x = 3
speed_y = 3

window = display.set_mode((win_width, win_height))
background = (250, 255, 255)
window.fill(background)

font.init()
font = font.Font(None, 35)

lose1 = font.render('PLAYER 1 LOSE', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE', True, (180, 0, 0))

racket_1 = Player('racket.png', 30, 200, 50, 150, 4)
racket_2 = Player('racket.png', 520, 200, 50, 150, 4)

ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        window.fill(background)
        racket_1.update_L()
        racket_1.reset()
        racket_2.update_R()
        racket_2.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
    
        if sprite.collide_rect(racket_1, ball) or sprite.collide_rect(racket_2, ball):
            speed_x *= -1
            speed_y *= 1
        
        if ball.rect.y > win_height -50 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x > win_width:
            window.blit(lose2, (200, 200))
            finish = True
            
        
        if ball.rect.x < 0:
            window.blit(lose1, (200, 200))
            finish = True
        


    display.update()
    clock.tick(FPS)
