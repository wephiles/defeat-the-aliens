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
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet
from button import Button
from game_status import GameStatus
from settings import Settings
from ship import Ship
from score_board import ScoreBoard


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
                pygame.FULLSCREEN,
            )
            # 更新配置文件中的宽和高
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height)
            )

        pygame.display.set_caption(self.settings.caption)
        self.bg_color = self.settings.bg_color
        # self.bg_color = pygame.Color("white")

        # 用于存储统计信息的实例对象
        self.status = GameStatus(self)

        # 记分牌
        self.score_board = ScoreBoard(self)

        # 我们的飞船
        self.ship = Ship(self)
        # 注册子弹的编组
        self.bullets = pygame.sprite.Group()
        # 注册外星人的编组
        self.aliens = pygame.sprite.Group()

        # 外星人舰队
        self._create_fleet()

        # 让游戏在一开始处于非活动状态
        self.game_active = False

        self.play_button = Button(self, "Play")

    def _create_alien(self, x_position, y_position):
        """创建一个外星人并将其放在当前行中"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _create_fleet(self):
        """创建外星人舰队"""
        # 创建一个外星人，再不断添加，直到没有空间放外星人为止
        # 外星人的间距是外星人的宽度
        alien_ = Alien(self)
        alien_width, alien_height = alien_.rect.width, alien_.rect.height

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 5 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            # 添加一个一行外星人后, 重置 x 并增大 y
            current_x, current_y = alien_width, current_y + 2 * alien_height

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """单机 Play 按钮就开始游戏"""
        # 使用 rect 的 collidepoint() 方法检查鼠标的单击位置是否在 Play 按钮的 rect 内
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # not self.game_active 是为了解决当点击 Play 按钮后这个按钮消失但是如果点击按钮的位置还是会重启游戏
        if button_clicked and not self.game_active:
            # 重置游戏的统计信息
            self.status.reset_status()
            self.score_board.prep_score()
            self.score_board.prep_ships()
            # 重置游戏速度
            self.settings.initialize_dynamic_settings()

            self.game_active = True

            # 清空外星人列表和子弹列表
            self.bullets.empty()
            self.aliens.empty()

            # 创建一个新的外星舰队，并将飞船放在屏幕底部中央
            self._create_fleet()
            self.ship.center_ship()

            # 隐藏鼠标
            pygame.mouse.set_visible(False)

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

        # 绘制外星人
        self.aliens.draw(self.screen)

        # 显示记分牌
        self.score_board.show_score()

        # 如果游戏没有开始, 绘制按钮
        if not self.game_active:
            self.play_button.draw_button()

        # 3. 让最近绘制的屏幕可见
        # pygame.display.flip()，命令 pygame 让最近绘制的屏幕可见。
        # 这里，它在每次执行 while 循环时都绘制一个空屏幕，
        # 并擦去旧屏幕，使得只有新的空屏幕可见。我们在移动游戏元素时，
        # pygame.display.flip() 将不断更新屏幕，以显示新位置上的元素并隐藏原来位置上的元素，
        # 从而营造平滑移动的效果。
        pygame.display.flip()

    def _check_collisions_bullet_alien(self):
        """响应子弹和外星人的碰撞"""
        # 检查是否有子弹击中了外星人
        # 如果是就删除子弹和外星人
        # ===========================================================================================
        # 这些新增的代码将 self.bullets 中的所有子弹与 self.aliens 中的所有外星人进行比较，看它们是否重叠了在一起。
        # 每当有子弹和外星人的 rect 重叠时，groupcollide() 就在返回的字典中添加一个键值对。
        # 两个值为 True 的实参告诉 Pygame 在发生碰撞时删除对应的子弹和外星人。
        # 注意: 要模拟能够飞到屏幕上边缘的高能子弹（它会消灭击中的每个外星人，但自己不受影响），
        #   可将第一个布尔实参设置为 False，并保留第二个布尔实参为 True。
        #   这样被击中的外星人将消失，但所有的子弹始终有效，直到抵达屏幕的上边缘后消失。
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                # 如果在一次循环中有两颗子弹分别击中了两个外星人，或者因一颗子弹太宽而同时击中了多个外星人，
                # 玩家将只能得到一个外星人的分数。为了修复这个问题，我们需要调整检测子弹和外星人碰撞的方式。
                self.status.score += self.settings.alien_scores * len(aliens)

            self.score_board.prep_score()
            self.score_board.check_high_score()

        # 如果没有舰队了 生成新的舰队
        if not self.aliens:
            # 删除现有的子弹并创建一个新的外星舰队
            self.bullets.empty()
            self._create_fleet()

            # 将所有外星人都消灭后, 加快速度
            self.settings.increase_speed()

            # 提高等级
            self.status.level += 1
            self.score_board.prep_level()

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
        self._check_collisions_bullet_alien()

    def _ship_hit(self):
        """响应飞船和外星人的碰撞"""
        if self.status.ships_left > 0:
            # 将 ship_lefts - 1
            self.status.ships_left -= 1
            self.score_board.prep_ships()
        else:
            self.game_active = False
            # 游戏结束后显示鼠标
            pygame.mouse.set_visible(True)

        # 清空外星人列表和子弹列表
        self.bullets.empty()
        self.aliens.empty()

        # 创建一个新的外星舰队，并将飞船放在屏幕底部的中央
        self._create_fleet()
        self.ship.center_ship()

        # 暂停 0.5 s
        sleep(0.5)

    def _update_aliens(self):
        """检查是否有外星人处于屏幕边缘, 更新外星舰队所有外星人的位置"""
        self._check_fleets_edge()
        # 对 aliens 编组调用 update() 方法，将自动对每个外星人调用 update() 方法。
        self.aliens.update()

        # 检测外星人和飞船的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 检查是否有外星飞船到达屏幕底部
        self._check_alien_fleet_bottom()

    def _check_fleets_edge(self):
        """在有外星人到达屏幕边缘时采取相应的措施"""
        for one_alien in self.aliens.sprites():
            if one_alien.check_edges():
                # 到达边缘
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整个舰队向下移动并改变他们的位置"""
        for one_alien in self.aliens.sprites():
            one_alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_alien_fleet_bottom(self):
        """外星人舰队有到达底部"""
        for alien_ in self.aliens.sprites():
            if alien_.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 每次循环检查事件 检查时间完毕后根据事件类型更新屏幕展示内容并刷新
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()

            self._update_screen()
            # tick() 方法接受一个参数：游戏的帧率。这里使用的值为 60，
            # pygame 将尽可能确保这个循环每秒恰好运行 60 次。
            self.clock.tick(self.settings.frame_rate)


if __name__ == "__main__":
    alien = AlienInvasion()
    alien.run_game()
