#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
目標：產生畫布，並再畫布上繪製一個可以隨鼠標來移動長方形。
核心概念：
1. 用 pygame 來產生畫布
2. 用 pygame.draw.rect() 來繪製長方形
3. 用 pygame.mouse.get_pos() 取得滑鼠位置
'''
import pygame

screen = pygame.display.set_mode((640,480))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0,255,0))
    pygame.display.update()