#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/04 19:15
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: alien_invasion
# @FileName   : alien_invasion/ship.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

"""
飞船。
"""

import pygame

from settings import Settings


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置

        pygame 之所以高效，是因为它让你能够把所有的游戏元素当作矩形（rect 对象）来处理，
        即便它们的形状并非矩形也一样。而把游戏元素当作矩形来处理之所以高效，
        是因为矩形是简单的几何形状。例如，通过将游戏元素视为矩形，
        Pygame 能够更快地判断出它们是否发生了碰撞。这种做法的效果通常很好，
        游戏玩家几乎注意不到我们处理的不是游戏元素的实际形状。
        在这个类中，我们将把飞船和屏幕作为矩形进行处理。

        在处理 rect 对象时，可使用矩形的四个角及中心的 x 坐标和 y 坐标，通过设置这些值来指定矩形的位置。
        如果要将游戏元素居中，可设置相应 rect 对象的属性 center、centerx 或 centery；
        要让游戏元素与屏幕边缘对齐，可设置属性 top、bottom、left 或right。
        除此之外，还有一些组合属性，如 midbottom、midtop、midleft 和 midright。
        要调整游戏元素的水平或垂直位置，可使用属性 x 和 y，它们分别是相应矩形左上角的 x 坐标和 y 坐标。
        这些属性让你无须去做游戏开发人员原本需要手动完成的计算，因此很常用。
        注意：在 Pygame 中，原点(0, 0)位于屏幕的左上角，当一个点向右下方移动时，它的坐标值将增大。
            在 1200×800 的屏幕上，原点位于左上角，右下角的坐标为(1200, 800)。
            这些坐标对应的是游戏窗口，而不是物理屏幕。因为我们要将飞船放在屏幕底部的中央，
            所以将self.rect.midbottom 设置为表示屏幕的矩形的属性 midbottom。
            Pygame 将使用这些 rect 属性来放置飞船图像，使其与屏幕下边缘对齐并水平居中。
        """
        # 配置
        self.settings = ai_game.settings

        self.screen = ai_game.screen

        # 使用 get_rect 访问屏幕的 rect 属性
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        # pygame.image.load() 返回一个 surface
        self.image = pygame.image.load('images/ship_2.bmp')
        # 飞船设置
        self.settings.ship_width = self.settings.screen_width // 20
        self.settings.ship_height = self.settings.screen_height // 20
        self.image = pygame.transform.scale(self.image, (self.settings.ship_width, self.settings.ship_height))
        self.rect = self.image.get_rect()

        # 每一艘新飞船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 飞船移动标志 -- 新创建飞船后飞船是不移动的 只有持续按住某一个键的时候才需要持续移动
        self.moving_right = False
        self.moving_left = False
        # self.moving_up = False
        # self.moving_down = False

    def update(self):
        """根据移动标志调整飞船位置"""
        speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= speed
        # if self.moving_up:
        #     self.y -= speed
        # if self.moving_down:
        #     self.y += speed

        # rect 只保留整数部分, 所以需要另设一个浮点数来让其能够表示小数
        self.rect.x = self.x

    def blit_me(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """在屏幕底部中央创建飞船"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
