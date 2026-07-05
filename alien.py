#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/05 9:28
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: alien_invasion
# @FileName   : alien_invasion/alien.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

"""
外星人类
"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人"""

    def __init__(self, ai_game):
        """Alien 类不需要在屏幕上绘制外星人的方法，

        因为我们将使用一个 Pygame 编组方法，自动地在屏幕上绘制编组中的所有元素。
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外星人图片 设置其 rect 属性
        self.image = pygame.image.load("images/alien.bmp")
        self.settings.alien_width = self.settings.screen_width // 18
        self.settings.alien_height = self.settings.screen_height // 18
        self.image = pygame.transform.scale(self.image, (self.settings.alien_width, self.settings.alien_height))
        self.rect = self.image.get_rect()

        # 每个外星人都在屏幕左上角出现
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的真实位置
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人处于屏幕边缘, 返回 True, 否则返回False"""
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

# END
