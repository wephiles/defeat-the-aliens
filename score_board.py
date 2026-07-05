#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/05 17:24
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: alien_invasion
# @FileName   : alien_invasion/score_board.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

"""
记分
"""

import pygame
from pygame.sprite import Group

from ship import Ship


class ScoreBoard:
    """显示得分信息的类"""

    def __init__(self, ai_game):
        """初始化显示得分涉及的属性"""
        self.ships = None
        self.level_rect = None
        self.level_image = None
        self.high_score_rect = None
        self.high_score_image = None
        self.score_rect = None
        self.score_image = None

        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.status = ai_game.status

        # 显示得分信息时使用的字体设置
        self.text_color = (0, 255, 255)
        self.font = pygame.font.Font(None, 48)

        # 准备初始得分图像
        self.prep_score()
        self.prep_highest_score()
        self.prep_level()
        self.prep_ships()

    def prep_highest_score(self):
        """将最高分渲染为图像"""
        high_score = round(self.status.high_score, -1)
        high_score_str = f"Highest: {high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.settings.bg_color)
        # 将最高分放在屏幕顶部的中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_score(self):
        """将得分渲染为图像"""
        # round() 函数通常让浮点数（第一个实参）精确到小数点后某一位，
        # 其中的小数位数由第二个实参指定。如果将第二个实参指定为负数，
        # round() 会将第一个实参舍入到最近的 10 的整数倍，如 10、100、1000 等。

        rounded_score = round(self.status.score, -1)
        score_str = f'Current: {rounded_score:,}'
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # 在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 30
        self.score_rect.top = 30

    def show_score(self):
        """在屏幕上显示得分

        在屏幕上显示得分图像，并将其放在 score_rect 指定的位置上。
        """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """检查是否诞生了新的最高分"""
        if self.status.score > self.status.high_score:
            self.status.high_score = self.status.score
            self.prep_highest_score()

    def prep_level(self):
        """将等级渲染为图像"""
        level_str = 'Level: ' + str(self.status.level)
        self.level_image = self.font.render(level_str, True,
                                            self.text_color, self.settings.bg_color)
        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示还余下多少艘飞船"""
        self.ships = Group()
        for ship_number in range(self.status.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
