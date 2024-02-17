import pygame,random
import sys
from pygame.locals import *

import pygameGUI as pg

# 颜色常量
WHITE = (255,255,255)
BLACK = (0,0,0)

size = width, height = 800,600

screen = pygame.display.set_mode(size)

pygame.display.set_caption("title")

clock = pygame.time.Clock()

delay = 60 # 延时计时器(1秒)

# 是否全屏
fullscreen = False
screen_change = False

# 背景颜色设定
bg_color = (80,80,80)

running = True

# ui=====

guis = pg.Group()

l1 = pg.Label(text="默认文本...")
e1 = pg.Entry(group=guis,text = l1,size=[200,l1.rect[3]],pos=[10,10])
# =================

while running:
    # 设定帧数
    clock.tick(60)

    # 获取鼠标位置
    pos = pygame.mouse.get_pos()

    # 延时计时器刷新
    if delay == 0:
        delay = 60

    delay -= 1

    # 检测是否全屏
    if fullscreen and screen_change:
        screen = pygame.display.set_mode(size,FULLSCREEN,HWSURFACE)
        screen_change = False
    elif screen_change:
        screen = pygame.display.set_mode(size)
        screen_change = False

    # 事件检测
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # 鼠标
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1: # 左键按下，获取鼠标位置
                pass

        # 按键按下事件
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
            #F11切换全屏
            if event.key == K_F11:
                fullscreen = not fullscreen
                screen_change = True

        # 按键抬起事件
        if event.type == KEYUP:
            pass

        elif event.type == 1024:
            pass

    #画背景
    screen.fill(bg_color)
    for i in range(int(800/50)):
        pygame.draw.line(screen,(0,0,0),[i*800/16,0],[i*800/16,600])
    for i in range(int(600/50)):
        pygame.draw.line(screen,(0,0,0),[0,i*600/12],[800,i*600/12])
    
    # 刷新xxx
    guis.update(pos=pos,events = events)

    #画 xxxx
    guis.draw(screen)
    

    # 刷新界面
    pygame.display.update()

    

