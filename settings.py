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

"""
全局配置文件。
"""


import pygame


class Settings:
    """存储《外星人入侵》中所有设置的类"""

    def __init__(self):
        # ================== 应用设置 ==================
        # 标题
        self.caption = '打倒外星人'
        # 帧率设置
        self.frame_rate = 60
        # 屏幕设置
        # 注意: 在全屏模式下运行这款游戏前，请确认能够按 Q 键退出，
        #   因为 Pygame 不提供在全屏模式下退出游戏的默认方式。
        self.full_screen = True
        if self.full_screen:
            self.screen_width = 0
            self.screen_height = 0
        else:
            self.screen_width = 1200
            self.screen_height = 800
        # self.bg_color = (230, 230, 230)
        # 颜色也可以使用下面的代码来指定
        self.bg_color = pygame.Color("black")

        # ================== 游戏设置 ==================
        self.ship_speed = 10.5
        # 子弹设置
        self.bullet_speed = 12.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_max_nums = 5

