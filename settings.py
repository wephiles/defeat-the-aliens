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
        # 飞船设置
        self.ship_speed = 10.5
        self.ship_limit = 3
        # # 程序运行之后会设置此属性
        # self.ship_width = 200
        # self.ship_height = 100

        # 子弹设置
        self.bullet_speed = 12.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_max_nums = 5

        # 外星人设置
        self.alien_speed = 1.0
        # fleet_drop_speed 表示外星人舰队在碰到边缘的时候向下移动的速度
        self.fleet_drop_speed = 10
        # fleet_direction 为 1 表示向右移动, 为 -1 表示向左移动
        self.fleet_direction = 1
        # # 程序运行之后会设置此属性
        # self.alien_width = 200
        # self.alien_height = 100
