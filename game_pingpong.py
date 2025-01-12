from pygame import *

class GameSprite(sprite.Sprite):
    '''класс родитель для спрайтов'''

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        '''конструктор класса'''
        super().__init__()
        # каждый спрайт хранит изображение image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        # каждый спрайт - это прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        '''отобразить персонажа'''
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    '''клас наследник для спрайта игроки(управляется стрелками)'''

    def move_left(self):
        '''перемещение игрока клавишами'''
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

    def move_right(self):
        '''перемещение игрока клавишами'''
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed


# создаем окно игры
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-pong')
background = transform.scale(image.load('pingpong.png'), (win_width, win_height))

racket1 = Player('rokket.png', 10, 200, 75, 125,  20)
racket2 = Player('rokket.png', 520, 200, 75, 125,  20)
ball = GameSprite('ball.png', 200, 200, 70, 50, 50)

game = True
finish =False
clock = time.Clock()
FPS = 30

font.init()
font_sample = font.Font(None, 35)
lose1 = font_sample.render('ИГРОК 2 ПРОИГРАЛ', True, 'brown1')
lose2 = font_sample.render('ИГРОК 1 ПРОИГРАЛ', True, 'brown1')


speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x < 0:
            finish = True
            window.blit(lose2, (200, 200))

        racket1.move_left()
        racket2.move_right()

        ball.rect.x += speed_x
        ball.rect.y += speed_y


        racket1.reset()
        racket2.reset()
        ball.reset()


    display.update()
    clock.tick(FPS)