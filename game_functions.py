# encoding: utf-8

import sys

import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # 响应按键和鼠标事件
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

# 响应按键和鼠标事件
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

# 发射子弹            
def fire_bullet(ai_settings, screen, ship, bullets):
    # 如果还没有达到限制，就发射一个新子弹
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

# 在飞船和外星人后面重新绘制所有子弹
def update_screen(ai_settings, screen, ship, bullets):
    # Redraw the screen, each pass through the loop.
    screen.fill(ai_settings.bg_color)
    
    # Redraw all bullets, behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
    
def update_bullets(bullets):
    # 更新子弹位置
    bullets.update()

    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
