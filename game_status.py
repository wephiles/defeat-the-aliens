#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/05 11:08
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: alien_invasion
# @FileName   : alien_invasion/game_status.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

"""
跟踪游戏状态
"""
from ship import Ship


class GameStatus:
    """跟踪游戏的统计信息"""
    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_status()

    def reset_status(self):
        """初始化可能在游戏运行期间变化的统计信息"""
        self.ships_left = self.settings.ship_limit
