# -*- coding: utf-8 -*-
import sys
import json
import random

"""
проверка версии Питона с назначением нового имени для функции

"""
versionPython = sys.version_info[0]
if versionPython == 2:
    consoleInput = raw_input
else:
    consoleInput = input

"""
чтение файла настроек формата JSON и присвоение параметров переменным

"""
try:
    f = open('config.json', 'r')
except OSError:    # если нет файла настроек, то устанавливаем по-умолчанию
    maxAttempt=3
    maxAttemptAnswer=3
    maxRepeatCircle=3
    print("Файл настроек не найден. Установлены значения по-умолчанию.")
    print("Количество попыток - " + str(maxAttempt))
else:
    configuration = json.load(f)    # парсинг файла настроек
    #maxAttempt = configuration['maxAttempt']    # макс количество попыток выбора ветви исполнения
    #maxAttemptAnswer = configuration['maxAttemptAnswer']    # макс количество попыток правильного ответа
    #maxRepeatCircle = configuration['maxRepeatCircle']    # макс число циклов
finally:
    f.close()

"""
инициализация счетчиков

"""
uI = 0
attemptAnswer = 0
repeatCircle = 0
stopFlag = 0

"""
объявление переменных с присвоением текстовых строк с вопросами и ответами

"""
q1 = "Сколько в байте бит?\n"
a1 = "8"
q2 = "Как обозначается целый тип?\n"
a2 = "int"
q3 = "Ева?\n"
a3 = "да"

listQ = []
listQ.append(q1)
listQ.append(q2)
listQ.append(q3)

listA = []
listA.append(a1)
listA.append(a2)
listA.append(a3)

"""
выбор ветви выполнения программы

"""
while uI < configuration['maxAttempt']:    # цикл выбора ветви выполнения
    user1Choice = consoleInput("Чиста (п)оржать или (с)ерьезно?")
    if user1Choice == 'п':
        random.shuffle(listQ)    # генерация случайных перестановок
        random.shuffle(listA)
        uI = configuration['maxAttempt']    # управление циклом выбора ветви выполнения - завершение цикла
    elif user1Choice == 'с':
        uI = configuration['maxAttempt']
    else:
        print("Не шали!")
        uI +=1
        stopFlag = 1

if stopFlag == 1:
    print('Ну и зря! :-Р')
    consoleInput('Press any key')
    exit()
#print(listQ)    # для периода отладки
#print(listA)    # для периода отладки

"""
цикл вывода вопросов, ответов, прием данных ответа

"""
while repeatCircle < configuration['maxRepeatCircle']:
    for item in range(len(listQ)):
        attemptAnswer = 0    # возврат счетчика в исходное состояние
        print("Вопрос: \n" + str(item) + listQ[item] + "\n")
        while attemptAnswer < configuration['maxAttemptAnswer']:
            userAnswer = consoleInput("Ваш ответ: ")
            if userAnswer == listA[item]:
                print("Bingo!")
                attemptAnswer = configuration['maxAttemptAnswer']
            else:
                print("Думай еще!")
                attemptAnswer +=1
                if attemptAnswer == configuration['maxAttemptAnswer']:
                    print("Все неверно! Учи матчасть дальше...\n")
    
    i = 1
    while i == 1:
        user2Choice = consoleInput("Еще раз по вопросам пройдемся? - (д)а/(н)ет ")
        if user2Choice == 'н':
            repeatCircle = configuration['maxRepeatCircle']    # для завершения работы
            i = 0    # для выхода из цикла запроса повтора
        elif user2Choice == 'д':
            repeatCircle +=1
            i = 0
        else:
            print("Ась? Чегось?")
            i = 1

consoleInput('До новых встреч в эфире! А теперь... Press any key')