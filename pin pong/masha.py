from pygame import *
from random import *

window = display.set_mode((700,500))#создаю окно
display.set_caption('pygame window')#устанавливаю название окна
fon=transform.scale(image.load("pin_pong.avif"),(700,500))

clock= time.Clock()
FPS=60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image= transform.scale(image.load(player_image),(size_x, size_y))
        self.speed=player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y  
        self.direction = 'left'   
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 3:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 700 - 50:
            self.rect.y += self.speed

class Player_2(GameSprite):   
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 3:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < 500:
            self.rect.y += self.speed

finish = False

speed_x = 3
speed_y = 3

raketca_1 = Player('racetka_1.jpg', 20, 350, 5, 50, 50)
raketca_2 = Player_2('racetka_2.jpg', 680, 350, 5, 50, 50)
ball = GameSprite('baascet.jpg', randint(150, 520), randint(150,300),4,50,50)

font.init()
font2 = font.SysFont(None,36)

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game= False

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > 500-50 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(raketca_1, ball) or sprite.collide_rect(raketca_2, ball):
        speed_x *= -1


    if not finish:
            window.blit(galaxy,(0,0))
            raketca_1.reset()
            raketca_1.update()
            
            raketca_2.reset()
            raketca_2.update()
            
            ball.reset()
           
    
    if ball.rect.x < 0:
        finish = True
        win = font2.render('player_2 win' , 1, (0,255,0))
        window.blit(lose,(250,250)) 

    elif ball.rect.x > 700:
        finish = True
        win = font2.render('player_1 win' , 1, (0,255,0))
        window.blit(lose,(250,250)) 

        



    display.update()
    clock.tick(FPS) 





