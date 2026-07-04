#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/04 21:21
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: alien_invasion
# @FileName   : alien_invasion/bullet.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.


"""
子弹。
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理飞船所发射的子弹"""

    def __init__(self, ai_game):
        """在飞船的当前位置创建一个子弹

        继承了从模块 pygame.sprite 导入的 Sprite 类。
        通过使用精灵（sprite），可将游戏中相关的元素编组，进而同时操作编组中的所有元素。
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在 (0, 0) 处创建一个子弹, 再放到正确的位置上
        # 因为子弹我们在这里不用图片, 所以从头创建子弹
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midbottom = ai_game.ship.rect.midtop

        # 存储用浮点数表示的子弹位置
        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        # 更新子弹的准确位置
        self.y -= self.settings.bullet_speed

        # 更新表示子弹的 rect 的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

# END
