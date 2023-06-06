from pygame import *
window = display.set_mode((600, 500))
window.fill((255, 255, 255))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, speed, player_x ,player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (73,80))
        self.speed = speed
        self.rect  = self. image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_s] and self.rect.y < 550:
            self.rect.y += 10
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_DOWN] and self.rect.y < 550:
            self.rect.y += 10



run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    clock.tick(60)
    display.update()
