#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
目標：檢查球與擋板是否相碰
核心概念
1. barP.x = max(min(mouseX,width), 0) 
2. hitBar = true if (ballP-ballV).x < ...
3. over = true if y> screenHeight 
'''
import pygame
from pygame.math import Vector2

screen = pygame.display.set_mode((640,480))
done = False
ballP = Vector2(10,10)
ballV = Vector2(5,3)
barW = 60
barH = 30
barP = Vector2(200,440) #3-1
hitBar = False #3-2
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  
    #3-3 檢查球是否跑出下方邊界
    if ballP.y > screen.get_height():
        screen.fill((255,255,255)) 
    else:
        screen.fill((0,255,0))
    ballP += ballV
    #3-2 檢查球是否碰到擋板
    dis = ballP +ballV - barP
    if (abs(dis.x) < barW/2) and (abs(dis.y) < barH/2):
        hitBar = True
    ballV.x *= -1 if ballP.x > screen.get_width() or ballP.x < 0 else 1
    ballV.y *= -1 if hitBar or ballP.y < 0 else 1
    hitBar = False
    pygame.draw.circle(screen, (50,50,250),[int(ballP.x),int(ballP.y)],10)
    mouseX, mouseY = pygame.mouse.get_pos()
    #3-1 更新擋板的位置
    barP.x = max(min(mouseX, screen.get_width()),0)
    pygame.draw.rect(screen,(0,128,128),[barP.x-barW/2,barP.y-barH/2,barW,barH])
    pygame.display.update()