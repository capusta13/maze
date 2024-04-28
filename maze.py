from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,  player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= 10
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += 10
        if keys_pressed[K_RIGHT] and self.rect.x < 600:
            self.rect.x += 10
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= 10
            
class Enemy(GameSprite):
    def move(self):
        if self.rect.x > 600:
            self.speed *= -1
        if self.rect.x < 500:
            self.speed *= -1
        self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, wall_width, wall_height, wall_x, wall_y):
       super().__init__()
       self.color_1 = color_1
       self.width = wall_width
       self.heigth = wall_height
       self.image1 = Surface((self.width, self.heigth))
       self.image1.fill(self.color_1)
       self.rect = self.image1.get_rect()
       self.rect.x = wall_x
       self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image1, (self.rect.x, self.rect.y))
        window.blit(self.image1, (self.rect.x, self.rect.y))


#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Изображение')
#задай фон сцены
background = transform.scale(image.load('background.jpg'), (700, 500))
x1 = 200
x2 = 500
y1 = 130
y2 = 250
x3 = 550
y3 = 400

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound("money.ogg")


        
FPS = 60
clock = time.Clock() 

hero = Player('hero.png', x1, y1, 10)
hero2 = Player('hero.png', 200, 200, 10)
cyborg = Enemy('cyborg.png', x2, y2, 3) 
treasure = GameSprite('treasure.png', x3, y3, 10)

wall1 = Wall((255, 255, 0), 100, 10, 250, 300)
wall2 = Wall((255, 255, 0), 200, 10, 50, 50)
wall3 = Wall((255, 255, 0), 10, 300, 50, 50)
wall4 = Wall((255, 255, 0), 10, 250, 250, 50)
wall5 = Wall((255, 255, 0), 10, 250, 160, 140)
wall6 = Wall((255, 255, 0), 209, 10, 177, 371)

game = True
while game:
    hero.move()
    hero2.move()
    cyborg.move()
    
    clock.tick(FPS)
    window.blit(background, (0, 0))
    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
    wall4.draw_wall()
    wall5.draw_wall()
    wall6.draw_wall()
    hero.reset()
    hero2.reset()
    cyborg.reset()
    treasure.reset()
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    if sprite.collide_rect(hero, treasure):
        money.play()
        game = False
    
    display.update()
#создай 2 спрайта и размести их на сцене
#обработай событие «клик по кнопке "Закрыть окно"»
