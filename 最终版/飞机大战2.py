import pygame as p
import random as r
#from os import
p.init()
class Plane(p.sprite.Sprite):
    def __init__(self,screen,image_fill,location,speed):
        p.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = p.image.load(image_fill)
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
class Monster(p.sprite.Sprite):
    def __init__(self,screen,image_fill,locstion,speed,hp):
        p.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = p.image.load(image_fill)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = locstion
        self.speed = speed
        self.hp = hp
    def move(self):
        global score
        global boss_time
        self.rect = self.rect.move(self.speed)
        if self.rect.top >= height:
            self.kill()
        if self.hp <= 0:
            self.kill()
            score = score + 1
            boss_time+=1
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > width:
            self.rect.right = width
    def blit(self):
        self.screen.blit(self.image,self.rect)
class Supply(p.sprite.Sprite):
    def __init__(self,screen,image_fill,locstion,speed):
        p.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = p.image.load(image_fill)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = locstion
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.top >= height:
            self.kill()
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > width:
            self.rect.right = width
    def blit(self):
        self.screen.blit(self.image,self.rect)




width = 400
height = 600
screen = 0
boss_bullet_time = 0
key_list = []
run_flag = True
start_flag = False
boss_bullet_flag = False
start_image = 1
monster_time = 0
bullet_time = 24
boss_time = 0
score = 0

s_boss = p.mixer.Sound("sounds/s_boss.wav")
s_boss.set_volume(0.40)
s_boss_bullet = p.mixer.Sound("sounds/s_boss_bullet.wav")
s_boss_bullet.set_volume(0.03)
s_allied = p.mixer.Sound("sounds/s_allied.wav")
s_allied.set_volume(0.10)
s_live = p.mixer.Sound("sounds/s_live.wav")
s_live.set_volume(0.10)
s1 = p.mixer.Sound("sounds/s_bullet.wav")
s1.set_volume(0.10)
p.mixer.music.load("sounds/s_bg.mp3")
p.mixer.music.set_volume(0.05)
p.mixer.music.play(-1)

font1 = p.font.Font(None,50)
f1 = font1.render("score:"+str(screen),1,[0,255,0])
life = 1
life_image = p.image.load("img/life.png")
screen = p.display.set_mode([width,height])
'''plane = Plane(screen,"plane.png",[175,750],[0,0])
monster = Monster(screen,"monster.png",[0,0],[0,3])'''
plane = Plane(screen,"plane.png",[175,751],[0,0])
#monster = Monster(screen,"img/monsters.png",[0,0],[0,0])
start1 = p.image.load("img/start1.png")
start2 = p.image.load("img/start2.png")
start3 = p.image.load("img/start3.png")
monsters = p.sprite.Group()
bullets = p.sprite.Group()
supplys = p.sprite.Group()
bosss = p.sprite.Group()
boss_bullets = p.sprite.Group()
p.time.set_timer(p.USEREVENT,1000)
running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
        if event.type == p.USEREVENT:
            supply = Supply(screen,"img/supply.png",[r.randint(0,width-75),-75],[0,4])
            supplys.add(supply)
        if event.type == p.MOUSEMOTION:
            x, y = p.mouse.get_pos()
            if x >= 300 and x <= 350:
                if y>=500 and y<=530:
                    start_image = 3
                else:
                    start_image = 1
            else:
                start_image = 1
        if event.type == p.MOUSEBUTTONDOWN:
            if x >= 300 and x <= 350:
                if y>=500 and y<=530:
                    start_flag = True
                    run_flag = True
                    f1_location = [25,25]
                    score = 0
                    life = 1
        if event.type == p.QUIT:
            running = False
        if event.type == p.KEYDOWN:
            if event.key == p.K_UP:
                key_list.append("K_UP")
            elif event.key == p.K_DOWN:
                key_list.append("K_DOWN")
            elif event.key == p.K_LEFT:
                key_list.append("K_LEFT")
            elif event.key == p.K_RIGHT:
                key_list.append("K_RIGHT")
            elif event.key == p.K_x:
                key_list.append("K_x")
        elif event.type == p.KEYUP:
            if event.key == p.K_UP:
                key_list.remove("K_UP")
            elif event.key == p.K_DOWN:
                key_list.remove("K_DOWN")
            elif event.key == p.K_LEFT:
                key_list.remove("K_LEFT")
            elif event.key == p.K_RIGHT:
                key_list.remove("K_RIGHT")
            elif event.key == p.K_x:
                key_list.remove("K_x")
                bullet_time = 24
    if start_flag:
        if run_flag:
            if boss_bullet_flag:
                boss_bullet_time+=1
                if boss_bullet_time>=40:
                    boss_bullet_time = 0
                    boss_bullet = Plane(screen,"img/boss_bullet.png",[boss.rect.centerx-10,boss.rect.bottom],[0,4])
                    boss_bullets.add(boss_bullet)
            if boss_time>=15:
                boss = Monster(screen,"img/i_boss.png",[r.randint(0,width-120),-91],[0,2],20)
                bosss.add(boss)
                boss_time = 0
                boss_bullet_flag = True
                s_boss_bullet.play()
            if "K_UP" in key_list:
                plane.rect.top-=3
            if "K_DOWN" in key_list:
                plane.rect.top+=3
            if "K_LEFT" in key_list:
                plane.rect.left-=3
            if "K_RIGHT" in key_list:
                plane.rect.left+=3
            if "K_x" in key_list:
                bullet_time +=1
                print(1)
                if bullet_time >=25:
                    s1.play()
                    bullet = Plane(screen,"bullet2.png",[plane.rect.centerx-5,plane.rect.top],[0,-5])
                    bullets.add(bullet)
                    bullet_time = 0
            if monster_time>=25:
                monster = Monster(screen,"monster.png",[r.randint(0,width-75),-75],[0,2],3)
                monsters.add(monster)
                monster_time = 0
            for i in range(1,life+1):
                screen.blit(life_image,[width-i*50,30])
            for supply in supplys:
                supply.blit()
                supply.move()
                if p.sprite.collide_rect(plane,supply):
                    supply.kill()
                    life+=1

            for bullet in bullets:
                bullet.blit()
                bullet.move()
                if bullet.rect.top <= 0:
                    bullet.kill()
            for monster in monsters:
                monster.blit()
                monster.move()
                if p.sprite.spritecollide(monster,bullets,1):
                    monster.hp-=1
                    #monster.hp = 1
            if p.sprite.spritecollide(plane,monsters,1):
                life-=1
            if life <= 0:
                monsters.empty()
                bullets.empty()
                supplys.empty()
                run_flag = False
            #print(monsters)-=
            monster_time += 1
            f1 = font1.render("score:" + str(score),1,[0,255,0])
            plane.blit()
            plane.move()
            screen.blit(f1,[30,30])
            for bullet in boss_bullets:
                bullet.blit()
                bullet.move()
                if p.sprite.collide_rect(bullet, plane):
                    bullet.kill()
                    life -= 1
                #                    s_live.play()
                elif bullet.rect.bottom >= height:
                    bullet.kill()
            for boss in bosss:
                boss.blit()
                boss.move()
                if p.sprite.spritecollide(boss,bullets,1):
                    boss.hp -= 1
                if boss.hp<=0:
                    score+=5
                    boss_time+=5
                    boss_bullet__flag = False
                elif p.sprite.collide_rect(plane,boss):
                    boss.kill()
                    life-=2
                    boss_bullet_flag = False
                elif boss.rect.top>=height:
                    boss_bullet_flag = False
        else:
            f2 = font1.render("GAME OVER", 1, [255, 0, 0])
            screen.blit(eval("start"+str(start_image)),[300,500])
            screen.blit(f2,[10,40])
    else:
        screen.blit(eval("start"+str(start_image)),[300,500])
    p.display.update()
    p.time.delay(10)
    screen.fill([78, 78, 78])
#screen.distop.leet(10,10)
p.quit()




