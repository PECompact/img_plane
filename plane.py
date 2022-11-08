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
key_list = []
monster_time = 0
bullet_time = 24
score = 100
f1_location = [25,25]
start_flag = False                              #游戏是否启动
start_image = 1                                 #游戏启动按钮状态
run_flag = True                                 #游戏是否正常运行/结束
pygame.mixer.init()
s1 = pygame.mixer.Sound("sounds/s_bullet.wav")
pygame.mixer.music.load("mp3/bg_music.mp3")
pygame.mixer.music.play(-1)
start1 = pygame.image.load("img/start1.png")
start2 = pygame.image.load("img/start2.png")
start3 = pygame.image.load("img/start3.png")
font1 = pygame.font.Font(None,50)
f1 = font1.render("score:"+str(score),1,[0,255,0])
screen = pygame.display.set_mode([width,height])
plane = Plane(screen,"img/fly_4.png",[175,750],[0,0])
#bullet = Plane(screen,"img/buttel",[plane.rect.centerx-5,plane.rect.top],[0,0])
bullets = pygame.sprite.Group()
bullets_left = pygame.sprite.Group()
bullets_right = pygame.sprite.Group()
monster = Monster(screen,"img/monsters.png",[0,0],[0,3])
monsters = pygame.sprite.Group()
#pygame.time.set_timer(pygame.USEREVENT,350)
#pygame.key.set_repeat(100,10)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            x,y = pygame.mouse.get_pos()
            if x>=300 and x<=350:           #通过获取的鼠标位置确定按钮是否抬起
                if y>=670 and y<=700:
                    start_image = 3
                else:
                    start_image = 1
            else:
                start_image = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if x >= 300 and x <= 350:  # 通过获取的鼠标位置确定按钮是否抬起
                if y >= 670 and y <= 700:
                    start_flag = True
                    run_flag = True
                    f1_location = [25,25]
                    score = 0
        if event.type == pygame.KEYDOWN:  # 按键按下则保存到列表
            if event.key == pygame.K_UP:
                key_list.append("K_UP")
            elif event.key == pygame.K_DOWN:
                key_list.append("K_DOWN")
            elif event.key == pygame.K_LEFT:
                key_list.append("K_LEFT")
            elif event.key == pygame.K_RIGHT:
                key_list.append("K_RIGHT")
            elif event.key == pygame.K_x:
                key_list.append("K_x")
        if event.type == pygame.KEYUP:  # 当按键松开则删除对应按键于列表中
            if event.key == pygame.K_UP:
                key_list.remove("K_UP")
            elif event.key == pygame.K_DOWN:
                key_list.remove("K_DOWN")
            elif event.key == pygame.K_RIGHT:
                key_list.remove("K_RIGHT")
            elif event.key == pygame.K_LEFT:
                key_list.remove("K_LEFT")
            elif event.key == pygame.K_x:
                key_list.remove("K_x")
                bullet_time = 24
    if "K_UP" in key_list:  # 通过列表中是否拥有按键判断上下左右
        if "K_DOWN" in key_list:
            if key_list.index("K_DOWN") > key_list.index("K_UP"):
                plane.rect.top += 3
            else:
                plane.rect.top -= 3
        else:
            plane.rect.top -= 3
    elif "K_DOWN" in key_list:
        plane.rect.top += 3
    #            if "K_UP" in key_eve:
    #                if key_eve.index("K_UP")>key_eve.index("K_DOWN"):
    #                    speed_y = -1
    #                else:
    #                    speed_y = 1
    #            else:
    #                speed_y = 1
    if "K_RIGHT" in key_list:
        if "K_LEFT" in key_list:
            if key_list.index("K_LEFT") > key_list.index("K_RIGHT"):
                plane.rect.left -= 5
            else:
                plane.rect.left += 5
        else:
            plane.rect.left += 5
    elif "K_LEFT" in key_list:
        plane.rect.left -= 5
    #           if "K_RIGHT" in key_eve:
    #                if key_eve.index("K_LEFT")<key_eve.index("K_RIGHT"):
    #                    speed_x = 1
    #                else:
    #                    speed_x = -1
    #            else:
    #                speed_x = -1
    screen.fill([78, 78, 78])
    if start_flag:
        if run_flag:
            if "K_x" in key_list:
                bullet_time+=1
                if bullet_time >= 25:
                    s1.play()
                    bullet = Plane(screen, "img/bullet.png", [plane.rect.centerx - 5, plane.rect.top], [0, -5])
                    bullet_l = Plane(screen, "img/bullet.png", [plane.rect.centerx - 15, plane.rect.top], [-1, -5])
                    bullet_r = Plane(screen, "img/bullet.png", [plane.rect.centerx + 10, plane.rect.top], [1, -5])
                    bullets.add(bullet)
                    bullets_left.add(bullet_l)
                    bullets_right.add(bullet_r)
                    bullet_time = 0
            monster_time += 1
            if monster_time >= 75:
                monster = Monster(screen, "img/monsters.png", [random.randint(0, width), -75], [0, 3])
                monsters.add(monster)
                monster_time = 0

            if pygame.sprite.spritecollide(plane,monsters,0):
                monsters.empty()
                run_flag = False
                f1_location = [int(width/2-100), int(height/2)]
            for bullet in bullets:
                bullet.blit()
                bullet.move()
                if bullet.rect.top <=0:
                    bullet.kill()
            for bullet in bullets_left:
                bullet.blit()
                bullet.move()
                if bullet.rect.top <=0 or bullet.rect.left<=0:
                    bullet.kill()
            for bullet in bullets_right:
                bullet.blit()
                bullet.move()
                if bullet.rect.top <=0 or bullet.rect.right>=width:
                    bullet.kill()
            for monster in monsters:
                monster.blit()
                monster.move()
                if pygame.sprite.spritecollide(monster,bullets,1):
                    monster.hp -= 1
                if pygame.sprite.spritecollide(monster,bullets_left,1):
                    monster.hp -= 1
                if pygame.sprite.spritecollide(monster,bullets_right,1):
                    monster.hp -= 1
                if monster.rect.top >= height:
                    monster.kill()
            f1 = font1.render("score:" + str(score), 1, [0, 255, 0])
            plane.blit()
            plane.move()
        #    monster.blit()
        #    monster.move()
        else:
            f1 = font1.render("GAME OVER", 1, [0, 255, 0])
            screen.blit(eval("start" + str(start_image)), [300, 670])
    else:
        screen.blit(eval("start"+str(start_image)), [300,670])
    screen.blit(f1, f1_location)
    pygame.display.update()
    pygame.time.delay(10)
pygame.quit()