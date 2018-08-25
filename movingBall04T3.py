#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
目標：檢查球與擋板是否相碰
核心概念
1. 以 GameState 切換場景
2. 插入圖片 pygame.image.load
3. 偵測鍵盤 event.key == pygame.K_SPACE:
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
gameState = True #4-1
failImage = pygame.image.load('fail.png') #4-2
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: #4-3
            if event.key == pygame.K_SPACE:
                ballP = Vector2(10,10)
                ballV = Vector2(5,3) 
                gameState = True
    #3-3 檢查球是否跑出下方邊界
    if gameState == True: #4-1
        if ballP.y > screen.get_height():
            gameState = False  
        else:
            screen.fill((0,255,0))
        ballP += ballV 
        #3-2 檢查球是否碰到擋板
        dis = ballP + ballV - barP
        if (abs(dis.x)<(barW)/2) and (abs(dis.y)<barH/2):
            hitBar = True
        ballV.x *= -1 if ballP.x > screen.get_width() or ballP.x < 0 else 1
        ballV.y *= -1 if hitBar or ballP.y < 0 else 1
        hitBar = False
        pygame.draw.circle(screen, (50,50,250),[int(ballP.x),int(ballP.y)],10)
        mouseX, mouseY = pygame.mouse.get_pos()
        #3-1 更新擋板的位置
        barP.x = max(min(mouseX, screen.get_width()),0)
        pygame.draw.rect(screen,(0,128,128),[barP.x-barW/2,barP.y-barH/2,barW,barH])
    if gameState == False: #4-1
        screen.fill((255,255,255)) #4-1
        screen.blit(failImage, (screen.get_width()/2-failImage.get_width()/2, screen.get_height()/2-failImage.get_height()/2))
    pygame.display.update() 