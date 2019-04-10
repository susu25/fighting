import pygame

pygame.init()

# 创建游戏窗口480 * 700
screen = pygame.display.set_mode((300, 530))

# 绘制背景图
# 1>加载图像
bg = pygame.image.load("./images/background.png")
# 可以使用transfrom.soomthscale()方法修改图片大小
bg = pygame.transform.smoothscale(bg, (300, 530))
# 2>blit绘制图像
screen.blit(bg, (0,0))
# 3>update更新屏幕显示
# 可以在绘制完所有图像后,统一调用一次update()方法
# pygame.display.update()

# 绘制英雄飞机
hero = pygame.image.load("./images/me1.png")
hero = pygame.transform.smoothscale(hero, (50, 70))
screen.blit(hero, (110, 380))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(110, 380, 50, 70)

# 游戏循环,意味着游戏的正式开始
while True:
    # 可以指定游戏循环内部代码执行的频率
    clock.tick(60)

    # 使用event()事件监听,捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)

    # 2.修改飞机位置
    hero_rect.y -= 1

    # 判断飞机位置
    if hero_rect.y <= 0:
        # 飞机飞出屏幕后,把飞机移动到屏幕底部
        hero_rect.y = 530
    # 3.调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    # 4.update更新显示
    pygame.display.update()

pygame.quit()