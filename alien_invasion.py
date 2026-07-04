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
from bullet import Bullet


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
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # # print(type(self.screen))  # <class 'pygame.surface.Surface'>
        if self.settings.full_screen:
            # 全屏
            # 因为不知道用户的屏幕尺寸，如果设置全屏的话要在设置全屏之后再获取宽和高
            # 注意: 在全屏模式下运行这款游戏前，请确认能够按 Q 键退出，
            #   因为 Pygame 不提供在全屏模式下退出游戏的默认方式。
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height),
                pygame.FULLSCREEN
            )
            # 更新配置文件中的宽和高
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption(self.settings.caption)
        self.bg_color = self.settings.bg_color
        # self.bg_color = pygame.Color("white")

        self.ship = Ship(self)

        # 注册子弹的编组
        self.bullets = pygame.sprite.Group()

    def _fire(self):
        """创建一个子弹，并将子弹加入编组中。"""

        # 限制子弹最多多少颗
        if len(self.bullets) < self.settings.bullets_max_nums:
            self.bullets.add(Bullet(self))

    def _check_events_key_down(self, event):
        # 按下按键
        # 如果按下的是英文状态下的 q, 直接退出.
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_ESCAPE:
            # TODO: 增加连续按两次 ESC 才退出 现在是只按下ESC就退出
            sys.exit()

        # 开火！
        if event.key == pygame.K_SPACE:
            self._fire()
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

        # 2. 绘制屏幕中的元素
        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 绘制飞船
        self.ship.blit_me()

        # 3. 让最近绘制的屏幕可见
        # pygame.display.flip()，命令 pygame 让最近绘制的屏幕可见。
        # 这里，它在每次执行 while 循环时都绘制一个空屏幕，
        # 并擦去旧屏幕，使得只有新的空屏幕可见。我们在移动游戏元素时，
        # pygame.display.flip() 将不断更新屏幕，以显示新位置上的元素并隐藏原来位置上的元素，
        # 从而营造平滑移动的效果。
        pygame.display.flip()

    def _update_bullet(self):
        """更新子弹的位置并删除已经消失的子弹"""
        # 在对编组调用 update() 时，编组会自动对其中的每个精灵调用 update()，
        # 因此 self.bullets.update() 将为 bullets 编组中的每颗子弹调用 bullet.update()。
        self.bullets.update()

        # 删除跑出屏幕外面的子弹
        # 注意:
        #  在使用 for 循环遍历列表（或 Pygame 编组）时，Python 要求该列表的长度在整个循环中保持不变。
        #  这意味着不能从 for 循环遍历的列表或编组中删除元素，因此必须遍历编组的副本。
        self._update_screen()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 每次循环检查事件 检查时间完毕后根据事件类型更新屏幕展示内容并刷新
            self._check_events()
            self.ship.update()

            self._update_bullet()

            # tick() 方法接受一个参数：游戏的帧率。这里使用的值为 60，
            # pygame 将尽可能确保这个循环每秒恰好运行 60 次。
            self.clock.tick(self.settings.frame_rate)


if __name__ == "__main__":
    alien = AlienInvasion()
    alien.run_game()
