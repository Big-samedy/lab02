# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр 02_global_color.py скопировать сюда
# Результат решения см results/exercise_03_shape_select.jpg

# TODO здесь ваш код

color_rainbow = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                 sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

def vector(vector_start, length, angle):
    v = sd.get_vector(vector_start, angle, length)
    return v.end_point


def polygon(point, heads, length, color):
    angle = 0
    angle_start = 15
    angle_polygon = 360 / heads
    point_polygon = point
    color_paint = color_rainbow[color - 1]
    for _ in range(heads):
        if _ == 0:
            angle = angle_start
        else:
            angle += angle_polygon
        if _ < (heads - 1):
            end_point = vector(point, length, angle)
        else:
            end_point = point_polygon
        sd.line(start_point=point, end_point=end_point, color=color_paint, width=1)
        point = end_point


start_point = [(100, 100, 150, 3), (400, 100, 150, 4), (100, 350, 100, 5), (400, 350, 100, 6)]
color_input = 1
figur_input = 1

while color_input and figur_input:
    figur_input = input('Введите, номер желаемой фигуры: \n'
                        '   1: Треугольник\n'
                        '   2: Квадрат\n'
                        '   3: Пятиугольник\n'
                        '   4: Шестиугольник\n')

    if figur_input.isnumeric():
        figur_input = int(figur_input)
        if figur_input < 1 or figur_input > 4:
            print('Неверный ввод')
            continue
    else:
        print('Неверный ввод')
        continue

    color_input = input('Введите, номер желаемого цвета:\n'
                        '   1: Красный\n'
                        '   2: Оранжевый\n'
                        '   3: Жёлтый\n'
                        '   4: Зелёный\n'
                        '   5: Голубой\n'
                        '   6: Синий\n'
                        '   7: фиолетовый\n')
    if color_input.isnumeric():
        color_input = int(color_input)
        if color_input < 0 or color_input > 7:
            print('Неверный ввод')
            continue
    else:
        print('Неверный ввод')
        continue

    point_start = sd.get_point(start_point[figur_input - 1][0], start_point[figur_input - 1][1])
    length_start = start_point[figur_input - 1][2]
    heads_start = start_point[figur_input - 1][3]
    polygon(point_start, heads_start, length_start, color_input)

    break

sd.pause()

