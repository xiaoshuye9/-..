from tkinter import messagebox
import datetime
import tkinter as tk
from tkinter import *
import cmd
#
# while True:
#     print('请输入测试版密钥!!!')
#     print('密钥格式为:XXXXX-XXXXX-XXXXX-XXXXX-XXXXX')
#     print('教师密钥是:zswdmy,wsjs,pzh=xxxxxx')
#     print('(pzh=xxxxxx的解释:pzh是批准号  xxxxxx是批准号)')
#     a=input()
#     if a=='zswdmy,wsjs,pzh=0x12jsgxbn' or a=='zswdmy,wsjs,pzh=nXs小':
#         messagebox.showinfo('感谢!', '真诚的感谢您(教师)免费试用我们的产品!!!致谢🙇🙇🙇')
#         print('                                 ')
#         break
#
#     ab=len(a)
#     if ab!=29:
#         messagebox.showinfo('你SB™的真SB', '密钥格式有误(你是SB,不买密钥!!!)')
#         print('                                 ')
#         continue
#     else:
#         if a=='gxnmy-fe223-66ooo-nihao-xxxxx':
#             messagebox.showinfo('感谢!', '真诚的感谢你(您)购买我们的产品!!!致谢🙇🙇🙇')
#             print('                                 ')
#             break
#         else:
#             messagebox.showinfo('你SB™的真SB', '你这密钥也错!!!老实输入密钥')
#             print('                                 ')
#             continue

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-




# -*- coding: utf-8 -*-


# 获取当前时间, 其中中包含了year, month, hour, 需要import datetime
today = datetime.date.today()
today = str(today)
if today == '2024-05-31' or today > '2024-05-31':
    while True:
        messagebox.showinfo('提示', '你无法使用了,该版本已过期（时间炸弹爆炸）')

def clear():
    os.system('cls')


import re


#判断是否有英文↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
def is_contains_english(str):
    my_re = re.compile(r'[A-Za-z]', re.S)
    res = re.findall(my_re, str)
    if len(res):
        return True
    else:
        return False


#判断是否有中文↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


#判断是否有符号↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
def ppppppppp(pppppp):
    input_psd = pppppp
    test_str = re.search(r"\W", input_psd)
    if test_str == None:
        return False
    else:
        return True




while True:
    pppppp = ''





    root = Tk()
    root.resizable(False, False)
    var = StringVar()
    root.title("代码合集Insider Preview...评估版本:Build24501")
    root.geometry('800x650')
    text = Text(root, width=520, height=10, undo=True, autoseparators=False, font=('微软雅黑', 20), fg='blue',
                bg='sky blue')
    tex = Text(root, width=520, height=1, undo=True, autoseparators=False, font=('微软雅黑', 20))
    te = Text(root, width=520, height=1, undo=True, autoseparators=False, font=('微软雅黑', 20), fg='red')
    t = Text(root, width=520, height=1, undo=True, autoseparators=False, font=('微软雅黑', 20), fg='red')

    # 适用 pack(fill=X) 可以设置文本域的填充模式。比如 X表示沿水平方向填充，Y表示沿垂直方向填充，BOTH表示沿水平、垂直方向填充

    # INSERT 光标处插入；END 末尾处插入
    text.insert(INSERT, '1是买东西问题，2是自制乘法函数，3是贪吃蛇，4是天气查询，5是小游戏，6是猜数字，7是画海绵宝宝，8是多啦a梦，9是画小猪佩奇，'
                        '10是画乔治，11可以转EXE，12是吃豆人，13是四子棋，'
                        '14是井字棋，15是将数字滑动到位的拼图游戏，16是人工智障，17是乒乓球游戏，18是画冰墩墩，19是不知道，20是学生管理系统'
                        '，21是小黑子，22是迷宫(有点难操作。。)，23是石头剪刀布，24是漩涡(好看！)，25是计算小王子，r是退出')
    tex.pack()
    te.pack()
    t.pack()


    tex.insert(INSERT, '公告:报错率减少，时间炸弹异常修复，不能修改窗口大小')
    te.insert(INSERT,'版本号:Insider Preview...评估版本:Build24501  作者(网名):小树叶')
    t.insert(INSERT,'时间炸弹:2024-5-31过期')
    # root.mainloop()
    # tk=Tk()
    # can=Canvas(tk,width=400,height=400)
    # can.pack()
    #
    # ppoa=PhotoImage(file='C:\\sss.gif')
    # can.create_image(0,0,anchor=NW,image=ppoa)
    # width 一行可见的字符数；height 显示的行数
    text.pack()
    text.config(state=DISABLED)
    tex.config(state=DISABLED)
    te.config(state=DISABLED)
    t.config(state=DISABLED)
    def callback():
        global pppppp
        global E2
        pppppp = E2.get()
        root.destroy()


    # 定义一个文本框
    E2 = Entry(root,textvariable=var,font=('微软雅黑',20))
    but_set = Button(root, text="  使 用  ", command=callback,font=('微软雅黑',20))  # command参数来调用函数

    but_set.pack(pady=10)
    E2.pack()
    root.mainloop()

    if pppppp == '':

        roo = Tk()
        vapr = StringVar()
        roo.resizable(False, False)
        roo.title("代码合集3.57的疑难解答")
        roo.geometry('700x650')
        txt = Text(width=520, height=10, undo=True, autoseparators=False, font=('微软雅黑', 20), fg='blue',bg='sky blue')
        txt.insert(INSERT, '你要退出吗？回答：好/不好''    Y/N')
        txt.pack()
        txt.config(state=DISABLED)
        def ca():
            global lll
            global E
            global root
            lll = E.get()
            root.destroy()
        E=Entry(roo, textvariable=vapr, font=('微软雅黑', 20))
        but_set=Button(roo, text="  使 用  ", command=ca, font=('微软雅黑', 20))  # command参数来调用函数



        lll = input('')
        if lll == '好':
            break
        elif lll == '不好':

            continue
        elif lll == 'Y' or lll == 'y':
            break
        elif lll == 'N' or lll == 'n':
            continue


    if pppppp == 'r' or pppppp == 'R':
        break
    # 创建Tkinter窗口
    sss = is_contains_english(pppppp)
    ddd = is_contains_chinese(pppppp)
    psd = ppppppppp(pppppp)
    if sss == True or ddd == True or psd == True:
        messagebox.showinfo('提示', '说点人话哦，™的傻逼（说数字！），再来')
        print('                               ')
        continue
    sss = ''
    ddd = ''
    psd = ''



    pppppp = int(pppppp)

    if pppppp == 1:
        messagebox.showinfo('提示', '制作中......')
        continue
        print('你要买几个写字笔🖊')
        a = input()
        print('你要买几个记事本😂')
        s = input()
        print('你要买几个直尺🤩')
        d = input()

        print('你要有多少钱( $ _ $ )💴🤑')
        f = input()
        a = int(a)
        s = int(s)
        d = int(d)
        f = float(f)
        if 1 <= a <= 10 and 1 <= s <= 10 and 1 <= d <= 10:
            if f >= 2 * a + 5 * s + 3 * d:
                g = a * 2
                h = s * 5
                j = d * 3
                l = 0
                z = a + s + d
                v = g + h + j - f
                v = str(v)
                if f < z:
                    print('你还需要', v)
                else:
                    print('可以买！')
                    g = a * 2
                    h = s * 5
                    j = d * 3
                    l = f - (g + h + j)
                    print('你买了', a, '支笔')
                    print('你买了', s, '个记事本')
                    print('你买了', a, '个直尺')
                    print(l)

        else:
            print('商店的货品不足')
    elif pppppp == 2:
        messagebox.showinfo('提示', '制作中......')
        continue
        a = input('输入一个数字:')
        d = input('再输入一个数字:')
        a = int(a)
        d = int(d)


        def s(n1, n2):
            r = n1 * n2
            print(r)


        s(a, d)
    elif pppppp == 3:
        import pygame
        import random

        # 初始化pygame
        pygame.init()

        # 定义游戏画面大小和速度
        window_width = 500
        window_height = 500
        speed = 10

        # 创建窗口
        window = pygame.display.set_mode((window_width, window_height))

        # 定义颜色
        black = pygame.Color(0, 0, 0)
        white = pygame.Color(255, 255, 255)
        red = pygame.Color(255, 0, 0)
        green = pygame.Color(0, 255, 0)
        blue = pygame.Color(0, 0, 255)

        # 设置游戏标题
        pygame.display.set_caption('贪吃蛇')

        # 设置时钟
        clock = pygame.time.Clock()

        # 定义蛇的初始位置和大小
        snake_position = [100, 50]
        snake_body = [[100, 50], [90, 50], [80, 50]]

        # 定义食物的初始位置和大小
        food_position = [random.randrange(1, (window_width // 10)) * 10,
                         random.randrange(1, (window_height // 10)) * 10]
        food_spawned = True

        # 定义蛇的移动方向
        direction = 'RIGHT'
        change_to = direction


        # 定义游戏结束函数
        def game_over():
            font = pygame.font.SysFont('Arial', 30)
            game_over_text = font.render('Game Over!', True, red)
            game_over_rect = game_over_text.get_rect()
            game_over_rect.midtop = (window_width / 2, window_height / 4)
            window.blit(game_over_text, game_over_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            pygame.quit()
            quit()


        # 开始游戏循环
        while True:
            for event in pygame.event.get():
                # 监听窗口关闭事件
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # 监听按键事件
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        change_to = 'RIGHT'
                    elif event.key == pygame.K_LEFT:
                        change_to = 'LEFT'
                    elif event.key == pygame.K_UP:
                        change_to = 'UP'
                    elif event.key == pygame.K_DOWN:
                        change_to = 'DOWN'

            # 判断蛇头是否与食物重合
            if snake_position == food_position:
                food_spawned = False
            else:
                snake_body.pop()

            # 生成新的食物
            if not food_spawned:
                food_position = [random.randrange(1, (window_width // 10)) * 10,
                                 random.randrange(1, (window_height // 10)) * 10]
                food_spawned = True

            # 改变蛇的移动方向
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'
            elif change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            elif change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            elif change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'

            # 移动蛇
            if direction == 'RIGHT':
                snake_position[0] += speed
            elif direction == 'LEFT':
                snake_position[0] -= speed
            elif direction == 'UP':
                snake_position[1] -= speed
            elif direction == 'DOWN':
                snake_position[1] += speed

            # 添加新的蛇头
            snake_head = list(snake_position)
            snake_body.insert(0, snake_head)

            # 判断游戏是否结束
            if snake_position[0] < 0 or snake_position[0] > window_width - 10:
                game_over()
            if snake_position[1] < 0 or snake_position[1] > window_height - 10:
                game_over()
            for block in snake_body[1:]:
                if snake_position == block:
                    game_over()

            # 绘制游戏画面
            window.fill(black)
            for block in snake_body:
                pygame.draw.rect(window, green, pygame.Rect(
                    block[0], block[1], 10, 10))
            pygame.draw.rect(window, blue, pygame.Rect(
                food_position[0], food_position[1], 10, 10))
            pygame.display.update()

            # 设置游戏帧率
            clock.tick(10)
    elif pppppp == 4:
        messagebox.showinfo('提示', '制作中......')
        continue
        import wftools as t

        print(t.weather())
    elif pppppp == 5:
        import pygame

        # 初始化pygame
        pygame.init()

        # 设置窗口大小
        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))

        # 设置球的初始位置
        ball_position = [screen_width / 2, screen_height / 2]
        ball_radius = 20

        # 游戏主循环标志
        running = True

        # 游戏主循环
        while running:
            # 遍历事件
            for event in pygame.event.get():
                # 检查是否点击了关闭按钮
                if event.type == pygame.QUIT:
                    running = False

                # 检查鼠标点击事件
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 获取鼠标点击的位置
                    ball_position[0] = event.pos[0]
                    ball_position[1] = event.pos[1]

            # 设置背景颜色
            screen.fill((255, 255, 255))

            # 绘制球
            pygame.draw.circle(screen, (0, 0, 0), ball_position, ball_radius)

            # 更新屏幕显示
            pygame.display.flip()

    elif pppppp == 6:
        import random


        def guess_number():
            target = random.randint(1, 10)  # 生成随机数作为目标值

            while True:
                try:
                    number = int(input("请输入一个介于1到100之间的整数："))

                    if number < target:
                        print("太低了！")

                    elif number > target:
                        print("太高了！")

                    else:
                        print("恭喜你猜对了！")
                        break

                except ValueError:
                    print("无效的输入。请重新输入一个整数。")


        guess_number()
    elif pppppp == 7:
        import turtle


        def plotLine(points, pencolor=None, width=None, speed=None):
            '''
            功能：画折线
            参数：
            - points : 一系列点，用列表或元组表示
            - pencolor : 画笔颜色，默认不变
            - width : 画笔宽度，默认不变
            - speed : 绘制速度，默认不变
            '''
            # 记录旧参数
            oldpencolor = turtle.pencolor()
            oldwidth = turtle.width()
            oldspeed = turtle.speed()

            # 修改新参数
            if pencolor is not None:
                turtle.pencolor(pencolor)
            if width is not None:
                turtle.width(width)
            if speed is not None:
                turtle.speed(speed)

            # 绘制折线
            turtle.up()
            turtle.goto(points[0])
            turtle.down()
            for point in points[1:]:
                turtle.goto(point)

            # 恢复旧参数
            turtle.pencolor(oldpencolor)
            turtle.width(oldwidth)
            turtle.speed(oldspeed)


        def plotPoly(points, fill=False, pencolor=None, fillcolor=None,
                     width=None, speed=None):
            '''
            功能：绘制封闭多边形
            '''
            # 保存旧参数
            oldfillcolor = turtle.fillcolor()

            # 更新新参数
            if fillcolor is not None:
                turtle.fillcolor(fillcolor)

            # 绘制封闭多边形
            points_plotline = list(points) + [points[0]]
            if fill:
                turtle.begin_fill()
                plotLine(points_plotline, pencolor, width, speed)
                turtle.end_fill()
            else:
                plotLine(points_plotline, pencolor, width, speed)

            # 恢复旧参数
            turtle.fillcolor(oldfillcolor)


        # 设置一些参数
        turtle.setup(600, 559, 50, 50)
        turtle.speed(10)
        turtle.turtlesize(1.5, 1.5, 1.5)

        # 绘画

        # 脸部轮廓
        points = [
            (-139, 267), (-144, 265), (-148, 264), (-152, 260), (-156, 255),
            (-160, 247), (-163, 232), (-162, 226), (-162, 221), (-163, 215),
            (-165, 207), (-172, 191), (-176, 178), (-181, 163), (-182, 156),
            (-183, 150), (-181, 142), (-181, 132), (-181, 120), (-181, 112),
            (-184, 103), (-188, 96), (-190, 89), (-192, 84), (-195, 76),
            (-196, 73), (-197, 58), (-197, 47), (-195, 35), (-195, 22),
            (-196, 10), (-197, 1), (-199, -5), (-200, -9), (-200, -20),
            (-198, -27), (-196, -35), (-195, -45), (-195, -55), (-196, -62),
            (-197, -70), (-197, -77), (-196, -81), (-193, -86), (-189, -89),
            (-185, -90), (-178, -92), (-170, -94), (-153, -94), (-149, -96),
            (-143, -99), (-138, -102), (-134, -105), (-129, -106), (-119, -107),
            (-104, -107), (-94, -108), (-87, -108), (-80, -111), (-71, -117),
            (-64, -119), (-49, -121), (-33, -122), (-23, -123), (-15, -125),
            (-8, -128), (0, -132), (7, -135), (15, -137), (24, -137),
            (35, -138), (40, -140), (57, -145), (60, -146), (66, -147),
            (71, -147), (76, -146), (83, -143), (91, -139), (97, -138),
            (116, -141), (144, -139), (147, -131), (152, -111), (154, -106),
            (156, -103), (156, -79), (156, -75), (159, -71), (164, -63),
            (168, -57), (170, -52), (171, -44), (172, -23), (173, -18),
            (175, -14), (182, -7), (190, 2), (194, 9), (197, 15),
            (199, 24), (201, 39), (204, 47), (208, 53), (215, 57),
            (222, 61), (225, 66), (228, 74), (231, 87), (233, 95),
            (236, 99), (242, 105), (247, 109), (249, 113), (253, 118),
            (255, 123), (255, 127), (253, 132), (250, 135), (245, 139),
            (241, 143), (239, 147), (237, 150), (236, 157), (235, 160),
            (233, 163), (230, 166), (227, 168), (222, 170), (216, 175),
            (214, 179), (211, 185), (211, 193), (209, 198), (205, 204),
            (202, 207), (198, 209), (171, 209), (166, 209), (161, 212),
            (154, 217), (148, 220), (142, 222), (136, 223), (128, 223),
            (120, 221), (114, 220), (107, 222), (100, 223), (95, 225),
            (76, 234), (70, 237), (65, 238), (55, 238), (37, 238),
            (33, 239), (23, 242), (12, 245), (5, 246), (-4, 245),
            (-14, 244), (-22, 242), (-29, 242), (-38, 244), (-44, 247),
            (-52, 251), (-57, 254), (-62, 257), (-71, 258), (-95, 258),
            (-100, 258), (-105, 258), (-111, 262), (-117, 264), (-127, 267),
        ]
        plotPoly(points, True, pencolor=(0.55, 0.56, 0.1),
                 fillcolor=(1.0, 0.96, 0.34), width=5)

        # 脸部线条
        points = [
            (199, 208), (199, 201), (199, 193), (198, 190), (195, 185),
            (191, 178), (186, 172), (180, 166), (174, 161), (169, 155),
            (166, 149), (165, 144), (163, 128), (162, 121), (161, 117),
            (158, 111), (154, 105), (152, 101), (150, 99), (146, 95),
            (142, 91), (138, 87), (136, 84), (135, 79), (135, 72),
            (134, 65), (134, 57), (133, 53), (132, 49), (130, 45),
            (126, 40), (123, 36), (118, 31), (113, 27), (110, 22),
            (107, 18), (105, 12), (106, 6), (106, 0), (106, -6),
            (105, -14), (104, -18), (100, -24), (96, -29), (92, -35),
            (89, -41), (87, -45), (85, -49), (85, -58), (86, -70),
            (85, -81), (84, -87), (82, -92), (80, -96), (77, -101),
            (75, -105), (72, -109), (71, -112), (71, -129), (71, -134),
            (69, -138), (68, -140), (66, -142), (63, -144), (61, -145),
        ]
        plotLine(points, pencolor=(0.55, 0.56, 0.1), width=4)

        # 脸部斑点
        points = [
            (-129, 238), (-134, 237), (-139, 235), (-143, 231), (-145, 226),
            (-147, 221), (-147, 213), (-145, 208), (-142, 204), (-139, 202),
            (-136, 202), (-131, 203), (-127, 206), (-123, 210), (-121, 215),
            (-119, 220), (-118, 224), (-118, 226), (-119, 229), (-121, 232),
            (-123, 235), (-126, 237),
        ]
        plotPoly(points, True, pencolor=(0.66, 0.73, 0.15),
                 fillcolor=(0.66, 0.73, 0.15), width=1)

        # 脸部斑点
        points = [
            (-149, 189), (-151, 190), (-154, 190), (-157, 188), (-160, 185),
            (-162, 181), (-163, 178), (-163, 170), (-161, 168), (-159, 166),
            (-154, 165), (-150, 167), (-148, 170), (-146, 174), (-144, 177),
            (-145, 184), (-147, 187),
        ]
        plotPoly(points, True, pencolor=(0.66, 0.73, 0.15),
                 fillcolor=(0.66, 0.73, 0.15), width=1)

        # 脸部斑点
        points = [
            (147, 195), (143, 196), (140, 195), (136, 193), (132, 191),
            (129, 186), (127, 181), (125, 177), (125, 171), (127, 165),
            (130, 160), (134, 158), (138, 156), (143, 155), (148, 156),
            (152, 160), (155, 165), (156, 170), (157, 177), (156, 183),
            (154, 188), (151, 192),
        ]
        plotPoly(points, True, pencolor=(0.66, 0.73, 0.15),
                 fillcolor=(0.66, 0.73, 0.15), width=1)

        # 脸部斑点
        points = [
            (-154, 21), (-159, 20), (-164, 18), (-168, 14), (-172, 10),
            (-175, 5), (-176, 1), (-176, -6), (-174, -12), (-171, -17),
            (-167, -20), (-163, -22), (-157, -23), (-154, -22), (-149, -19),
            (-145, -15), (-142, -10), (-141, -4), (-141, 3), (-142, 8),
            (-143, 13), (-146, 16), (-149, 19),
        ]
        plotPoly(points, True, pencolor=(0.66, 0.73, 0.15),
                 fillcolor=(0.66, 0.73, 0.15), width=1)

        # 脸部斑点
        points = [
            (-147, -43), (-151, -43), (-155, -46), (-159, -50), (-162, -54),
            (-164, -59), (-164, -64), (-161, -69), (-156, -71), (-150, -71),
            (-145, -68), (-141, -64), (-140, -58), (-139, -54), (-140, -49),
            (-143, -45),
        ]
        plotPoly(points, True, pencolor=(0.66, 0.73, 0.15),
                 fillcolor=(0.66, 0.73, 0.15), width=1)

        # 脸部斑点
        points = [
            (65, -24), (59, -24), (56, -26), (52, -29), (50, -34),
            (49, -38), (50, -44), (52, -49), (55, -51), (58, -52),
            (62, -51), (66, -48), (69, -44), (71, -40), (71, -33),
            (69, -28),
        ]
        plotPoly(points, True, pencolor=(0.66, 0.73, 0.15),
                 fillcolor=(0.66, 0.73, 0.15), width=1)

        # 脸部斑点
        points = [
            (42, -66), (38, -67), (32, -71), (28, -75), (26, -80),
            (24, -85), (24, -94), (26, -101), (28, -106), (31, -109),
            (34, -111), (38, -112), (45, -111), (51, -107), (55, -102),
            (57, -96), (58, -89), (59, -82), (57, -76), (54, -71),
            (52, -69), (47, -67),
        ]
        plotPoly(points, True, pencolor=(0.66, 0.73, 0.15),
                 fillcolor=(0.66, 0.73, 0.15), width=1)

        # 脸旁斑点
        points = [
            (204, 160), (195, 160), (191, 157), (187, 153), (184, 148),
            (182, 143), (182, 137), (183, 131), (184, 124), (186, 119),
            (189, 116), (193, 112), (198, 110), (204, 109), (210, 111),
            (215, 114), (218, 119), (220, 126), (220, 133), (219, 141),
            (217, 148), (214, 153), (210, 157),
        ]
        plotPoly(points, True, pencolor=(0.57, 0.57, 0.01),
                 fillcolor=(0.57, 0.57, 0.01), width=1)

        # 脸旁斑点
        points = [
            (187, 88), (183, 87), (180, 85), (177, 81), (175, 76),
            (176, 70), (178, 64), (181, 59), (185, 57), (190, 57),
            (194, 60), (197, 64), (199, 69), (199, 73), (199, 76),
            (197, 80), (194, 84), (191, 86),
        ]
        plotPoly(points, True, pencolor=(0.57, 0.57, 0.01),
                 fillcolor=(0.57, 0.57, 0.01), width=1)

        # 脸旁斑点
        points = [
            (145, 47), (150, 46), (156, 44), (160, 41), (163, 37),
            (164, 32), (166, 26), (166, 18), (165, 12), (164, 7),
            (161, 3), (158, -1), (155, -3), (147, -3), (142, 0),
            (137, 4), (134, 11), (132, 20), (133, 28), (135, 35),
            (139, 41), (142, 44),
        ]
        plotPoly(points, True, pencolor=(0.57, 0.57, 0.01),
                 fillcolor=(0.57, 0.57, 0.01), width=1)

        # 脸旁斑点
        points = [
            (136, -23), (141, -24), (145, -27), (147, -30), (148, -34),
            (148, -38), (147, -42), (145, -45), (143, -47), (139, -47),
            (136, -44), (133, -41), (131, -36), (130, -31), (132, -26),
        ]
        plotPoly(points, True, pencolor=(0.57, 0.57, 0.01),
                 fillcolor=(0.57, 0.57, 0.01), width=1)

        # 嘴巴
        points = [
            (-85, 17), (-95, -13), (-103, -33), (-107, -46), (-108, -51),
            (-108, -56), (-105, -60), (-99, -67), (-93, -70), (-86, -74),
            (-76, -78), (-64, -82), (-51, -83), (-35, -83), (-27, -81),
            (-21, -79), (-14, -75), (-3, -67), (9, -56), (19, -44),
            (29, -29), (39, -12), (48, 7), (53, 23), (60, 38),
            (56, 40), (51, 37), (43, 30), (33, 25), (20, 20),
            (10, 16), (-3, 13), (-19, 11), (-35, 10), (-53, 11),
            (-67, 13), (-76, 15),
        ]
        plotPoly(points, True, pencolor=(0.05, 0.0, 0.05),
                 fillcolor=(0.54, 0.12, 0.02), width=4)

        # 舌头
        points = [
            (-98, -66), (-93, -59), (-88, -53), (-82, -49), (-76, -46),
            (-69, -44), (-62, -43), (-53, -44), (-45, -46), (-38, -48),
            (-33, -50), (-31, -52), (-26, -49), (-20, -47), (-14, -46),
            (-8, -45), (-1, -46), (5, -48), (11, -52), (6, -59),
            (-2, -65), (-9, -71), (-18, -77), (-25, -81), (-30, -82),
            (-39, -84), (-55, -83), (-67, -81), (-78, -78), (-86, -74),
            (-92, -71),
        ]
        plotPoly(points, True, pencolor=(0.02, 0.03, 0.06),
                 fillcolor=(0.95, 0.61, 0.55), width=4)

        # 舌头
        points = [
            (-33, -51), (-36, -54), (-38, -56), (-40, -58), (-43, -61),
            (-45, -64), (-47, -67), (-43, -64), (-41, -62), (-39, -60),
            (-36, -58), (-32, -55), (-29, -53), (-28, -52), (-26, -50),
            (-30, -51),
        ]
        plotPoly(points, True, pencolor=(0.02, 0.03, 0.06),
                 fillcolor=(0.02, 0.03, 0.06), width=0)

        # 牙齿
        points = [
            (-101, 22), (-112, -6), (-98, -13), (-92, -15), (-86, -16),
            (-81, -17), (-77, -17), (-73, -5), (-70, 6), (-69, 13),
            (-74, 14), (-80, 15), (-86, 17), (-91, 19), (-96, 21),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.0, 0.02),
                 fillcolor=(1.0, 1.0, 1.0), width=4)

        # 牙齿
        points = [
            (-53, 11), (-58, -16), (-58, -18), (-54, -20), (-43, -23),
            (-30, -25), (-23, -26), (-20, -20), (-18, -11), (-17, -1),
            (-17, 10), (-24, 10), (-31, 10), (-41, 10), (-48, 10),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.0, 0.02),
                 fillcolor=(1.0, 1.0, 1.0), width=4)

        # 鼻子
        points = [
            (-99, 22), (-107, 26), (-117, 32), (-127, 39), (-136, 46),
            (-143, 52), (-145, 53), (-145, 54),
        ]
        plotLine(points, pencolor=(0.0, 0.0, 0.02), width=4)

        # 鼻子
        points = [
            (-145, 54), (-144, 55), (-138, 55), (-124, 56), (-115, 57),
        ]
        plotLine(points, pencolor=(0.0, 0.0, 0.02), width=2)

        # 鼻子
        points = [
            (-56, 49), (-67, 48), (-80, 48), (-92, 50), (-103, 53),
            (-114, 58), (-123, 63), (-131, 69), (-141, 76), (-149, 84),
            (-154, 90), (-158, 99), (-160, 106), (-160, 114), (-159, 116),
            (-158, 118), (-156, 120), (-154, 121), (-151, 122), (-141, 122),
            (-138, 121), (-135, 120), (-133, 119), (-129, 116), (-123, 111),
            (-117, 105), (-111, 99), (-104, 93), (-95, 86), (-87, 81),
            (-79, 77), (-71, 73), (-63, 71), (-56, 69), (-52, 68),
        ]
        plotLine(points, pencolor=(0.0, 0.0, 0.02), width=4)

        # 右眼
        points = [
            (-71, 198), (-83, 198), (-93, 196), (-102, 194), (-112, 189),
            (-118, 184), (-123, 179), (-129, 173), (-134, 165), (-138, 157),
            (-141, 149), (-143, 140), (-143, 133), (-143, 123), (-140, 122),
            (-137, 121), (-135, 120), (-131, 118), (-126, 113), (-118, 106),
            (-113, 101), (-106, 95), (-99, 89), (-91, 84), (-78, 76),
            (-67, 72), (-61, 70), (-57, 70), (-54, 72), (-49, 75),
            (-44, 78), (-39, 81), (-35, 84), (-28, 92), (-23, 99),
            (-19, 110), (-16, 122), (-15, 134), (-15, 143), (-16, 154),
            (-19, 162), (-24, 170), (-31, 179), (-38, 186), (-46, 190),
            (-53, 194), (-60, 196),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.0, 0.02),
                 fillcolor=(1.0, 1.0, 1.0), width=3)

        # 右眼珠
        points = [
            (-69, 155), (-76, 155), (-82, 153), (-87, 150), (-91, 145),
            (-93, 140), (-94, 135), (-95, 129), (-93, 123), (-89, 118),
            (-86, 115), (-82, 112), (-78, 111), (-69, 111), (-63, 112),
            (-59, 115), (-55, 119), (-52, 123), (-50, 129), (-49, 134),
            (-50, 139), (-53, 144), (-57, 149), (-62, 153),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.0, 0.02),
                 fillcolor=(0.01, 0.63, 0.82), width=3)

        # 右眼珠
        points = [
            (-71, 145), (-76, 144), (-79, 142), (-82, 139), (-84, 135),
            (-84, 131), (-82, 126), (-79, 123), (-76, 121), (-72, 120),
            (-67, 121), (-63, 124), (-61, 127), (-60, 130), (-60, 135),
            (-61, 138), (-63, 141), (-66, 143),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.0, 0.02),
                 fillcolor=(0.0, 0.0, 0.02), width=1)

        # 右眼睫毛
        points = [
            (-97, 196), (-101, 214), (-101, 215), (-95, 217), (-93, 217),
            (-91, 198), (-91, 197),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.0, 0.02),
                 fillcolor=(0.0, 0.0, 0.02), width=1)

        # 右眼睫毛
        points = [
            (-62, 197), (-59, 215), (-53, 215), (-52, 214), (-52, 213),
            (-57, 196),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.0, 0.02),
                 fillcolor=(0.0, 0.0, 0.02), width=1)

        # 右眼睫毛
        points = [
            (-35, 184), (-24, 199), (-23, 199), (-19, 195), (-32, 180),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.0, 0.02),
                 fillcolor=(0.0, 0.0, 0.02), width=1)

        # 左眼
        points = [
            (30, 171), (19, 171), (9, 168), (-1, 164), (-8, 160),
            (-15, 154), (-21, 148), (-27, 140), (-32, 132), (-35, 123),
            (-37, 115), (-38, 108), (-37, 97), (-36, 89), (-32, 80),
            (-28, 72), (-22, 63), (-16, 57), (-11, 52), (-2, 47),
            (8, 43), (17, 40), (25, 40), (35, 40), (47, 43),
            (58, 47), (67, 52), (74, 59), (81, 68), (86, 79),
            (90, 89), (92, 102), (92, 115), (89, 128), (84, 138),
            (77, 148), (72, 154), (62, 162), (51, 167), (42, 170),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.0, 0.02),
                 fillcolor=(1.0, 1.0, 1.0), width=4)

        # 左眼珠
        points = [
            (25, 133), (19, 132), (13, 129), (9, 126), (6, 122),
            (4, 117), (3, 111), (3, 103), (6, 97), (10, 93),
            (15, 90), (20, 88), (25, 87), (33, 89), (39, 93),
            (44, 99), (47, 107), (47, 115), (45, 120), (41, 125),
            (38, 129), (33, 131),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.0, 0.02),
                 fillcolor=(0.06, 0.65, 0.88), width=4)

        # 左眼珠
        points = [
            (27, 124), (21, 123), (18, 121), (16, 119), (14, 116),
            (13, 111), (15, 104), (17, 101), (20, 99), (25, 98),
            (31, 99), (35, 102), (37, 106), (38, 111), (36, 117),
            (34, 120), (31, 122),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.0, 0.02),
                 fillcolor=(0.0, 0.0, 0.02), width=1)

        # 左眼睫毛
        points = [
            (11, 170), (8, 188), (13, 189), (16, 171),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.0, 0.02),
                 fillcolor=(0.0, 0.0, 0.02), width=1)

        # 左眼睫毛
        points = [
            (45, 170), (50, 187), (51, 187), (57, 186), (57, 186),
            (50, 168),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.0, 0.02),
                 fillcolor=(0.0, 0.0, 0.02), width=1)

        # 左眼睫毛
        points = [
            (72, 155), (82, 170), (83, 170), (87, 166), (87, 165),
            (74, 151),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.0, 0.02),
                 fillcolor=(0.0, 0.0, 0.02), width=1)

        # 脸上疙瘩
        points = [
            (40, 36), (37, 43), (37, 50), (38, 56), (42, 62),
            (49, 67), (56, 70), (65, 70), (72, 68), (78, 64),
            (80, 62), (77, 56), (75, 53), (69, 47), (64, 44),
            (59, 43), (54, 42), (50, 40), (46, 38),
        ]
        plotPoly(points, True, pencolor=(1.0, 0.96, 0.34),
                 fillcolor=(1.0, 0.96, 0.34), width=0)

        # 脸上疙瘩
        points = [
            (50, 43), (52, 43), (56, 41), (61, 38), (64, 36),
            (66, 34), (68, 32),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.0, 0.02),
                 fillcolor=(0.0, 0.0, 0.02), width=2)

        # 脸上疙瘩
        points = [
            (40, 35), (37, 40), (36, 48), (37, 53), (39, 59),
            (43, 64), (46, 66), (52, 69), (58, 70), (66, 70),
            (71, 68), (76, 65), (81, 62), (86, 57), (89, 53),
            (92, 48), (94, 42), (93, 35), (90, 28), (87, 24),
            (83, 20), (77, 17), (73, 16), (66, 16),
        ]
        plotLine(points, pencolor=(0.83, 0.37, 0.21), width=4)

        # 脸上疙瘩
        points = [
            (64, 48), (65, 49), (69, 49), (70, 48), (70, 43),
            (67, 45), (66, 46),
        ]
        plotPoly(points, True, pencolor=(0.83, 0.37, 0.21),
                 fillcolor=(0.83, 0.37, 0.21), width=0)

        # 脸上疙瘩
        points = [
            (62, 61), (63, 62), (64, 63), (66, 63), (68, 61),
            (69, 60), (69, 57), (68, 57), (65, 58), (63, 59),
            (62, 60),
        ]
        plotPoly(points, True, pencolor=(0.83, 0.37, 0.21),
                 fillcolor=(0.83, 0.37, 0.21), width=0)

        # 脸上疙瘩
        points = [
            (78, 51), (78, 52), (79, 53), (81, 52), (83, 50),
            (84, 47), (83, 45), (82, 45), (80, 47), (79, 49),
            (78, 50),
        ]
        plotPoly(points, True, pencolor=(0.83, 0.37, 0.21),
                 fillcolor=(0.83, 0.37, 0.21), width=0)

        # 裤子
        points = [
            (-186, -121), (64, -176), (61, -223), (-182, -165), (-185, -146),
            (-186, -140),
        ]
        plotPoly(points, True, pencolor=(0.02, 0.0, 0.01),
                 fillcolor=(0.84, 0.55, 0.2), width=3)

        # 裤子
        points = [
            (64, -176), (143, -161), (143, -197), (64, -224),
        ]
        plotPoly(points, True, pencolor=(0.04, 0.02, 0.02),
                 fillcolor=(0.61, 0.35, 0.03), width=2)

        # 裤子
        points = [
            (-189, -93), (-188, -117), (-187, -144), (-183, -167), (58, -225),
            (64, -225), (143, -196), (143, -137),
        ]
        plotLine(points, pencolor=(0.04, 0.02, 0.02), width=6)

        # 裤子
        points = [
            (65, -149), (62, -223),
        ]
        plotLine(points, pencolor=(0.04, 0.02, 0.02), width=5)

        # 右袖子
        points = [
            (-198, -42), (-203, -51), (-207, -61), (-210, -72), (-212, -81),
            (-212, -87), (-209, -92), (-203, -98), (-197, -102), (-190, -103),
        ]
        plotLine(points, pencolor=(0.02, 0.0, 0.01), width=5)

        # 左袖子
        points = [
            (128, -83), (122, -85), (117, -91), (113, -98), (109, -106),
            (106, -117), (104, -128), (103, -139), (103, -146), (106, -150),
            (115, -154), (124, -156), (134, -155), (144, -151), (151, -146),
            (152, -136), (150, -124), (147, -110), (141, -94), (138, -86),
            (133, -84),
        ]
        plotPoly(points, True, pencolor=(0.06, 0.06, 0.07),
                 fillcolor=(1.0, 1.0, 1.0), width=5)

        # 右手轮廓
        points = [
            (-185, -159), (-190, -160), (-193, -162), (-195, -167), (-198, -173),
            (-199, -180), (-200, -193), (-204, -198), (-207, -202), (-208, -205),
            (-207, -207), (-205, -210), (-201, -211), (-196, -211), (-195, -215),
            (-193, -220), (-191, -226), (-188, -230), (-184, -232), (-180, -232),
            (-178, -230), (-176, -233), (-172, -235), (-169, -235), (-166, -234),
            (-163, -231), (-159, -226), (-156, -223), (-153, -221), (-153, -217),
            (-153, -210), (-156, -203), (-158, -198), (-158, -190), (-155, -175),
            (-183, -167),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.01, 0.0),
                 fillcolor=(1.0, 0.96, 0.33), width=5)

        # 右手指
        points = [
            (-184, -188), (-185, -193), (-187, -198), (-189, -203), (-191, -206),
            (-194, -209), (-196, -211),
        ]
        plotLine(points, pencolor=(0.02, 0.0, 0.0), width=4)

        # 右手指
        points = [
            (-178, -231), (-177, -227), (-176, -223), (-177, -219), (-179, -213),
            (-180, -207), (-180, -204), (-180, -201), (-175, -198), (-171, -196),
            (-166, -196), (-168, -197), (-168, -202), (-168, -206), (-166, -210),
            (-163, -216), (-161, -220), (-160, -227),
        ]
        plotLine(points, pencolor=(0.05, 0.06, 0.11), width=4)

        # 左手臂和手轮廓
        points = [
            (120, -155), (125, -156), (130, -156), (134, -156), (132, -191),
            (130, -217), (131, -220), (133, -223), (136, -226), (139, -231),
            (142, -236), (144, -242), (145, -250), (146, -272), (145, -277),
            (144, -281), (103, -281), (105, -278), (107, -273), (107, -268),
            (107, -262), (105, -260), (103, -259), (100, -261), (94, -264),
            (90, -267), (87, -267), (84, -266), (81, -264), (80, -260),
            (82, -258), (85, -254), (91, -252), (95, -248), (97, -243),
            (99, -238), (100, -233), (102, -231), (105, -228), (109, -227),
            (113, -225), (115, -223), (116, -219), (117, -209), (119, -181),
        ]
        plotPoly(points, True, pencolor=(0.01, 0.0, 0.0),
                 fillcolor=(1.0, 0.96, 0.33), width=5)

        # 左手指
        points = [
            (121, -281), (122, -277), (123, -272), (124, -267), (124, -261),
        ]
        plotLine(points, pencolor=(0.01, 0.0, 0.0), width=4)

        # 左手指
        points = [
            (132, -281), (133, -277), (134, -271), (134, -265), (134, -260),
        ]
        plotLine(points, pencolor=(0.01, 0.0, 0.0), width=4)

        # 右裤腿
        points = [
            (-131, -181), (-132, -200), (-119, -206), (-104, -208), (-86, -208),
            (-75, -206), (-67, -203), (-62, -198), (-88, -191), (-112, -185),
        ]
        plotPoly(points, True, pencolor=(0.01, 0.0, 0.0),
                 fillcolor=(0.8, 0.56, 0.18), width=5)

        # 左裤腿
        points = [
            (-6, -210), (-9, -226), (-6, -230), (8, -234), (24, -237),
            (41, -237), (50, -234), (58, -230), (60, -226),
        ]
        plotPoly(points, True, pencolor=(0.04, 0.05, 0.08),
                 fillcolor=(0.82, 0.56, 0.15), width=5)

        # 右腿
        points = [
            (-104, -208), (-96, -208), (-90, -207), (-86, -226), (-84, -248),
            (-91, -250), (-97, -250), (-101, -250), (-102, -234), (-104, -217),
            (-105, -210),
        ]
        plotPoly(points, True, pencolor=(0.02, 0.02, 0.04),
                 fillcolor=(0.99, 0.95, 0.36), width=4)

        # 右袜子
        points = [
            (-100, -250), (-84, -248), (-80, -281), (-99, -282), (-100, -265),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.03, 0.02),
                 fillcolor=(0.98, 0.98, 0.98), width=4)

        # 右袜子
        points = [
            (-98, -260), (-83, -260),
        ]
        plotPoly(points, True, pencolor=(0.39, 0.46, 0.49),
                 fillcolor=(0.39, 0.46, 0.49), width=2)

        # 右袜子
        points = [
            (-98, -271), (-83, -271),
        ]
        plotLine(points, pencolor=(0.86, 0.31, 0.24), width=4)

        # 左腿
        points = [
            (18, -236), (28, -237), (37, -237), (40, -255), (40, -268),
            (31, -269), (22, -269), (19, -248),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.01, 0.02),
                 fillcolor=(1.0, 0.93, 0.42), width=4)

        # 左袜子
        points = [
            (22, -269), (33, -269), (40, -268), (40, -281), (22, -281),
        ]
        plotPoly(points, True, pencolor=(0.04, 0.03, 0.04),
                 fillcolor=(0.98, 0.98, 0.98), width=4)

        # 裤子上的黑条
        points = [
            (-171, -137), (-137, -143), (-138, -154), (-171, -148),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.01, 0.0),
                 fillcolor=(0.0, 0.01, 0.0), width=0)

        # 裤子上的黑条
        points = [
            (-120, -148), (-85, -155), (-87, -165), (-121, -158),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.01, 0.0),
                 fillcolor=(0.0, 0.01, 0.0), width=0)

        # 裤子上的黑条
        points = [
            (-63, -158), (-64, -170), (-26, -177), (-25, -167),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.01, 0.0),
                 fillcolor=(0.0, 0.01, 0.0), width=0)

        # 裤子上的黑条
        points = [
            (-2, -172), (-2, -183), (47, -194), (47, -181),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.01, 0.0),
                 fillcolor=(0.0, 0.01, 0.0), width=0)

        # 裤子上的黑条
        points = [
            (91, -181), (91, -194), (118, -186), (118, -175),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.01, 0.0),
                 fillcolor=(0.0, 0.01, 0.0), width=0)

        # 领带
        points = [
            (-130, -109), (-120, -121), (-117, -126), (-110, -121), (-103, -116),
            (-95, -112),
        ]
        plotLine(points, pencolor=(0.0, 0.01, 0.0), width=3)

        # 领带
        points = [
            (-47, -125), (-32, -144), (-18, -140), (-5, -134),
        ]
        plotLine(points, pencolor=(0.0, 0.01, 0.0), width=3)

        # 领带
        points = [
            (-92, -111), (-90, -110), (-87, -111), (-81, -113), (-77, -116),
            (-74, -119), (-69, -120), (-63, -121), (-57, -123), (-55, -124),
            (-58, -128), (-61, -132), (-64, -134), (-67, -137), (-75, -137),
            (-78, -135), (-83, -132), (-85, -126), (-88, -120), (-89, -117),
            (-91, -115),
        ]
        plotPoly(points, True, pencolor=(0.98, 0.25, 0.17),
                 fillcolor=(0.98, 0.25, 0.17), width=0)

        # 领带
        points = [
            (-94, -112), (-92, -114), (-89, -120), (-87, -125), (-84, -131),
            (-82, -134), (-79, -136), (-73, -137), (-67, -137), (-64, -136),
            (-60, -131), (-56, -127), (-53, -124),
        ]
        plotLine(points, pencolor=(0.0, 0.0, 0.02), width=3)

        # 领带
        points = [
            (-82, -135), (-82, -139), (-84, -144), (-85, -149), (-86, -153),
            (-88, -157), (-90, -161), (-93, -166), (-94, -169), (-94, -170),
            (-92, -173), (-86, -180), (-81, -186), (-77, -190), (-73, -187),
            (-68, -184), (-62, -180), (-57, -176), (-58, -175), (-59, -168),
            (-61, -159), (-63, -149), (-65, -140), (-66, -137), (-69, -137),
            (-73, -137), (-75, -137), (-78, -136), (-80, -135),
        ]
        plotPoly(points, True, pencolor=(0.0, 0.0, 0.02),
                 fillcolor=(0.98, 0.25, 0.17), width=3)

        # 隐藏海龟
        turtle.hideturtle()
        turtle.done()
    elif pppppp == 8:
        # -*- codeing = utf-8 -*-
        # @Time : 2022/10/17 12:09
        # @Author : 可乐不加糖
        # @File : duolaAmeng.py
        # @Software: PyCharm
        import turtle  # 导入turtle库
        import time


        # 实现清屏
        def clear():
            turtle.speed(0)
            turtle.penup()
            turtle.home()
            turtle.pensize(800)
            turtle.pencolor("white")
            turtle.pendown()
            turtle.forward(400)
            turtle.back(800)


        # 先画哆啦A梦的外部轮廓
        def duo_head():
            turtle.setup(1800, 1800, 0, 0)  # 设置窗口大小和位置
            turtle.speed(10)
            turtle.penup()  # 抬起画笔
            turtle.goto(0, 100)  # 将画笔移到指定位置
            turtle.circle(150, 45)
            turtle.pensize(1)
            turtle.pencolor("black")
            turtle.pendown()  # 放下画笔
            turtle.begin_fill()
            turtle.fillcolor("#38B8F7")
            turtle.circle(150, 270)
            turtle.penup()
            turtle.circle(150, 340)
            turtle.seth(150)
            turtle.pendown()
            turtle.forward(30)
            turtle.left(80)
            turtle.circle(-30)
            turtle.penup()
            turtle.circle(-30, 60)
            turtle.left(130)
            turtle.pendown()
            turtle.forward(120)
            turtle.seth(90)
            turtle.circle(-300, 5)
            turtle.penup()
            turtle.back(20)
            turtle.pendown()
            turtle.seth(-90)
            turtle.circle(800, 8)
            turtle.right(60)
            turtle.circle(20, 120)
            turtle.seth(0)
            turtle.forward(110)
            turtle.seth(60)
            turtle.circle(-20, 120)
            turtle.seth(0)
            turtle.fd(110)
            turtle.seth(40)
            turtle.circle(20, 120)
            turtle.seth(90)
            turtle.circle(700, 10)
            turtle.circle(800, 2)
            turtle.penup()
            turtle.back(30)
            turtle.seth(-30)
            turtle.pendown()
            turtle.forward(5)
            turtle.circle(500, 5)
            turtle.circle(20, 180)
            turtle.forward(80)
            turtle.end_fill()


        # 画哆啦A梦的手
        def duo_hand():
            turtle.back(80)
            turtle.seth(30)
            turtle.circle(-30, 290)
            turtle.penup()
            turtle.goto(-155, 225)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("white")
            turtle.circle(30)
            turtle.end_fill()


        # 画哆啦A梦的脚
        def duo_feet():
            turtle.penup()
            turtle.goto(-129, -45)
            turtle.pendown()
            turtle.left(90)
            turtle.forward(10)
            turtle.circle(15, 150)
            turtle.circle(200, 30)
            turtle.circle(100, 17)
            turtle.circle(15, 130)

            turtle.penup()
            turtle.goto(25, -50)
            turtle.pendown()
            turtle.left(50)
            turtle.circle(18, 130)
            turtle.circle(100, 18)
            turtle.circle(200, 25)
            turtle.circle(18, 140)


        # 画哆啦A梦的脸
        def duo_face():
            turtle.penup()
            turtle.goto(-70, 340)
            turtle.pensize(1)
            turtle.left(30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("white")
            turtle.circle(50, 80)
            turtle.penup()
            turtle.goto(-100, 300)
            turtle.seth(170)
            turtle.pendown()
            turtle.circle(30, 220)
            turtle.penup()
            turtle.circle(30, 310)
            turtle.pendown()
            turtle.right(70)
            turtle.circle(150, 40)
            turtle.seth(0)
            turtle.forward(170)
            turtle.seth(60)
            turtle.circle(150, 40)
            turtle.penup()
            turtle.goto(55, 250)
            turtle.seth(-60)
            turtle.circle(30, 60)
            turtle.pendown()
            turtle.circle(30, 230)
            turtle.penup()
            turtle.circle(30, 280)
            turtle.seth(100)
            turtle.pendown()
            turtle.circle(80, 30)
            turtle.circle(50, 40)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-30, 380)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("white")
            turtle.circle(30)

            turtle.penup()
            turtle.goto(30, 380)
            turtle.pendown()
            turtle.circle(30)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(10, 360)
            turtle.pensize(8)
            turtle.pendown()
            turtle.circle(8)

            turtle.penup()
            turtle.goto(-20, 360)
            turtle.pensize(8)
            turtle.pendown()
            turtle.circle(8)

            turtle.penup()
            turtle.goto(-95, 242)
            turtle.seth(10)
            turtle.pensize(1)
            turtle.pendown()
            turtle.circle(500, 5)
            turtle.circle(-60, 20)
            turtle.circle(200, 10)
            turtle.circle(-60, 20)
            turtle.circle(500, 5)
            turtle.circle(500, 3)
            turtle.penup()
            turtle.goto(-9, 300)
            turtle.pensize(1)
            turtle.pendown()
            turtle.circle(16)
            turtle.seth(-90)
            turtle.forward(50)
            turtle.penup()
            turtle.goto(-35, 300)
            turtle.seth(160)
            turtle.pendown()
            turtle.forward(60)

            turtle.penup()
            turtle.goto(-35, 290)
            turtle.seth(180)
            turtle.pendown()
            turtle.forward(80)

            turtle.penup()
            turtle.goto(-35, 280)
            turtle.seth(200)
            turtle.pendown()
            turtle.forward(90)

            turtle.penup()
            turtle.goto(20, 300)
            turtle.seth(20)
            turtle.pendown()
            turtle.forward(60)

            turtle.penup()
            turtle.goto(20, 290)
            turtle.seth(0)
            turtle.pendown()
            turtle.forward(80)

            turtle.penup()
            turtle.goto(20, 280)
            turtle.seth(-20)
            turtle.pendown()
            turtle.forward(90)

            turtle.penup()
            turtle.goto(-90, 245)
            turtle.seth(-70)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("red")
            turtle.circle(200, 20)
            turtle.seth(-30)
            turtle.circle(100, 50)
            turtle.seth(40)
            turtle.circle(200, 24)
            turtle.seth(165)
            turtle.circle(500, 10)
            turtle.end_fill()

            turtle.penup()
            turtle.goto(-50, 185)
            turtle.seth(90)
            turtle.pensize(1)
            turtle.pendown()
            turtle.circle(-40, 190)


        # 画哆啦A梦的肚子
        def duo_du():
            turtle.penup()
            turtle.goto(-50, -10)
            turtle.seth(160)
            turtle.pensize(1)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("white")
            turtle.circle(-80, 110)
            turtle.circle(-90, 110)
            turtle.circle(-80, 110)
            turtle.circle(-110, 55)
            turtle.end_fill()

            turtle.penup()
            turtle.goto(-70, 70)
            turtle.seth(-10)
            turtle.pensize(1)
            turtle.pendown()
            for i in range(16):
                turtle.fd(4)
                turtle.left(0.5)
            turtle.seth(10)
            for i in range(16):
                turtle.fd(4)
                turtle.left(0.5)
            turtle.right(120)
            turtle.circle(-70, 90)
            turtle.right(10)
            turtle.circle(-70, 50)


        # 画哆啦A梦的铃铛
        def duo_lingdang():
            turtle.penup()
            turtle.goto(-115, 150)
            turtle.seth(0)
            turtle.pensize(1)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("red")
            turtle.forward(230)
            turtle.right(10)
            turtle.circle(-5, 170)
            turtle.forward(230)
            turtle.circle(-5, 170)
            turtle.end_fill()

            turtle.penup()
            turtle.goto(-20, 140)
            turtle.pensize(1)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("yellow")
            turtle.left(10)
            turtle.circle(-20)
            turtle.end_fill()

            turtle.penup()
            turtle.goto(-30, 130)
            turtle.pensize(1)
            turtle.seth(0)
            turtle.pendown()
            turtle.forward(34)
            turtle.penup()
            turtle.goto(5, 125)
            turtle.pensize(1)
            turtle.seth(0)
            turtle.pendown()
            turtle.back(37)

            turtle.penup()
            turtle.goto(-12, 115)
            turtle.pensize(3)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("black")
            turtle.circle(4)
            turtle.end_fill()
            turtle.seth(-90)
            turtle.pensize(1)
            turtle.forward(15)


        # 显示文字
        def draw_1():
            turtle.setup(1800, 1800, 0, 0)
            turtle.penup()
            turtle.hideturtle()  # 隐藏箭头显示
            turtle.goto(-250, -250)
            turtle.color('black')
            write = turtle.write('哆啦A梦', font=('wisdom', 120, 'normal'))
            time.sleep(2)


        # clear()
        duo_head()
        duo_hand()
        duo_feet()
        duo_face()
        duo_du()
        duo_lingdang()
        draw_1()
        turtle.hideturtle()
        turtle.done()
    elif pppppp == 9:
        import turtle as t

        t.pensize(4)  # 设置画笔的大小
        t.colormode(255)  # 设置GBK颜色范围为0-255
        t.color((255, 155, 192), "pink")  # 设置画笔颜色和填充颜色(pink)
        t.setup(840, 500)  # 设置主窗口的大小为840*500
        t.speed(10)  # 设置画笔速度为10
        # 鼻子
        t.pu()  # 提笔
        t.goto(-100, 100)  # 画笔前往坐标(-100,100)
        t.pd()  # 下笔
        t.seth(-30)  # 笔的角度为-30°
        t.begin_fill()  # 外形填充的开始标志
        a = 0.4
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a = a + 0.08
                t.lt(3)  # 向左转3度
                t.fd(a)  # 向前走a的步长
            else:
                a = a - 0.08
                t.lt(3)
                t.fd(a)
        t.end_fill()  # 依据轮廓填充
        t.pu()  # 提笔
        t.seth(90)  # 笔的角度为90度
        t.fd(25)  # 向前移动25
        t.seth(0)  # 转换画笔的角度为0
        t.fd(10)
        t.pd()
        t.pencolor(255, 155, 192)  # 设置画笔颜色
        t.seth(10)
        t.begin_fill()
        t.circle(5)  # 画一个半径为5的圆
        t.color(160, 82, 45)  # 设置画笔和填充颜色
        t.end_fill()
        t.pu()
        t.seth(0)
        t.fd(20)
        t.pd()
        t.pencolor(255, 155, 192)
        t.seth(10)
        t.begin_fill()
        t.circle(5)
        t.color(160, 82, 45)
        t.end_fill()
        # 头
        t.color((255, 155, 192), "pink")
        t.pu()
        t.seth(90)
        t.fd(41)
        t.seth(0)
        t.fd(0)
        t.pd()
        t.begin_fill()
        t.seth(180)
        t.circle(300, -30)  # 顺时针画一个半径为300,圆心角为30°的园
        t.circle(100, -60)
        t.circle(80, -100)
        t.circle(150, -20)
        t.circle(60, -95)
        t.seth(161)
        t.circle(-300, 15)
        t.pu()
        t.goto(-100, 100)
        t.pd()
        t.seth(-30)
        a = 0.4
        for i in range(60):
            if 0 <= i < 30 or 60 <= i < 90:
                a = a + 0.08
                t.lt(3)  # 向左转3度
                t.fd(a)  # 向前走a的步长
            else:
                a = a - 0.08
                t.lt(3)
                t.fd(a)
        t.end_fill()
        # 耳朵
        t.color((255, 155, 192), "pink")
        t.pu()
        t.seth(90)
        t.fd(-7)
        t.seth(0)
        t.fd(70)
        t.pd()
        t.begin_fill()
        t.seth(100)
        t.circle(-50, 50)
        t.circle(-10, 120)
        t.circle(-50, 54)
        t.end_fill()
        t.pu()
        t.seth(90)
        t.fd(-12)
        t.seth(0)
        t.fd(30)
        t.pd()
        t.begin_fill()
        t.seth(100)
        t.circle(-50, 50)
        t.circle(-10, 120)
        t.circle(-50, 56)
        t.end_fill()
        # 眼睛
        t.color((255, 155, 192), "white")
        t.pu()
        t.seth(90)
        t.fd(-20)
        t.seth(0)
        t.fd(-95)
        t.pd()
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.color("black")
        t.pu()
        t.seth(90)
        t.fd(12)
        t.seth(0)
        t.fd(-3)
        t.pd()
        t.begin_fill()
        t.circle(3)
        t.end_fill()
        t.color((255, 155, 192), "white")
        t.pu()
        t.seth(90)
        t.fd(-25)
        t.seth(0)
        t.fd(40)
        t.pd()
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.color("black")
        t.pu()
        t.seth(90)
        t.fd(12)
        t.seth(0)
        t.fd(-3)
        t.pd()
        t.begin_fill()
        t.circle(3)
        t.end_fill()
        # 腮
        t.color((255, 155, 192))
        t.pu()
        t.seth(90)
        t.fd(-95)
        t.seth(0)
        t.fd(65)
        t.pd()
        t.begin_fill()
        t.circle(30)
        t.end_fill()
        # 嘴
        t.color(239, 69, 19)
        t.pu()
        t.seth(90)
        t.fd(15)
        t.seth(0)
        t.fd(-100)
        t.pd()
        t.seth(-80)
        t.circle(30, 40)
        t.circle(40, 80)
        # 身体
        t.color("red", (255, 99, 71))
        t.pu()
        t.seth(90)
        t.fd(-20)
        t.seth(0)
        t.fd(-78)
        t.pd()
        t.begin_fill()
        t.seth(-130)
        t.circle(100, 10)
        t.circle(300, 30)
        t.seth(0)
        t.fd(230)
        t.seth(90)
        t.circle(300, 30)
        t.circle(100, 3)
        t.color((255, 155, 192), (255, 100, 100))
        t.seth(-135)
        t.circle(-80, 63)
        t.circle(-150, 24)
        t.end_fill()
        # 手
        t.color((255, 155, 192))
        t.pu()
        t.seth(90)
        t.fd(-40)
        t.seth(0)
        t.fd(-27)
        t.pd()
        t.seth(-160)
        t.circle(300, 15)
        t.pu()
        t.seth(90)
        t.fd(15)
        t.seth(0)
        t.fd(0)
        t.pd()
        t.seth(-10)
        t.circle(-20, 90)
        t.pu()
        t.seth(90)
        t.fd(30)
        t.seth(0)
        t.fd(237)
        t.pd()
        t.seth(-20)
        t.circle(-300, 15)
        t.pu()
        t.seth(90)
        t.fd(20)
        t.seth(0)
        t.fd(0)
        t.pd()
        t.seth(-170)
        t.circle(20, 90)
        # 脚
        t.pensize(10)
        t.color((240, 128, 128))
        t.pu()
        t.seth(90)
        t.fd(-75)
        t.seth(0)
        t.fd(-180)
        t.pd()
        t.seth(-90)
        t.fd(40)
        t.seth(-180)
        t.color("black")
        t.pensize(15)
        t.fd(20)
        t.pensize(10)
        t.color((240, 128, 128))
        t.pu()
        t.seth(90)
        t.fd(40)
        t.seth(0)
        t.fd(90)
        t.pd()
        t.seth(-90)
        t.fd(40)
        t.seth(-180)
        t.color("black")
        t.pensize(15)
        t.fd(20)
        # 尾巴
        t.pensize(4)
        t.color((255, 155, 192))
        t.pu()
        t.seth(90)
        t.fd(70)
        t.seth(0)
        t.fd(95)
        t.pd()
        t.seth(0)
        t.circle(70, 20)
        t.circle(10, 330)
        t.circle(70, 30)
        t.done()
    elif pppppp == 10:
        import turtle as t

        '''
        t.pu()  提起画笔
        t.pd()  移动时绘制图形，缺省时也为绘制
        t.seth  设置当前朝向为angle角度
        t.begin_fill()  准备开始填充图形
        t.color      同时设置pencolor=color1, fillcolor=color2
        t.goto      设置笔的坐标
        t.circle(70,20) 半径 度数
        15,124,215  乔治裤子颜色外面
        66,163,242  乔治裤子颜色里面

        134  196  247  天空的颜色
        123,245,95 草地的颜色
        253,6,6  鞋子外面
        253,70,70  鞋子里面
        130,119,100 泥坑


        '''
        r_a = 0.8
        wight = 1100
        height = 700
        # t.pensize(4)
        t.hideturtle()
        t.colormode(255)
        t.color((255, 155, 192), "pink")
        t.setup(wight, height)
        t.speed(10)


        def move_pen(x, y):
            t.pu()
            t.goto(x - wight / 2 + 50, y - height / 2 + 50)
            t.pd()


        def pen_set(size, r1, g1, b1, r2=0, g2=0, b2=0):
            t.pensize(size)
            t.color((r1, g1, b1), (r2, g2, b2))


        def draw_grid():
            pen_set(1, 0, 0, 0, 0, 0, 0)
            for i in range(20):
                move_pen(0 + i * 50, 0)
                t.seth(90)
                t.fd(600)
            for i in range(12):
                move_pen(0, 0 + i * 50)
                t.seth(0)
                t.fd(1000)


        def draw_bg():
            # 画草地

            move_pen(0, 350)
            pen_set(4, 123, 245, 95, 123, 245, 95)
            t.begin_fill()
            t.seth(-90)
            t.fd(350)
            t.seth(0)
            t.fd(1000)
            t.seth(90)
            t.fd(350)
            t.end_fill()
            # 画天空
            move_pen(0, 350)
            pen_set(4, 134, 196, 247, 134, 196, 247)
            t.begin_fill()
            t.seth(90)
            t.fd(250)
            t.seth(0)
            t.fd(1000)
            t.seth(-90)
            t.fd(250)
            a = -180 + r_a
            for i in range(50):
                a = a - r_a / 50
                t.seth(a)
                t.fd(500 / 50)
            a = 180
            for i in range(50):
                a = a - r_a / 50
                t.seth(a)
                t.fd(500 / 50)
            t.end_fill()


        def draw_mud_pit():
            # 画泥坑
            pen_set(5, 130, 119, 100, 130, 119, 100)
            move_pen(350, 150)
            t.begin_fill()
            t.seth(-180)
            t.circle(50, 125)
            t.seth(-20)
            t.circle(350, 60)
            t.seth(20)
            t.circle(50, 30)
            t.seth(10)
            t.circle(50, 30)
            t.seth(0)
            t.circle(50, 30)
            t.seth(40)
            t.circle(50, 90)
            t.seth(170)
            t.circle(500, 45)
            t.end_fill()


        def draw_shoes():
            pen_set(3, 253, 6, 6, 253, 70, 70)
            move_pen(400, 100)
            t.begin_fill()
            t.seth(0)
            t.fd(50)
            t.seth(87)
            t.fd(50)
            t.seth(180)
            t.fd(25)
            t.seth(-93)
            t.fd(20)
            t.seth(-180)
            t.fd(25)
            t.seth(-120)
            t.circle(45, 38)
            t.end_fill()
            move_pen(470, 100)
            t.begin_fill()
            t.seth(0)
            t.fd(50)
            t.seth(87)
            t.fd(50)
            t.seth(180)
            t.fd(25)
            t.seth(-93)
            t.fd(20)
            t.seth(-180)
            t.fd(25)
            t.seth(-120)
            t.circle(45, 38)
            t.end_fill()


        def draw_leg():
            pen_set(6, 255, 155, 192, 255, 155, 192)
            move_pen(440, 140)
            t.seth(90)
            t.fd(20)
            move_pen(510, 140)
            t.seth(90)
            t.fd(20)


        def draw_trousers():
            move_pen(400, 300)
            pen_set(6, 15, 124, 215, 66, 163, 242)
            t.begin_fill()
            d_a = 100
            a = -130
            for i in range(60):
                a = a + 2
                t.seth(a)
                t.fd(3)
            for i in range(14):
                a = a + 0.02
                t.seth(a)
                t.fd(2)
            a = 0 - a
            for i in range(14):
                a = a + 0.02
                t.seth(a)
                t.fd(2)
            for i in range(60):
                a = a + 2.2
                t.seth(a)
                t.fd(3)
            t.end_fill()


        def draw_tile():
            move_pen(550, 177)
            pen_set(6, 255, 155, 192, 255, 155, 192)
            a = -60
            for i in range(25):
                a = a + 4
                t.seth(a)
                t.fd(1)
            t.circle(5)
            a = -a
            for i in range(30):
                a = a + 4
                t.seth(a)
                t.fd(1)


        def draw_hands():
            move_pen(550, 250)
            pen_set(6, 255, 155, 192, 255, 155, 192)
            t.seth(20)
            t.fd(70)
            move_pen(600, 270)
            t.seth(60)
            t.fd(20)
            move_pen(600, 270)
            t.seth(-20)
            t.fd(20)

            move_pen(380, 250)
            t.seth(160)
            t.fd(50)
            move_pen(350, 260)
            t.seth(100)
            t.fd(20)
            move_pen(350, 260)
            t.seth(-140)
            t.fd(20)


        def draw_face():
            move_pen(400, 360)
            pen_set(4, 255, 155, 192, 255, 196, 218)
            t.begin_fill()
            a = -120
            for i in range(20):
                a = a + 2.5
                t.seth(a)
                t.fd(2.2)
            for i in range(130):
                a = a + 1.3
                t.seth(a)
                t.fd(1.8)
            for i in range(35):
                a = a + 1.4
                t.seth(a)
                t.fd(2)
            for i in range(50):
                a = a + 0.35
                t.seth(a)
                t.fd(2)
            for i in range(50):
                a = a + 0.2
                t.seth(a)
                t.fd(2)
            n = 0.4
            for i in range(180):
                if 0 <= i < 30 or 60 <= i < 90 or 120 <= i < 150:
                    n = n + 0.08
                    t.lt(3)  # 向左转3度
                    t.fd(n)  # 向前走a的步长
                else:
                    n = n - 0.08
                    t.lt(3)
                    t.fd(n)
            a = -50
            for i in range(20):
                a = a + 2.8
                t.seth(a)
                t.fd(5)
            t.end_fill()


        def draw_other():
            move_pen(310, 440)
            pen_set(6, 255, 145, 192, 255, 145, 192)
            t.begin_fill()
            t.circle(3)
            t.end_fill()
            move_pen(330, 430)
            t.begin_fill()
            t.circle(3)
            t.end_fill()

            pen_set(6, 255, 145, 192, 255, 255, 255)
            move_pen(410, 425)
            t.begin_fill()
            t.circle(10)
            t.end_fill()
            move_pen(460, 395)
            t.begin_fill()
            t.circle(10)
            t.end_fill()

            pen_set(6, 0, 0, 0, 0, 0, 0)
            move_pen(405, 429)
            t.begin_fill()
            t.circle(3)
            t.end_fill()
            move_pen(455, 399)
            t.begin_fill()
            t.circle(3)
            t.end_fill()

            move_pen(510, 310)
            pen_set(6, 255, 155, 192, 255, 155, 192)
            t.begin_fill()
            t.circle(25)
            t.end_fill()

            move_pen(410, 340)
            pen_set(6, 255, 145, 192, 255, 145, 192)
            a = -80
            for i in range(20):
                a = a + 6
                t.seth(a)
                t.fd(3)
            move_pen(430, 445)
            pen_set(4, 255, 155, 192, 255, 196, 218)
            t.begin_fill()
            a = 120
            for i in range(40):
                a = a - 2
                t.seth(a)
                t.fd(1.2)
            a = -a
            for i in range(45):
                a = a - 2
                t.seth(a)
                t.fd(1.2)
            t.end_fill()
            move_pen(480, 430)
            t.begin_fill()
            a = 70
            for i in range(40):
                a = a - 1.5
                t.seth(a)
                t.fd(1.5)
            a = -80
            for i in range(45):
                a = a - 1.5
                t.seth(a)
                t.fd(1.5)
            t.end_fill()


        draw_bg()
        draw_mud_pit()
        # draw_grid()
        draw_leg()
        draw_shoes()
        draw_trousers()
        draw_tile()
        draw_hands()
        draw_face()
        draw_other()
        t.mainloop()
    elif pppppp == 11:
        import os
        from tkinter import *
        from tkinter import simpledialog
        from tkinter import messagebox


        def in1():
            a = int(radio1.get())
            global r1
            global ret
            global s1
            if a == 1:
                ret = simpledialog.askstring(title='输入', prompt='请输入ico图标绝对路径或相对路径')
                r1 = " -i " + str(ret)
                s1 = "是。" + " ico路径：" + ret
            else:
                r1 = ""
                s1 = "否"


        def in2():
            a = int(radio2.get())
            global r2
            global s2
            if a == 1:
                r2 = " -F"
                s2 = "是"
            else:
                r2 = ""
                s2 = "否"


        def in3():
            a = int(radio3.get())
            global r3
            global s3
            if a == 2:
                r3 = " -w"
                s3 = "否"
            else:
                r3 = ""
                s3 = "是"


        def ok():
            r4 = e1.get()
            con = "pyinstaller" + r2 + r3 + r1 + " " + r4
            os.system(con)


        def seeall():
            r4 = e1.get()
            nr = "py文件路径：" + r4 + "\n" + "是否添加ico图标：" + s1 + "\n" + "是否生成一整个exe文件：" + s2 + "\n" + "是否允许显示控制台窗口：" + s3
            re = messagebox.askquestion(title='确认框 by sarxc', message=nr)
            if re == "yes":
                st = ok()
                messagebox.showinfo(title='完成', message="完成")
            else:
                messagebox.showinfo(title='取消', message="已取消")


        window = Tk()
        window.geometry('250x350')
        window.title('py转exe by sraxc')
        l1 = Label(window, text="py文件绝对路径或相对路径")
        l1.pack()

        e1 = Entry(window)
        e1.pack()

        l2 = Label(window, text="是否添加ico图标")
        l2.pack()

        radio1 = IntVar()
        R1 = Radiobutton(window, text="是", variable=radio1, value=1, command=in1)
        R1.pack(anchor=W)
        R2 = Radiobutton(window, text="否", variable=radio1, value=2, command=in1)
        R2.pack(anchor=W)

        l3 = Label(window, text="是否生成一整个exe文件？[建议选是]")
        l3.pack()

        radio2 = IntVar()
        R1 = Radiobutton(window, text="是[建议]", variable=radio2, value=1, command=in2)
        R1.pack(anchor=W)
        R2 = Radiobutton(window, text="否", variable=radio2, value=2, command=in2)
        R2.pack(anchor=W)

        l4 = Label(window, text="是否允许显示控制台窗口？")
        l4.pack()

        l5 = Label(window, text="（如您是直接在命令行中运行建议选是）")
        l5.pack()

        radio3 = IntVar()
        R1 = Radiobutton(window, text="是", variable=radio3, value=1, command=in3)
        R1.pack(anchor=W)
        R2 = Radiobutton(window, text="否", variable=radio3, value=2, command=in3)
        R2.pack(anchor=W)

        button = Button(window, text='开始', command=seeall)
        button.pack()

        window.mainloop()
    elif pppppp == 12:
        from random import choice
        from turtle import *

        from freegames import floor, vector

        state = {'score': 0}
        path = Turtle(visible=False)
        writer = Turtle(visible=False)
        aim = vector(5, 0)
        pacman = vector(-40, -80)
        ghosts = [
            [vector(-180, 160), vector(5, 0)],
            [vector(-180, -160), vector(0, 5)],
            [vector(100, 160), vector(0, -5)],
            [vector(100, -160), vector(-5, 0)],
        ]
        # fmt: off
        tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
            0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]


        # fmt: on

        def square(x, y):
            """Draw square using path at (x, y)."""
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()

            for count in range(4):
                path.forward(20)
                path.left(90)

            path.end_fill()


        def offset(point):
            """Return offset of point in tiles."""
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index


        def valid(point):
            """Return True if point is valid in tiles."""
            index = offset(point)

            if tiles[index] == 0:
                return False

            index = offset(point + 19)

            if tiles[index] == 0:
                return False

            return point.x % 20 == 0 or point.y % 20 == 0


        def world():
            """Draw world using path."""
            bgcolor('black')
            path.color('blue')

            for index in range(len(tiles)):
                tile = tiles[index]

                if tile > 0:
                    x = (index % 20) * 20 - 200
                    y = 180 - (index // 20) * 20
                    square(x, y)

                    if tile == 1:
                        path.up()
                        path.goto(x + 10, y + 10)
                        path.dot(2, 'white')


        def move():
            """Move pacman and all ghosts."""
            writer.undo()
            writer.write(state['score'])

            clear()

            if valid(pacman + aim):
                pacman.move(aim)

            index = offset(pacman)

            if tiles[index] == 1:
                tiles[index] = 2
                state['score'] += 1
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)

            up()
            goto(pacman.x + 10, pacman.y + 10)
            dot(20, 'yellow')

            for point, course in ghosts:
                if valid(point + course):
                    point.move(course)
                else:
                    options = [
                        vector(5, 0),
                        vector(-5, 0),
                        vector(0, 5),
                        vector(0, -5),
                    ]
                    plan = choice(options)
                    course.x = plan.x
                    course.y = plan.y

                up()
                goto(point.x + 10, point.y + 10)
                dot(20, 'red')

            update()

            for point, course in ghosts:
                if abs(pacman - point) < 20:
                    return

            ontimer(move, 100)


        def change(x, y):
            """Change pacman aim if valid."""
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y


        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        writer.goto(160, 160)
        writer.color('white')
        writer.write(state['score'])
        listen()
        onkey(lambda: change(5, 0), 'Right')
        onkey(lambda: change(-5, 0), 'Left')
        onkey(lambda: change(0, 5), 'Up')
        onkey(lambda: change(0, -5), 'Down')
        world()
        move()
        done()
    elif pppppp == 13:
        print('👉 游戏规则：单击行可放置光盘。第一个垂直、水平或对角连接四张光盘的玩家获胜。')
        from turtle import *

        from freegames import line

        turns = {'red': 'yellow', 'yellow': 'red'}
        state = {'player': 'yellow', 'rows': [0] * 8}


        def grid():
            """Draw Connect Four grid."""
            bgcolor('light blue')

            for x in range(-150, 200, 50):
                line(x, -200, x, 200)

            for x in range(-175, 200, 50):
                for y in range(-175, 200, 50):
                    up()
                    goto(x, y)
                    dot(40, 'white')

            update()


        def tap(x, y):
            """Draw red or yellow circle in tapped row."""
            player = state['player']
            rows = state['rows']

            row = int((x + 200) // 50)
            count = rows[row]

            x = ((x + 200) // 50) * 50 - 200 + 25
            y = count * 50 - 200 + 25

            up()
            goto(x, y)
            dot(40, player)
            update()

            rows[row] = count + 1
            state['player'] = turns[player]


        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        grid()
        onscreenclick(tap)
        done()
    elif pppppp == 14:
        from turtle import *

        from freegames import line


        def grid():
            """Draw tic-tac-toe grid."""
            line(-67, 200, -67, -200)
            line(67, 200, 67, -200)
            line(-200, -67, 200, -67)
            line(-200, 67, 200, 67)


        def drawx(x, y):
            """Draw X player."""
            line(x, y, x + 133, y + 133)
            line(x, y + 133, x + 133, y)


        def drawo(x, y):
            """Draw O player."""
            up()
            goto(x + 67, y + 5)
            down()
            circle(62)


        def floor(value):
            """Round value down to grid with square size 133."""
            return ((value + 200) // 133) * 133 - 200


        state = {'player': 0}
        players = [drawx, drawo]


        def tap(x, y):
            """Draw X or O in tapped square."""
            x = floor(x)
            y = floor(y)
            player = state['player']
            draw = players[player]
            draw(x, y)
            update()
            state['player'] = not player


        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        grid()
        update()
        onscreenclick(tap)
        done()
    elif pppppp == 15:
        from random import *
        from turtle import *

        from freegames import floor, vector

        tiles = {}
        neighbors = [
            vector(100, 0),
            vector(-100, 0),
            vector(0, 100),
            vector(0, -100),
        ]


        def load():
            """Load tiles and scramble."""
            count = 1

            for y in range(-200, 200, 100):
                for x in range(-200, 200, 100):
                    mark = vector(x, y)
                    tiles[mark] = count
                    count += 1

            tiles[mark] = None

            for count in range(1000):
                neighbor = choice(neighbors)
                spot = mark + neighbor

                if spot in tiles:
                    number = tiles[spot]
                    tiles[spot] = None
                    tiles[mark] = number
                    mark = spot


        def square(mark, number):
            """Draw white square with black outline and number."""
            up()
            goto(mark.x, mark.y)
            down()

            color('black', 'white')
            begin_fill()
            for count in range(4):
                forward(99)
                left(90)
            end_fill()

            if number is None:
                return
            elif number < 10:
                forward(20)

            write(number, font=('Arial', 60, 'normal'))


        def tap(x, y):
            """Swap tile and empty square."""
            x = floor(x, 100)
            y = floor(y, 100)
            mark = vector(x, y)

            for neighbor in neighbors:
                spot = mark + neighbor

                if spot in tiles and tiles[spot] is None:
                    number = tiles[mark]
                    tiles[spot] = number
                    square(spot, number)
                    tiles[mark] = None
                    square(mark, None)


        def draw():
            """Draw all tiles."""
            for mark in tiles:
                square(mark, tiles[mark])
            update()


        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        load()
        draw()
        onscreenclick(tap)
        done()
    elif pppppp == 16:
        # coding=gbk
        """
        作者：小树叶（闵熙昊）
        时间：2024/3/21
        """
        messagebox.showinfo('提示', '制作中......')
        continue
        import requests
        import pyttsx3

        print('请输入你想说的：')
        while True:
            a = input()
            if a == 'r':
                break
            url = 'https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s' % a
            te = requests.get(url).json()
            data = te['data']['info']['text']
            print(data)
            ini = pyttsx3.init()
            shuo = ini.say(data)
            ini.runAndWait()
    elif pppppp == 17:

        # Step 1 import set up turtle and Screen
        import turtle
        import random

        s = turtle.Screen()
        s.title("Pong")
        s.bgcolor("black")
        s.setup(width=600, height=400)

        # Step 2 Create ball
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("circle")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 4
        ball.dy = 4

        # Step 3 Create AI paddle
        ai = turtle.Turtle()
        ai.speed(0)
        ai.shape("square")
        ai.color("white")
        ai.penup()
        ai.goto(-250, 0)
        ai.shapesize(stretch_wid=5, stretch_len=1)

        # Step 4 Create a paddle For You
        you = turtle.Turtle()
        you.speed(0)
        you.shape("square")
        you.color("white")
        you.penup()
        you.goto(250, 0)
        you.shapesize(stretch_wid=5, stretch_len=1)


        # Step 5 Create Function to move AI paddle
        def move_ai_paddle():
            y = ball.ycor()
            if y > 0:
                ai.sety(ai.ycor() + 2)
            else:
                ai.sety(ai.ycor() - 2)


        # Step 6 Create a Function to move the your paddle
        def paddle2_up():
            y = you.ycor()
            y += 20
            you.sety(y)


        def paddle2_down():
            y = you.ycor()
            y -= 20
            you.sety(y)


        # Your Paddle control it with key
        s.listen()
        s.onkeypress(paddle2_up, "Up")
        s.onkeypress(paddle2_down, "Down")

        # Step 7 Start the game with a while loop
        while True:
            s.update()

            # Move the ball
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            # Check for collisions with the walls
            if ball.ycor() > 190 or ball.ycor() < -190:
                ball.dy *= -1

            # Move the robot paddle towards the ball
            if ball.ycor() > ai.ycor():
                ai.sety(ai.ycor() + 4)
            elif ball.ycor() < ai.ycor():
                ai.sety(ai.ycor() - 4)

                # Check for end game conditions
            if ball.xcor() > 300:
                turtle.textinput("Game End", "You Loss Pong Game With AI!")
                break
            if ball.xcor() < -300:
                turtle.textinput("Game End", "You Win Pong Game With AI!")
                break

            # Check for collisions with the robot paddle
            if (ball.xcor() < -240 and ball.xcor() > -250) and (
                    ball.ycor() < ai.ycor() + 40 and ball.ycor() > ai.ycor() - 40):
                if random.random() < 0.9:  # 90% chance of collision
                    ball.dx *= -1

                # Check for collisions with the user paddle
            if (ball.xcor() > 240 and ball.xcor() < 250) and (
                    ball.ycor() < you.ycor() + 40 and ball.ycor() > you.ycor() - 40):
                ball.dx *= -1

        turtle.exitonclick()
    elif pppppp == 18:
        import turtle

        turtle.title('PythonBingDwenDwen')
        turtle.speed(100)  # 速度*

        # 左手
        turtle.penup()
        turtle.goto(177, 112)
        turtle.pencolor("lightgray")
        turtle.pensize(3)
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(80)
        turtle.circle(-45, 200)
        turtle.circle(-300, 23)
        turtle.end_fill()

        # 左手内
        turtle.penup()
        turtle.goto(182, 95)
        turtle.pencolor("black")
        turtle.pensize(1)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.setheading(95)
        turtle.pendown()
        turtle.circle(-37, 160)
        turtle.circle(-20, 50)
        turtle.circle(-200, 30)
        turtle.end_fill()
        # 轮廓
        # 头顶
        turtle.penup()
        turtle.goto(-73, 230)
        turtle.pencolor("lightgray")
        turtle.pensize(3)
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(20)
        turtle.circle(-250, 35)
        # 左耳
        turtle.setheading(50)
        turtle.circle(-42, 180)
        # 左侧
        turtle.setheading(-50)
        turtle.circle(-190, 30)
        turtle.circle(-320, 45)
        # 左腿
        turtle.circle(120, 30)
        turtle.circle(200, 12)
        turtle.circle(-18, 85)
        turtle.circle(-180, 23)
        turtle.circle(-20, 110)
        turtle.circle(15, 115)
        turtle.circle(100, 12)
        # 右腿
        turtle.circle(15, 120)
        turtle.circle(-15, 110)
        turtle.circle(-150, 30)
        turtle.circle(-15, 70)
        turtle.circle(-150, 10)
        turtle.circle(200, 35)
        turtle.circle(-150, 20)
        # 右手
        turtle.setheading(-120)
        turtle.circle(50, 30)
        turtle.circle(-35, 200)
        turtle.circle(-300, 23)
        # 右侧
        turtle.setheading(86)
        turtle.circle(-300, 26)
        # 右耳
        turtle.setheading(122)
        turtle.circle(-53, 160)
        turtle.end_fill()

        # 右耳内
        turtle.penup()
        turtle.goto(-130, 180)
        turtle.pencolor("black")
        turtle.pensize(1)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(120)
        turtle.circle(-28, 160)
        turtle.setheading(210)
        turtle.circle(150, 20)
        turtle.end_fill()

        # 左耳内
        turtle.penup()
        turtle.goto(90, 230)
        turtle.setheading(40)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(-30, 170)
        turtle.setheading(125)
        turtle.circle(150, 23)
        turtle.end_fill()

        # 右手内
        turtle.penup()
        turtle.goto(-180, -55)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.setheading(-120)
        turtle.pendown()
        turtle.circle(50, 30)
        turtle.circle(-27, 200)
        turtle.circle(-300, 20)
        turtle.setheading(-90)
        turtle.circle(300, 14)
        turtle.end_fill()

        # 左腿内
        turtle.penup()
        turtle.goto(108, -168)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(-115)
        turtle.circle(110, 15)
        turtle.circle(200, 10)
        turtle.circle(-18, 80)
        turtle.circle(-180, 13)
        turtle.circle(-20, 90)
        turtle.circle(15, 60)
        turtle.setheading(42)
        turtle.circle(-200, 29)
        turtle.end_fill()
        # 右腿内
        turtle.penup()
        turtle.goto(-38, -210)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(-155)
        turtle.circle(15, 100)
        turtle.circle(-10, 110)
        turtle.circle(-100, 30)
        turtle.circle(-15, 65)
        turtle.circle(-100, 10)
        turtle.circle(200, 15)
        turtle.setheading(-14)
        turtle.circle(-200, 27)
        turtle.end_fill()

        # 右眼
        # 眼圈
        turtle.penup()
        turtle.goto(-64, 120)
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(40)
        turtle.circle(-35, 152)
        turtle.circle(-100, 50)
        turtle.circle(-35, 130)
        turtle.circle(-100, 50)
        turtle.end_fill()
        # 眼珠
        turtle.penup()
        turtle.goto(-47, 55)
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(25, 360)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-45, 62)
        turtle.pencolor("darkslategray")
        turtle.fillcolor("darkslategray")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(19, 360)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-45, 68)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(10, 360)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-47, 86)
        turtle.pencolor("white")
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(5, 360)
        turtle.end_fill()

        # 左眼
        # 眼圈
        turtle.penup()
        turtle.goto(51, 82)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(120)
        turtle.circle(-32, 152)
        turtle.circle(-100, 55)
        turtle.circle(-25, 120)
        turtle.circle(-120, 45)
        turtle.end_fill()
        # 眼珠
        turtle.penup()
        turtle.goto(79, 60)
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(24, 360)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(79, 64)
        turtle.pencolor("darkslategray")
        turtle.fillcolor("darkslategray")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(19, 360)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(79, 70)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(10, 360)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(79, 88)
        turtle.pencolor("white")
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(5, 360)
        turtle.end_fill()

        # 鼻子
        turtle.penup()
        turtle.goto(37, 80)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(-8, 130)
        turtle.circle(-22, 100)
        turtle.circle(-8, 130)
        turtle.end_fill()

        # 嘴
        turtle.penup()
        turtle.goto(-15, 48)
        turtle.setheading(-36)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(60, 70)
        turtle.setheading(-132)
        turtle.circle(-45, 100)
        turtle.end_fill()

        # 彩虹圈
        turtle.penup()
        turtle.goto(-135, 120)
        turtle.pensize(5)
        turtle.pencolor("cyan")
        turtle.pendown()
        turtle.setheading(60)
        turtle.circle(-165, 150)
        turtle.circle(-130, 78)
        turtle.circle(-250, 30)
        turtle.circle(-138, 105)
        turtle.penup()
        turtle.goto(-131, 116)
        turtle.pencolor("slateblue")
        turtle.pendown()
        turtle.setheading(60)
        turtle.circle(-160, 144)
        turtle.circle(-120, 78)
        turtle.circle(-242, 30)
        turtle.circle(-135, 105)
        turtle.penup()
        turtle.goto(-127, 112)
        turtle.pencolor("orangered")
        turtle.pendown()
        turtle.setheading(60)
        turtle.circle(-155, 136)
        turtle.circle(-116, 86)
        turtle.circle(-220, 30)
        turtle.circle(-134, 103)
        turtle.penup()
        turtle.goto(-123, 108)
        turtle.pencolor("gold")
        turtle.pendown()
        turtle.setheading(60)
        turtle.circle(-150, 136)
        turtle.circle(-104, 86)
        turtle.circle(-220, 30)
        turtle.circle(-126, 102)
        turtle.penup()
        turtle.goto(-120, 104)
        turtle.pencolor("greenyellow")
        turtle.pendown()
        turtle.setheading(60)
        turtle.circle(-145, 136)
        turtle.circle(-90, 83)
        turtle.circle(-220, 30)
        turtle.circle(-120, 100)
        turtle.penup()

        # 爱心
        turtle.penup()
        turtle.goto(220, 115)
        turtle.pencolor("brown")
        turtle.pensize(1)
        turtle.fillcolor("brown")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(36)
        turtle.circle(-8, 180)
        turtle.circle(-60, 24)
        turtle.setheading(110)
        turtle.circle(-60, 24)
        turtle.circle(-8, 180)
        turtle.end_fill()

        # 五环
        turtle.penup()
        turtle.goto(-5, -170)
        turtle.pendown()
        turtle.pencolor("blue")
        turtle.circle(6)
        turtle.penup()
        turtle.goto(10, -170)
        turtle.pendown()
        turtle.pencolor("black")
        turtle.circle(6)
        turtle.penup()
        turtle.goto(25, -170)
        turtle.pendown()
        turtle.pencolor("brown")
        turtle.circle(6)
        turtle.penup()
        turtle.goto(2, -175)
        turtle.pendown()
        turtle.pencolor("lightgoldenrod")
        turtle.circle(6)
        turtle.penup()
        turtle.goto(16, -175)
        turtle.pendown()
        turtle.pencolor("green")
        turtle.circle(6)
        turtle.penup()

        turtle.pencolor("black")
        turtle.goto(-70, -160)
        turtle.write("BEIJING 2022@小树叶", font=('Arial', 10, 'bold italic'))
        turtle.hideturtle()

        turtle.done()
    elif pppppp == 19:
        from random import *
        from turtle import *

        from freegames import vector

        bird = vector(0, 0)
        balls = []


        def tap(x, y):
            """Move bird up in response to screen tap."""
            up = vector(0, 30)
            bird.move(up)


        def inside(point):
            """Return True if point on screen."""
            return -200 < point.x < 200 and -200 < point.y < 200


        def draw(alive):
            """Draw screen objects."""
            clear()

            goto(bird.x, bird.y)

            if alive:
                dot(10, 'green')
            else:
                dot(10, 'red')

            for ball in balls:
                goto(ball.x, ball.y)
                dot(20, 'black')

            update()


        def move():
            """Update object positions."""
            bird.y -= 5

            for ball in balls:
                ball.x -= 3

            if randrange(10) == 0:
                y = randrange(-199, 199)
                ball = vector(199, y)
                balls.append(ball)

            while len(balls) > 0 and not inside(balls[0]):
                balls.pop(0)

            if not inside(bird):
                draw(False)
                return

            for ball in balls:
                if abs(ball - bird) < 15:
                    draw(False)
                    return

            draw(True)
            ontimer(move, 50)


        setup(420, 420, 370, 0)
        hideturtle()
        up()
        tracer(False)
        onscreenclick(tap)
        move()
        done()

    elif pppppp == 20:
        # 用于实现GUI界面
        # import json
        import tkinter
        from tkinter import *
        from tkinter import messagebox

        # 写账户和密码的全局变量，用于登录,创建一个列表,用于储存信息
        account = ''
        password = ''

        Info = []
        try:
            with open('studentData.txt', 'r+', encoding='utf-8') as f:  # 当没有Studentdata文本时会发生报错，走入except中
                list = f.readlines()
                for item in list:
                    Info.append(eval(item))  # 将字符串利用eval转换为字典，储存进列表中
        except:
            with open('studentData.txt', 'w+', encoding='utf-8') as f:  # 由于还未生成Studentdata文件，利用w创建一个
                pass  # 由于刚创建文本，没有内容，所以不需要像上面那样把内容加入到Info中


        class Application_login(Frame):
            def __init__(self, master=None):
                super().__init__(master)
                self.master = master
                self.font = ('宋体', 12)
                self.pack()
                self.createWidget()

            def createWidget(self):
                messagebox.showinfo('提示', '账号请输入管理员或用户@你的小树叶')
                messagebox.showinfo('提示', '管理员请输入密码(123456)@你的小树叶')
                # 创建标签
                self.lab01 = Label(self, text='账号: ', font=self.font)
                self.lab02 = Label(self, text='密码: ', font=self.font)

                self.lab01.grid(row=0, column=0, sticky=NSEW)
                self.lab02.grid(row=1, column=0, sticky=NSEW)

                # 创建单行文本框
                self.account = StringVar()
                self.account.set('管理员')
                self.entry01 = Entry(self, textvariable=self.account, width=50, exportselection=False, font=self.font)
                self.entry01.grid(row=0, column=1, sticky=NSEW)

                self.password = StringVar()
                self.password.set('123456')
                self.entry02 = Entry(self, textvariable=self.password, width=50, exportselection=False, font=self.font)
                self.entry02.grid(row=1, column=1, sticky=NSEW)

                # 创建功能按钮
                self.btn01 = Button(self, text='登录', command=self.confirm, bg='silver')
                self.btn01.grid(row=2, column=0, columnspan=2, sticky=NSEW)

            def confirm(self):  # 用于确认登录者的信息
                global account
                global password
                print('用户输入的账户是： ', self.account.get())
                if self.account.get() == '管理员':
                    if self.password.get() == '' or self.password.get() == '若是管理员,请输入密码(用户可以直接点击登录)':
                        messagebox.showwarning('警告', '您是管理员，还未输入密码')
                    elif self.password.get() == '123456':
                        account = self.account.get()
                        password = self.password.get()
                        messagebox.showinfo('提示', '恭喜您以管理员身份登录成功')
                        self.login_destroy()
                    else:
                        messagebox.showwarning('警告', '您以管理员身份登录,密码错误')

                elif self.account.get() == '用户':
                    account = self.account.get()
                    messagebox.showinfo('提示', '恭喜您以用户身份登录')
                    self.login_destroy()

                elif self.account.get() == '请输入：管理员/用户' or self.account.get() == '':
                    messagebox.showwarning('学生管理系统登录', '你还未选择账户是管理员还是用户')
                else:
                    messagebox.showwarning('学生管理系统登录', '你选择的账户不符合规定')

            def login_destroy(self):
                login_gui.destroy()


        login_gui = Tk()
        login_gui.title('<<学生管理系统登录界面>>')
        login_gui.geometry('500x100+500+200')
        app_login = Application_login(master=login_gui)
        login_gui.mainloop()


        class Application(Frame):
            def __init__(self, master=None):
                super().__init__(master)
                self.master = master
                self.font = ("宋体", 12)
                self.student_list = []
                self.grid(row=0, column=0, columnspan=6)
                self.createWidget()

            def createWidget(self):
                self.btn01 = Button(self, text='添 加 学 生 信 息', bg='silver', font=('Arial', 12),
                                    command=self.Add_window, width=20)
                self.btn02 = Button(self, text='删 除 学 生 信 息', bg='silver', font=('Arial', 12),
                                    command=self.Del_window, width=20)
                self.btn03 = Button(self, text='修 改 学 生 信 息', bg='silver', font=('Arial', 12),
                                    command=self.Mod_window, width=20)
                self.btn04 = Button(self, text='查 询 学 生 信 息', bg='silver', font=('Arial', 12),
                                    command=self.Ser_window, width=20)
                self.btn05 = Button(self, text='显 示 学 生 信 息', bg='silver', font=('Arial', 12),
                                    command=self.Show_window, width=20)
                self.btn06 = Button(self, text='退 出 学 生 管 理 系 统', bg='silver', font=('Arial', 12),
                                    command=self.Exit_window, width=20)

                self.btn01.grid(row=0, column=0, sticky=NSEW, pady=15)
                self.btn02.grid(row=1, column=0, sticky=NSEW, pady=15)
                self.btn03.grid(row=2, column=0, sticky=NSEW, pady=15)
                self.btn04.grid(row=3, column=0, sticky=NSEW, pady=15)
                self.btn05.grid(row=4, column=0, sticky=NSEW, pady=15)
                self.btn06.grid(row=5, column=0, sticky=NSEW, pady=15)

                self.result = StringVar()
                self.result.set(
                    '>>>欢迎使用学生信息管理系统<<<\n   版本号:  V2.3   \n   @小树叶 \n  该版本更新时间:  2024,3,30')
                self.Show_result = Label(self, bg="white", fg="black", font=self.font, bd='0', anchor='nw',
                                         textvariable=self.result, width=100)
                self.Show_result.grid(row=0, column=1, rowspan=6, sticky=NSEW)

            def Add_window(self):
                # 窗口创建
                print('打开窗口: 添加学生信息')
                self.add_window = tkinter.Toplevel()
                self.add_window.title('添加学生信息')
                self.add_window.geometry('400x350+520+300')

                # 学号
                self.ID = StringVar()
                self.lab_ID = Label(self.add_window, text='学号（6位）：', font=self.font)
                self.entry_ID = Entry(self.add_window, textvariable=self.ID, width=30)
                self.lab_ID.grid(row=0, column=0, sticky=E, pady=15)
                self.entry_ID.grid(row=0, column=1, columnspan=5, sticky=EW)

                # 姓名
                self.name = StringVar()
                self.lab_name = Label(self.add_window, text='   姓名 ：', font=self.font)
                self.entry_name = Entry(self.add_window, textvariable=self.name, width=30)
                self.lab_name.grid(row=1, column=0, sticky=E, pady=15)
                self.entry_name.grid(row=1, column=1, columnspan=5, sticky=EW)

                # 专业
                self.major = StringVar()
                self.lab_major = Label(self.add_window, text='   专业 ：', font=self.font)
                self.entry_major = Entry(self.add_window, textvariable=self.major, width=30)
                self.lab_major.grid(row=2, column=0, sticky=E, pady=15)
                self.entry_major.grid(row=2, column=1, columnspan=5, sticky=EW)

                # 年龄
                self.age = StringVar()
                self.lab_age = Label(self.add_window, text='   年龄 ：', font=self.font)
                self.entry_age = Entry(self.add_window, textvariable=self.age, width=30)
                self.lab_age.grid(row=3, column=0, sticky=E, pady=15)
                self.entry_age.grid(row=3, column=1, columnspan=5, sticky=EW)

                # 班级
                self._class = StringVar()
                self.lab__class = Label(self.add_window, text='班级（序号）：', font=self.font)
                self.entry__class = Entry(self.add_window, textvariable=self._class, width=30)
                self.lab__class.grid(row=4, column=0, sticky=E, pady=15)
                self.entry__class.grid(row=4, column=1, columnspan=5, sticky=EW)

                # 电话
                self.phone = StringVar()
                self.lab_phone = Label(self.add_window, text='  电话 ：', font=self.font)
                self.entry_phone = Entry(self.add_window, textvariable=self.phone, width=30)
                self.lab_phone.grid(row=5, column=0, sticky=E, pady=15)
                self.entry_phone.grid(row=5, column=1, columnspan=5, sticky=EW)

                # 确认按钮
                self.add_confirm = Button(self.add_window, text='确认', bg='silver', font=self.font,
                                          command=lambda: self.student_add(self.ID.get(), self.name.get(),
                                                                           self.major.get(), self.age.get(),
                                                                           self._class.get(), self.phone.get()))
                self.add_confirm.grid(row=7, column=2, sticky=NSEW)

                # 取消按钮
                self.add_concel = Button(self.add_window, text='取消', bg='silver', font=self.font,
                                         command=lambda: self.concel(self.add_window))
                self.add_concel.grid(row=7, column=4, sticky=NSEW)

                self.add_window.mainloop()

            def Del_window(self):
                print('打开窗口: 删除学生信息')
                # 窗口创建
                self.del_window = tkinter.Toplevel()
                self.del_window.title('删除学生信息')
                self.del_window.geometry('450x110+550+400')

                # 提示标签
                self.lab_del_tip = Label(self.del_window, text='>>>请先通过"查询学生信息"查询待删除学生的学号<<<',
                                         bg='white', font=self.font)
                self.lab_del_tip.grid(row=0, column=0, columnspan=5, sticky=NSEW)

                # 删除学号
                self.del_ID = StringVar()
                self.lab_del_ID = Label(self.del_window, text='学号（6位）：', font=self.font)
                self.entry_del_ID = Entry(self.del_window, textvariable=self.del_ID, width=30)
                self.lab_del_ID.grid(row=1, column=0, sticky=E, pady=15)
                self.entry_del_ID.grid(row=1, column=1, columnspan=4, sticky=EW)

                # 确认按钮
                self.del_confirm = Button(self.del_window, text='确认', bg='silver', font=self.font,
                                          command=lambda: self.student_del(self.del_ID.get()))
                self.del_confirm.grid(row=2, column=1)

                # 取消按钮
                self.del_concel = Button(self.del_window, text='取消', bg='silver', font=self.font,
                                         command=lambda: self.concel(self.del_window))
                self.del_concel.grid(row=2, column=2)

                self.del_window.mainloop()

            def Mod_window(self):
                # 窗口创建
                print('打开窗口:修改学生信息')
                self.mod_window = tkinter.Toplevel()
                self.mod_window.title('修改学生信息')
                self.mod_window.geometry('470x110+550+400')

                # 提示标签
                self.lab_mod_tip = Label(self.mod_window, text='>>>请先通过"查询学生信息"查询待修改信息学生的学号<<<',
                                         bg='white', font=self.font)
                self.lab_mod_tip.grid(row=0, column=0, columnspan=5, sticky=NSEW)

                # 查询学号
                self.mod_ID = StringVar()
                self.lab_mod_ID = Label(self.mod_window, text='学号（6位）：', font=self.font)
                self.entry_mod_ID = Entry(self.mod_window, textvariable=self.mod_ID, width=30)
                self.lab_mod_ID.grid(row=1, column=0, sticky=E, pady=15)
                self.entry_mod_ID.grid(row=1, column=1, columnspan=4, sticky=EW)

                # 确认按钮
                self.mod_confirm = Button(self.mod_window, text='确认', bg='silver', font=self.font,
                                          command=lambda: self.student_mod(self.mod_ID.get()))
                self.mod_confirm.grid(row=2, column=1)

                # 取消按钮
                self.mod_concel = Button(self.mod_window, text='取消', bg='silver', font=self.font,
                                         command=lambda: self.concel(self.mod_window))
                self.mod_concel.grid(row=2, column=2)

                self.mod_window.mainloop()

            def Ser_window(self):
                # 窗口创建
                print('打开窗口: 查询学生信息')
                self.ser_window = tkinter.Toplevel()
                self.ser_window.title('查询学生信息')
                self.ser_window.geometry('400x400+600+250')
                # 提示标签
                self.lab_mod_tip = Label(self.ser_window,
                                         text='>>>输入学号/姓名,点击确认后开始查询<<<\n<<当学号和姓名同时存在时,仅使用学号查找>>',
                                         bg='white', font=self.font)
                self.lab_mod_tip.grid(row=6, column=0, columnspan=7, sticky=NSEW)

                # 学号
                self.ser_ID = StringVar()
                self.lab_ser_ID = Label(self.ser_window, text='学号（6位）：', font=self.font)
                self.entry_ser_ID = Entry(self.ser_window, textvariable=self.ser_ID, width=30)
                self.lab_ser_ID.grid(row=0, column=0, sticky=E, pady=15)
                self.entry_ser_ID.grid(row=0, column=1, columnspan=5, sticky=EW)

                # 姓名
                self.ser_name = StringVar()
                self.lab_ser_name = Label(self.ser_window, text='   姓名 ：', font=self.font)
                self.entry_ser_name = Entry(self.ser_window, textvariable=self.ser_name, width=30)
                self.lab_ser_name.grid(row=1, column=0, sticky=E, pady=15)
                self.entry_ser_name.grid(row=1, column=1, columnspan=5, sticky=EW)

                # 专业
                self.ser_major = StringVar()
                self.lab_ser_major = Label(self.ser_window, text='   专业 ：', font=self.font)
                self.entry_ser_major = Entry(self.ser_window, textvariable=self.ser_major, width=30)
                self.lab_ser_major.grid(row=2, column=0, sticky=E, pady=15)
                self.entry_ser_major.grid(row=2, column=1, columnspan=5, sticky=EW)

                # 年龄
                self.ser_age = StringVar()
                self.lab_ser_age = Label(self.ser_window, text='   年龄 ：', font=self.font)
                self.entry_ser_age = Entry(self.ser_window, textvariable=self.ser_age, width=30)
                self.lab_ser_age.grid(row=3, column=0, sticky=E, pady=15)
                self.entry_ser_age.grid(row=3, column=1, columnspan=5, sticky=EW)

                # 班级
                self.ser__class = StringVar()
                self.lab_ser__class = Label(self.ser_window, text='班级（序号）：', font=self.font)
                self.entry_ser__class = Entry(self.ser_window, textvariable=self.ser__class, width=30)
                self.lab_ser__class.grid(row=4, column=0, sticky=E, pady=15)
                self.entry_ser__class.grid(row=4, column=1, columnspan=5, sticky=EW)

                # 电话
                self.ser_phone = StringVar()
                self.lab_ser_phone = Label(self.ser_window, text='  电话 ：', font=self.font)
                self.entry_ser_phone = Entry(self.ser_window, textvariable=self.ser_phone, width=30)
                self.lab_ser_phone.grid(row=5, column=0, sticky=E, pady=15)
                self.entry_ser_phone.grid(row=5, column=1, columnspan=5, sticky=EW)

                # 确认按钮
                self.ser_confirm = Button(self.ser_window, text='确认', bg='silver', font=self.font,
                                          command=lambda: self.student_ser(self.ser_ID.get(), self.ser_name.get()))
                self.ser_confirm.grid(row=7, column=2, sticky=NSEW)

                # 取消按钮
                self.ser_concel = Button(self.ser_window, text='取消', bg='silver', font=self.font,
                                         command=lambda: self.concel(self.ser_window))
                self.ser_concel.grid(row=7, column=4, sticky=NSEW)

                self.ser_window.mainloop()

            def Show_window(self):  # 用于实现信息的展示
                global Info
                if len(Info) == 0:
                    messagebox.showinfo('提示', '暂无学生信息')
                    self.result.set('>>>>暂无学生信息<<<<')
                    return
                if account == '管理员':
                    student_content = ("{:<15}".format("学号") +
                                       "{:<15}".format("姓名") +
                                       "{:<15}".format("专业") +
                                       "{:<15}".format("年龄") +
                                       "{:<15}".format("班级") +
                                       "{:<15}".format("电话号码") +
                                       "\n")

                    for i in Info:
                        student_content += ("{:<15}".format(i['ID']) +
                                            "{:<15}".format(i['Name']) +
                                            "{:<15}".format(i['Major']) +
                                            "{:<15}".format(i['Age']) +
                                            "{:<15}".format(i['Class']) +
                                            "{:<15}".format(i['Telephone']) +
                                            "\n")
                    self.result.set(student_content)
                    messagebox.showinfo('提示', '显示学生信息成功')
                elif account == '用户':
                    messagebox.showinfo('提示', '由于您是用户,仅展示一部分学生信息')
                    student_content = ("{:<15}".format("学号") +
                                       "{:<15}".format("姓名") +
                                       "{:<15}".format("专业") +
                                       "{:<15}".format("班级") +
                                       "\n")

                    for i in Info:
                        student_content += ("{:<15}".format(i['ID']) +
                                            "{:<15}".format(i['Name']) +
                                            "{:<15}".format(i['Major']) +
                                            "{:<15}".format(i['Class']) +
                                            "\n")
                    self.result.set(student_content)
                    messagebox.showinfo('提示', '显示学生信息成功')

            def Exit_window(self):  # 用于实现退出窗口
                answer = messagebox.askyesno('退出学生管理系统', '您确定退出学生管理系统吗？')
                print('是否退出学生管理系统：', answer)
                if answer == True:  # 传回的是bool值，不是字符串,所以不用加引号
                    messagebox.showinfo('学生管理系统', '欢迎下次使用')
                    root.destroy()
                elif answer == False:
                    return

            def concel(self, window):  # 用于关闭窗口
                print('关闭窗口')
                window.destroy()

            def student_add(self, ID, name, major, age, _class, phone):  # 用于添加学生信息
                global Info

                if account == '管理员':
                    Info_dict = {'ID': ID, 'Name': name, 'Major': major, 'Age': age
                        , 'Class': _class, 'Telephone': phone}
                    print('添加的学生信息是:', Info_dict)
                    Info.append(Info_dict)
                    with open('studentData.txt', 'w', encoding='utf-8') as f:
                        for item in Info:
                            f.write(str(item) + '\n')
                        self.Tip_Add()
                        self.add_window.destroy()
                        self.Show_window()
                else:
                    messagebox.showwarning('警告', '您不是管理员,无法添加学生信息')

            def student_del(self, get_ID):  # 用于删除学生信息
                global Info
                ID = get_ID
                flag = 0
                if not self.is_ID(ID):
                    self.Tip_Add_ID()
                    return

                if account == '管理员':
                    for i in Info:
                        if i['ID'] == ID:
                            Info.remove(i)
                            flag = 1
                            break
                    if flag == 1:
                        for i in Info:
                            with open('studentData.txt', 'w', encoding='utf-8') as f:
                                f.write(str(i) + '\n')
                        self.Tip_Del()
                        self.Show_window()
                    else:
                        self.Tip_Del_ID_None()
                else:
                    messagebox.showwarning('警告', '您不是管理员,无法删除学生信息')

            def student_mod(self, get_ID):  # 用于更改学生信息
                global Info
                ID = get_ID

                if account == '管理员':
                    for i in Info:
                        if i['ID'] == ID:
                            self.student_del(ID)
                            messagebox.showinfo('提示', '要修改的信息已删除,请输入修改后的信息')
                            self.Add_window()
                            break
                        else:
                            self.Tip_Del_ID_None()

                else:
                    messagebox.showwarning('警告', '您不是管理员,无法修改学生信息')

            def student_ser(self, get_ID, get_Name):  # 用于查询学生信息
                global Info
                ID = get_ID
                Name = get_Name
                flag = 0
                if account == '管理员':
                    for i in Info:
                        if i['ID'] == ID:
                            self.ser_ID.set(i['ID'])
                            self.ser_name.set(i['Name'])
                            self.ser_major.set(i['Major'])
                            self.ser_age.set(i['Age'])
                            self.ser__class.set(i['Class'])
                            self.ser_phone.set(i['Telephone'])
                            flag = 1
                            break


                elif account == '用户':
                    messagebox.showinfo('提示', '由于您是用户，仅展示一部分内容')
                    for i in Info:
                        if i['ID'] == ID:
                            self.ser_ID.set(i['ID'])
                            self.ser_name.set(i['Name'])
                            self.ser_major.set(i['Major'])
                            self.ser__class.set(i['Class'])
                            flag = 1
                            break

            # 用于判断是否符合要求
            # 定于一个方法，用于检查学号是否规范

            def is_ID(self, ID):
                return len(ID) == 6 and ID.isdigit()

            # 提示信息
            def Tip_Add(self):
                messagebox.showinfo("提示信息", "添加成功")

            def Tip_Search(self):
                messagebox.showinfo("提示信息", "查询成功")

            def Tip_Del(self):
                messagebox.showinfo("提示信息", "删除成功")

            def Tip_Mod(self):
                messagebox.showinfo("提示信息", "修改成功")

            def Tip_Del_ID_None(self):
                messagebox.showinfo("提示信息", "此学号不存在，请重新输入！")

            def Tip_Search_None(self):
                messagebox.showinfo("提示信息", "未查询到有关学生信息！")


        if account == '管理员' or account == '用户':
            root = Tk()
            root.title('<<<学生管理系统>>>')
            root.geometry('1050x375+500+200')
            app = Application(master=root)

            root.mainloop()

    elif pppppp == 21:
        import turtle as t
        import math

        t.setup(1000, 750)  # 设置窗口大小
        t.setworldcoordinates(-800, -600, 800, 600)  # 设置坐标系
        t.title('I am ikun!!')
        t.width(8)
        t.speed(0)
        t.pencolor('black')


        # 以圆心和半径画圆
        def my_circle(rad, c_x, c_y, color=None):
            if color is not None:
                t.fillcolor(color)
                t.begin_fill()
            t.penup()
            t.setheading(0)
            t.goto(c_x, c_y - rad)
            t.pendown()
            t.circle(rad)
            if color is not None:
                t.end_fill()


        # 求θ角度方向上椭圆的坐标
        def get_ellipse_xy(a, b, theta):
            if theta < 0: theta = theta + math.pi * 2
            x = a * b / math.sqrt(b * b + a * a * math.tan(theta) * math.tan(theta))
            if theta < math.pi / 2:
                return {'x': x, 'y': x * math.tan(theta)}
            elif theta < math.pi:
                return {'x': x * (-1), 'y': x * (-1) * math.tan(theta)}
            elif theta < math.pi * 3 / 2:
                return {'x': x * (-1), 'y': x * (-1) * math.tan(theta)}
            else:
                return {'x': x, 'y': x * math.tan(theta)}


        # 画一个椭圆，shape为椭圆形状参数，start_ang、end_ang为起始角度(相对于椭圆中心）
        # shape = {"X0": 0,"Y0": 0,"a": 200,"b": 100,"angle": math.pi/3}
        def draw_ellipse(shape, start_ang, end_ang, color=None):
            if color is not None:
                t.fillcolor(color)
                t.begin_fill()
            a = shape['a']
            b = shape['b']
            shape_ang = shape['angle']
            theta = start_ang - shape_ang
            x1, y1 = get_ellipse_xy(a, b, theta).values()
            x = shape['X0'] + x1 * math.cos(shape_ang) - y1 * math.sin(shape_ang)
            y = shape['Y0'] + x1 * math.sin(shape_ang) + y1 * math.cos(shape_ang)
            t.penup()
            t.goto(x, y)
            t.pendown()
            step = math.pi / 180 * 2  # 以方位角2°一步
            num_steps = math.ceil((end_ang - start_ang) / step)  # 总步数
            for i in range(num_steps):
                theta = theta + step
                x1, y1 = get_ellipse_xy(a, b, theta).values()
                t.goto(shape['X0'] + x1 * math.cos(shape_ang) - y1 * math.sin(shape_ang),
                       shape['Y0'] + x1 * math.sin(shape_ang) + y1 * math.cos(shape_ang))
            if color is not None:
                t.end_fill()


        # 画篮球
        my_circle(150, -206, -212, '#BA7148')
        baskt_line1 = {"X0": -120, "Y0": -34, "a": 186, "b": 162, "angle": 0}
        draw_ellipse(baskt_line1, math.pi / 180 * 198, math.pi / 180 * 290)
        baskt_line2 = {"X0": -294, "Y0": -402, "a": 186, "b": 162, "angle": 0}
        draw_ellipse(baskt_line2, math.pi / 180 * 21, math.pi / 180 * 110)
        t.penup()
        t.goto(-346, -160)
        t.pendown()
        t.goto(-66, -274)

        # 画脸蛋
        face = {"X0": 80, "Y0": -22, "a": 256, "b": 198, "angle": 0}
        draw_ellipse(face, 0, math.pi * 2, '#F5D477')

        # 眼睛
        my_circle(77, 63, 41, 'white')
        my_circle(68, 217, 41, 'white')
        my_circle(24, 100, 34, 'black')
        my_circle(24, 244, 34, 'black')

        # 嘴巴
        t.width(5)
        mouth = {"X0": 145, "Y0": -73, "a": 75, "b": 53, "angle": 0}
        draw_ellipse(mouth, 0, math.pi * 2, '#F4A644')
        mouse_line = {"X0": 138, "Y0": -40, "a": 92, "b": 53, "angle": 0}
        draw_ellipse(mouse_line, math.pi / 180 * 208, math.pi / 180 * 342, '#F4A644')

        # 腮红
        t.width(1)
        t.pencolor('#F5D477')
        my_circle(62, -82, -62, 'red')  # 左边
        face_cheek = {"X0": 294, "Y0": -66, "a": 37, "b": 60, "angle": -math.pi / 180 * 12}
        draw_ellipse(face_cheek, 0, math.pi * 2, 'red')  # 右边
        # 腮红有点遮住脸的轮廓，重新绘制一遍
        t.pencolor('black')
        t.width(8)
        draw_ellipse(face, -math.pi / 3, math.pi / 3)


        # 定义一个画polygon的函数
        def draw_poly(poly_data, color=None):
            x = poly_data['x']
            y = poly_data['y']
            t.penup()
            t.goto(x[0], y[0])
            t.pendown()
            if color is not None:
                t.fillcolor(color)
                t.begin_fill()
            for i in range(len(x)):
                t.goto(x[i], y[i])
            if color is not None:
                t.end_fill()


        # 画头发
        poly_hair = {'x': [-258, -161, -74, 0, 55, 111, 211, 315, 362,
                           329, 293, 283, 269, 227, 269, 283, 208, 194,
                           160, 160, 85, 44, 61, 44, 31, 1, -33,
                           1, -60, -51, -60, -62, -129, -142, -144, -108,
                           -144, -142, -209, -216, -200, -216, -258],
                     'y': [57, 187, 238, 267, 251, 296, 260, 171,
                           47, -9, 29, 61, 110, 166, 110, 61, 72, 132,
                           178, 178, 174, 162, 206, 162,
                           29, 35, 54, 35, 4, 40, 4, -37, -45, -8, 71,
                           152, 71, -8, -31, 31, 90, 31, 57]
                     }
        draw_poly(poly_hair, '#D0CED1')

        # 头发下那个小三角
        hair2 = {'x': [160, 114, 85], 'y': [178, 218, 174]}
        draw_poly(hair2, '#797572')

        # 衣服
        poly_cloth = {'x': [-142, -112, -22, 50, 132, 218, 249, 247,
                            295, 328, 318, 321, 309, 338, 353, -167,
                            -150, -165, -166, -150, -162, -157, -142],
                      'y': [-135, -155, -144, -140, -150, -166, -163, -150,
                            -145, -165, -194, -233, -244, -290, -326, -328,
                            -248, -233, -209, -195, -167, -146, -135]
                      }
        draw_poly(poly_cloth, '#222222')
        cloth2 = {'x': [-58, 0, 89, 146, 205, 250, 212, 179, 89, 26, -27, -58],
                  'y': [-207, -203, -178, -184, -202, -208, -236, -246, -243, -237, -233, -207]
                  }
        t.width(2)
        draw_poly(cloth2, '#0A0A0C')  # 中间黑的那一块

        # 左右背带
        strap1 = {'x': [-150, -92, -57, -41, -39, -46], 'y': [-220, -227, -243, -277, -306, -328]}
        strap2 = {'x': [309, 269, 238, 224, 222], 'y': [-222, -233, -257, -292, -326]}
        t.width(18)
        t.pencolor('#D3D1D4')
        draw_poly(strap1)
        draw_poly(strap2)

        # 中间背带
        t.width(10)
        strap3 = {'x': [-17, 90, 209, 90, 93], 'y': [-251, -273, -248, -273, -290]}
        draw_poly(strap3)
        t.width(2)
        t.pencolor('white')
        my_circle(30, 97, -320, '#D1D1D3')

        # 文字kun
        k = {'x': [78, 78, 78, 88, 78, 88], 'y': [-312, -326, -319, -312, -319, -326]}
        draw_poly(k)
        u = {'x': [93, 93, 98, 103, 103], 'y': [-312, -323, -326, -323, -312]}
        draw_poly(u)
        n = {'x': [109, 109, 119, 119], 'y': [-326, -312, -326, -312]}
        draw_poly(n)

        t.resizemode("user")
        t.shapesize(0.8, 0.8)
        t.hideturtle()
        t.done()

    elif pppppp == 22:
        from random import random
        from turtle import *

        from freegames import line


        def draw():
            """Draw maze."""
            color('black')
            width(5)

            for x in range(-200, 200, 40):
                for y in range(-200, 200, 40):
                    if random() > 0.5:
                        line(x, y, x + 40, y + 40)
                    else:
                        line(x, y + 40, x + 40, y)

            update()


        def tap(x, y):
            """Draw line and dot for screen tap."""
            if abs(x) > 198 or abs(y) > 198:
                up()
            else:
                down()

            width(2)
            color('red')
            goto(x, y)
            dot(4)


        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        draw()
        onscreenclick(tap)
        done()

    elif pppppp == 23:
        messagebox.showinfo('提示', '制作中......')
        continue
        print('ww可以退出')
        import random

        while True:

            options = ['石头', '剪刀', '布']
            computer_choice = random.choice(options)
            user_choice = input('请出拳（石头、剪刀、布）：')
            if user_choice == 'ww':
                print('触发退出!!!')
                break
            print('你出了', user_choice)
            print('电脑出了', computer_choice)
            if user_choice == computer_choice:
                print('平局')
            elif user_choice == '石头' and computer_choice == '剪刀' or \
                    user_choice == '剪刀' and computer_choice == '布' or \
                    user_choice == '布' and computer_choice == '石头':
                print('你赢了')
            else:
                print('你输了')

    elif pppppp == 24:
        # author:Monster
        # encoding=utf-8
        from turtle import *
        import random

        n = 6
        speed(10)
        color = ['red', 'yellow', 'blue', 'green', 'chocolate', 'deep pink', 'purple', 'cyan2', 'SeaGreen']
        for i in range(99):
            random_int = random.randint(0, 8)
            pencolor(color[random_int])
            forward(i * 5 / 3 + i)
            # circle(i//2,360)
            left(360 / n + 10)
            pensize(random_int % 3)
        done()
    elif pppppp==25:
        messagebox.showinfo('提示', '制作中......')
        continue
        import random
        a=random.randint(0, 10000)
        a=int(a)
        b=random.randint(0,10000)
        b=int(b)
        p=a+b
        print(a,'+',b,'等于几???')
        b=input('')
        b=int(b)
        if b==p:
            print('对了!!')
        else:
            print('你煞笔吧')


    else:

        messagebox.showinfo('提示', 'TM,D输入正常的数字')

        print('                         ')
        continue
