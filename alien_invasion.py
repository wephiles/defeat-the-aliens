#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/04 18:18
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: alien_invasion
# @FileName   : alien_invasion/alien_invasion.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

"""
外星人入侵项目入口模块。
"""

import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        # 赋值后 self.screen 是一个 Surface 对象
        # set_mode 返回的 surface 表示整个游戏窗口
        # 激活游戏的动画循环后，每经过一次循环都将自动重绘这个 surface，
        # 将用户输入触发的所有变化都反映出来。
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # print(type(self.screen))  # <class 'pygame.surface.Surface'>

        pygame.display.set_caption(self.settings.caption)
        self.bg_color = self.settings.bg_color
        # self.bg_color = pygame.Color("white")

        self.ship = Ship(self)

    def _check_events_key_down(self, event):
        # 按下按键
        if event.key == pygame.K_RIGHT:
            # 如果是按下的是键盘右键
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_events_key_up(self, event):
        if event.key == pygame.K_RIGHT:
            # 如果松开的是键盘右键
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            # 如果松开的是键盘右键
            self.ship.moving_left = False

    def _check_events(self):
        # 监听键盘和鼠标事件
        # event 是用户玩游戏时执行的操作，如按键或移动鼠标。
        # 我们使用 pygame.event.get() 函数来访问 pygame 检测到的事件。
        # 这个函数返回一个列表，其中包含它在上一次调用后发生的所有事件。
        # 所有键盘和鼠标事件都将导致这个 for 循环运行。在这个循环中，
        # 我们将编写一系列 if 语句来检测并响应特定的事件。
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 按下按键
                self._check_events_key_down(event)
            elif event.type == pygame.KEYUP:
                # 松开按键
                self._check_events_key_up(event)

    def _update_screen(self):
        # 每次循环时都重绘屏幕

        # 1. 填充背景色
        self.screen.fill(self.bg_color)

        # 2. 绘制飞船
        self.ship.blit_me()

        # 3. 让最近绘制的屏幕可见
        # pygame.display.flip()，命令 pygame 让最近绘制的屏幕可见。
        # 这里，它在每次执行 while 循环时都绘制一个空屏幕，
        # 并擦去旧屏幕，使得只有新的空屏幕可见。我们在移动游戏元素时，
        # pygame.display.flip() 将不断更新屏幕，以显示新位置上的元素并隐藏原来位置上的元素，
        # 从而营造平滑移动的效果。
        pygame.display.flip()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 每次循环检查事件 检查时间完毕后根据事件类型更新屏幕展示内容并刷新
            self._check_events()
            self.ship.update()
            self._update_screen()

            # tick() 方法接受一个参数：游戏的帧率。这里使用的值为 60，
            # pygame 将尽可能确保这个循环每秒恰好运行 60 次。
            self.clock.tick(self.settings.frame_rate)


if __name__ == "__main__":
    alien = AlienInvasion()
    alien.run_game()
