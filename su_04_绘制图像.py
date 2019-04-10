import pygame

pygame.init()

# 创建游戏窗口480 * 700
screen = pygame.display.set_mode((300, 530))

# 绘制背景图
# 1>加载图像
bg = pygame.image.load("./images/background.png")
# 2>blit绘制图像
screen.blit(bg, (0, 0))
# 3>update更新屏幕显示
# 可以在绘制完所有图像后,统一调用一次update()方法
# pygame.display.update()

# 绘制英雄飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (110, 300))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
i = 1
# 游戏循环,意味着游戏的正式开始
while True:
    # 可以指定游戏循环内部代码执行的频率
    clock.tick(1)
    print(i)
    i += 1
pygame.quit()