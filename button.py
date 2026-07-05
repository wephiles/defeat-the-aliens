#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/05 13:43
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: alien_invasion
# @FileName   : alien_invasion/button.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.


"""
创建按钮
"""

import pygame


class Button:
    """由于 Pygame 没有内置创建按钮的方法，我们需要自己创建button类"""

    def __init__(self, ai_game, msg):
        """初始化按钮的属性"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)

        # 新版 pygame 在Windows中不兼容整个写法
        # self.font = pygame.font.SysFont(None, 48)

        try:
            self.font = pygame.font.Font(None, 48)  # 使用 Pygame 默认字体
        except TypeError:
            # 如果默认字体也有问题，可以加载系统字体文件
            import os
            font_path = os.path.join(os.environ.get('WINDIR', ''), 'Fonts', 'simsun.ttc')
            if os.path.exists(font_path):
                self.font = pygame.font.Font(font_path, 48)
            else:
                self.font = pygame.font.Font(None, 48)
        # 创建按钮的 rect 对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需创建一次
        self._prep_msg(msg)

    def _prep_msg(self, text):
        """将 text 渲染为图像，并将其在按钮上居中"""
        # render
        #   antialias 参数: 如果为 True, 则开启反锯齿功能
        #   color 参数: 文本颜色
        #   background 参数: 背景色
        self.msg_image = self.font.render(text, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制一个用颜色填充的按钮，再绘制文本"""

        # screen.fill() 来绘制表示按钮的矩形
        self.screen.fill(self.button_color, self.rect)
        # screen.blit() 来向它传递一幅图像以及与该图像相关联的 rect
        self.screen.blit(self.msg_image, self.msg_image_rect)

# END
