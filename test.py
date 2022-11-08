import pygame
import random
pygame.init()
class Plane(pygame.sprite.Sprite):
    def __init__(self,screen,image_fill,location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load(image_fill)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > height:
            self.rect.bottom = height
    def blit(self):
        self.screen.blit(self.image,self.rect)
class Monster(pygame.sprite.Sprite):
    def __init__(self,screen,image_fill,location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load(image_fill)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed = speed
        self.hp = 3
    def move(self):
        global score
        self.rect = self.rect.move(self.speed)
        if self.rect.top >= height:
            self.kill()
        if self.hp <= 0:
            self.kill()
            score = score + 1
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > width:
            self.rect.right = width
    def blit(self):
        self.screen.blit(self.image,self.rect)
width = 400
height = 800
monster_time = 0
key_list = []
screen = pygame.display.set_mode([width,height])
plane = Plane(screen,"img/fly_4.png",[175,750],[0,0])
monster = Monster(screen,"img/monsters.png",[0,0],[0,0])
monsters = pygame.sprite.Group()
#pygame.key.set_repeat(100,10)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                key_list.remove("K_UP")
            elif event.key == pygame.K_DOWN:
                key_list.remove("K_DOWN")
            elif event.key == pygame.K_LEFT:
                key_list.remove("K_LEFT")
            elif event.key == pygame.K_RIGHT:
                key_list.remove("K_RIGHT")
    if "K_UP" in key_list:
        plane.rect.top-=3
    if "K_DOWN" in key_list:
        plane.rect.top+=3
    if "K_LEFT" in key_list:
        plane.rect.left-=3
    if "K_RIGHT" in key_list:
        plane.rect.left+=3
    if monster_time>= 25:
        monster = Monster(screen, "img/monsters.png", [random.randint(0,width-75),-75], [0, 5])
        monsters.add(monster)
        monster_time = 0

    screen.fill([78,78,78])
    for monster in monsters:
        monster.blit()
        monster.move()
    print(monsters)
    monster_time += 1
    #monster.blit()
    #monster.move()
    plane.blit()
    plane.move()
    pygame.display.update()
    pygame.time.delay(10)
pygame.quit()
