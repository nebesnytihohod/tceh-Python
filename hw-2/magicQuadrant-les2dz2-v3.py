# -*- coding: utf-8 -*-
import sys
import random

def createField():
    i = True
    ii = True
    while i:
        x = input("Укажите размер игрового поля по-горизонтали: X = ")    # dimX - column
        if 1 < int(x) < 10:
            i = False
    while ii:
        y = input("Укажите размер игрового поля по-вертикали: Y = ")      # dimY - row
        if 1 < int(y) < 10:
            ii = False
    xy = [x, y]
    return xy

def q(x, y, gameField):    # функция для создания массива: yes – игровой массив; no – массив индексов
    array = []
    for i in range(x*y):
        if gameField == 1:
            array.append(str(i + 1))
        else:
            array.append(i)
    if gameField == 1:
        ar = array[0:(x*y)-1]
    else:
        ar = array
    return ar

z = lambda array, i: array.insert(i - 1, 'empty')    # функция для вставки пустого поля в игровой массив

def border(x, y):         # функция для определения границ
    indexes = q(x, y, 0)                              # создание массива индексов
    limitsL = indexes[0:len(indexes):x]               # определение левых границ
    limitsR = sorted(indexes[len(indexes):0:-x])      # определение правых границ
    limitsT = indexes[0:x]                            # определение верхней границы
    limitsB = indexes[len(indexes) - x:len(indexes)]  # определение нижней границы
    limits = [limitsL, limitsR, limitsT, limitsB]
    return limits          # получение одного массива для всех границ
    
def shuffle_trick(array):
    return random.shuffle(array)    # перемешивание фишек

def print_field(x, y, array, limits):    # функция вывода игрового поля
    for i in range(y):
        s = limits[0][i]
        e = limits[1][i]
        p = array[s:e+1]
        print()    # для перехода на другую строку
        for n in range(x):
            print('[{:^5}]'.format(p[n]), end='')

    print("\nНаправления перемещения: w-up; a - left; s - down; d - right")
    print("Если хотите завершить игру - наберите exit - ENTER\n")

def changeTrick(array, indexEmpty, i):    # function of the change (move) trick
    temp = array[i]
    array[i] = array[indexEmpty]
    array[indexEmpty] = temp
    return array

def is_game_finished(array):
    if array[len(array) - 1] == "empty":
        for i in range(len(array) - 2):
            if int(array[i]) + 1 == int(array[i + 1]):
                game = 0
            else:
                game = 1
    else:
        game = 1
    return game

def check(i, indexE, borderField, array):
    if (i in borderField) and (indexE in borderField):
        checkResult = False
    elif (i < 0) or ((len(array) - 1) < i):
        checkResult = False
    else:
        checkResult = True
    return checkResult

def movie(x, y, array, limits):    # управление перемещениями фишек
    attempt = 0    # инициализация счетчика ходов
    game = 1          # инициализация условия цикла
    lr = limits[0] + limits[1]
    tb = limits[2] + limits[3]
    #result = []
    while game == 1:
        indexEmpty = array.index('empty')
        print_field(x, y, array, limits)   # вывод игрового поля
        key = input()
        if key == 's':
            newPosition = indexEmpty - x
            b = check(newPosition, indexEmpty, tb, array)
            changeTrick(array, indexEmpty, newPosition) if b else print("туда нельзя!")
        elif key == 'w':
            newPosition = indexEmpty + x
            b = check(newPosition, indexEmpty, tb, array)
            changeTrick(array, indexEmpty, newPosition) if b else print("туда нельзя!")
        elif key == 'a':
            newPosition = indexEmpty + 1
            b = check(newPosition, indexEmpty, lr, array)
            changeTrick(array, indexEmpty, newPosition) if b else print("туда нельзя!")
        elif key == 'd':
            newPosition = indexEmpty - 1
            b = check(newPosition, indexEmpty, lr, array)
            changeTrick(array, indexEmpty, newPosition) if b else print("туда нельзя!")
        elif key == 'exit':
            #result[0] = key
            break
            game = 0
        else:
            print("for manipulation gaming trick use: w-up, left-a, down-s, right-d")
        game = is_game_finished(array)
        attempt += 1
    #result[1] = attempt
    return attempt

def main():
    versionPython = sys.version_info[0]    # проверка версии Python и переназначение функции input
    if versionPython == 2:
        consoleInput = raw_input
    else:
        consoleInput = input

    xy = createField()
    dimX, dimY = xy[0], xy[1]
    mq = q(int(dimX), int(dimY), 1)    # стартовая инициализация игрового поля
    z(mq, int(dimX) * int(dimY))           # в конец вставляем пустышку
    l = border(int(dimX), int(dimY))    # определение границ игрового поля
    shuffle_trick(mq)       # перемешивание фишек
    r = movie(int(dimX), int(dimY), mq, l)    # перемещение фишек
    print_field(int(dimX), int(dimY), mq, l)
    print("Вы сделали " + str(r) + " ходов")
    input('Спасибо за игру и до новых встреч! А теперь... Press any key')


if __name__ == '__main__':
    main()