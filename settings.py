#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/04 18:53
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: alien_invasion
# @FileName   : alien_invasion/settings.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

import pygame


class Settings:
    """存储《外星人入侵》中所有设置的类"""

    def __init__(self):
        # 应用设置
        self.caption = '打倒外星人'

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 颜色也可以使用下面的代码来指定
        self.bg_color = pygame.Color("black")

        # 飞船移速
        self.ship_speed = 10.5

        # 帧率设置
        self.frame_rate = 60
