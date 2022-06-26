# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр 01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см /results/exercise_02_global_color.jpg

# TODO здесь ваш код

def figure(figure_point, length_tri, angle_tri, angles, figure_color):
    n = angles
    angle = (n - 2) / n * 180
    new_angle = 0 + angle_tri
    point1 = figure_point
    for _ in range(0, n - 1):
        v1 = sd.get_vector(figure_point, new_angle, length_tri, 2)
        v1.draw(color=figure_color)
        new_angle += 180 - angle
        figure_point = v1.end_point
    sd.line(point1, figure_point, color=figure_color, width=2)


def triangle(figure_color, figure_point):
    figure(figure_point, 100, 25, 3, figure_color)


def square(figure_color, figure_point):
    figure(figure_point, 100, 25, 4, figure_color)


def pentagon(figure_color, figure_point):
    figure(figure_point, 65, 25, 5, figure_color)


def hexagon(figure_color, figure_point):
    figure(figure_point, 65, 25, 7, figure_color)


colors = {'1': {'Название цвета': 'Красный', 'Цвет': sd.COLOR_RED},
          '2': {'Название цвета': 'Оранжевый', 'Цвет': sd.COLOR_ORANGE},
          '3': {'Название цвета': 'Жёлтый', 'Цвет': sd.COLOR_YELLOW},
          '4': {'Название цвета': 'Зелёный', 'Цвет': sd.COLOR_GREEN},
          '5': {'Название цвета': 'Циан', 'Цвет': sd.COLOR_CYAN},
          '6': {'Название цвета': 'Синий', 'Цвет': sd.COLOR_BLUE},
          '7': {'Название цвета': 'Фиолетовый', 'Цвет': sd.COLOR_PURPLE}}

for number, color in colors.items():
    print(number, ' - ', color['Название цвета'])

t_point = sd.get_point(100, 450)
s_point = sd.get_point(100, 100)
h_point = sd.get_point(400, 450)
p_point = sd.get_point(400, 110)

x = input("Введите свой номер: ")

if x in colors:
    point = sd.get_point(100, 350)
    triangle(colors[x]['Цвет'], t_point)
    square(colors[x]['Цвет'], s_point)
    pentagon(colors[x]['Цвет'], p_point)
    hexagon(colors[x]['Цвет'], h_point)
    sd.pause()
else:
    print('Вы ввели неправильное значение. Повторите попытку!')

sd.pause()
