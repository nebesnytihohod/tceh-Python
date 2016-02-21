# -*- coding: utf-8 -*-
import sys
import random

"""
проверка версии Python и переназначение функции input

"""
versionPython = sys.version_info[0]
if versionPython == 2:
    consoleInput = raw_input
else:
    consoleInput = input

"""
объявление и инициализация списка в виде массива 4х4

"""
mq = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 'NON']]
print("mq", mq)

"""
перемешивание фишек

"""
random.shuffle(mq)
print("mqS", mq)

"""
алгоритм движения фишек
перемещается фишка NON - направление обратное выбранному
если вправо, то NON(column - 1) ; если влево, то NON(column + 1)
если вверх, то NON(row - 1) ; если вниз, то NON(row + 1)

"""

"""
цикл движения (игры)

"""
attempt = 0    # инициализация счетчика ходов
i = 1    # инициализация условия цикла
while i == 1:
	print(mq)    # вывод игрового поля
	print("\nДля перемещения фишки нажмите клавишу управления курсором\n")
	print("Если хотите завершить игру - нажмите любую другую клавишу...\n")
	move = consoleInput()    # обработка клавиш управления курсором
	attempt +=1
	if move == right:
		NON(column - 1)
	elif move == left:
		NON(column + 1)
	elif move == up:
		NON(row - 1)
	elif move == down:
		NON(row + 1)
	else:
		i = 0

print("Вы сделали " + str(attempt) + "ходов")
consoleInput('Спасибо за игру и до новых встреч! А теперь... Press any key')