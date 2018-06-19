import pygame
from pygame.locals import *
from sys import exit
import random
class Plane:
    def __init__(self):
        self.restart()
        self.image = pygame.image.load('image/plane.png').convert_alpha()

    def move(self):
        x, y = pygame.mouse.get_pos()
        x -= self.image.get_width() / 2
        y -= self.image.get_height() / 2
        self.x = x
        self.y = y
    def restart(self):
        self.x = 200
        self.y = 600

class Bullet:
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load('image/bullet.jpg').convert_alpha()
        self.active = False

    def move(self):
        if self.active:
            self.y -= 1
        if self.y < 0:
            self.active = False

    def restart(self):
        mouseX,mouseY = pygame.mouse.get_pos()
        self.x = mouseX - self.image.get_width() / 2
        self.y = mouseY - self.image.get_height() / 2
        self.active = True

class Enemy:
    def __init__(self):
        self.restart()
        self.image = pygame.image.load('image/enemy.jpg').convert_alpha()

    def move(self):
        if self.y <800:
            self.y += self.speed
        else:
            self.restart()

    def restart(self):
        self.x = random.randint(50,400)
        self.y = random.randint(-200,-50)
        self.speed = 0.2

def CheckHit(enemy, bullet):
    if (bullet.x > enemy.x and bullet.x < enemy.x + enemy.image.get_width()) and (
        bullet.y > enemy.y and bullet.y < enemy.y + enemy.image.get_height()
    ):
        enemy.restart()
        bullet.active = False
        return  True
    return False
def CheckCrash(enemy,plane):
    if (plane.x+0.7*plane.image.get_width()>enemy.x) and (
        plane.x+0.3*plane.image.get_width()<enemy.x+enemy.image.get_width()) and (
        plane.y+0.7*plane.image.get_height()>enemy.y) and (
        plane.y+0.3*plane.image.get_width()<enemy.y+enemy.image.get_height()
    ):
        return True
    return False
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((450, 800), 0, 32)
pygame.display.set_caption("雷电打飞机")
background = pygame.image.load('image/back.jpg').convert()
pygame.mixer.music.load("sound/music.mp3")
pygame.mixer.music.set_volume(0.2)
plane = Plane()
bullets = []
for i in range(3):
    bullets.append(Bullet())
count_b = len(bullets)
index_b = 0
interval_b = 0
enemies = []
for i in range(5):
    enemies.append(Enemy())
gameover = False
score = 0
highest_score = [0]
font = pygame.font.Font(None, 32)
pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
        if gameover and event.type == pygame.MOUSEBUTTONUP:
            plane.restart()
            for e in enemies:
                e.restart()
            for b in bullets:
                b.active = False
            score = 0
            gameover = False
    screen.blit(background, (0, 0))
    if not gameover:
        interval_b -= 1
        if interval_b < 0:
            bullets[index_b].restart()
            interval_b = 200
            index_b = (index_b + 1) % count_b
        for b in bullets:
            if b.active:
                for e in enemies:
                    if CheckHit(e, b):
                        score += 100
                b.move()
                screen.blit(b.image, (b.x, b.y))
        for e in enemies:
            if CheckCrash(e, plane):
                    gameover = True
            e.move()
            screen.blit(e.image, (e.x, e.y))
        plane.move()
        screen.blit(plane.image, (plane.x, plane.y))
        # 在屏幕左上角显示分数
        text = font.render("Socre: %d" % score, 1, (0, 0, 0))
        screen.blit(text, (0, 0))
        highest_score.append(score)
    else:
         # 在屏幕中央显示分数
        if len(highest_score)>10:
             highest_score.remove(min(highest_score))
        text = font.render("Socre: %d" % score, 1, (0, 0, 0))
        screen.blit(text, (100, 280))
        highest = max(highest_score)
        text1 = font.render("highest_score: %d" % highest,1,(0,0,0))
        screen.blit(text1,(100,320))
        pass
    pygame.display.update()



    
