import sys
import os
import xml.etree.ElementTree as et    # вариант реализации парсинга

#FILE_PATH_Q = os.curdir + 'question.xml'
#FILE_PATH_A = os.curdir + 'answer.xml'
#print(FILE_PATH_Q)
try:    # проверка существования файлов вопросов и ответов
    fileQA = open('qa.xml', 'r')
    #fileQuestion = open('answer.xml', 'r')
except FileNotFoundError:
    print('нет файла вопросов и ответов')
    exit()
# else:

'''
разбор и чтение из qa.xml
'''
treeQA = et.parse(fileQA)
#print(treeQA)
#print(len(treeQA))
rootQA = treeQA.getroot()
child = rootQA.getchildren()
print(child)
print(child.tag)
allLinks = rootQA.findall('question')
print(allLinks.attrib)
"""
проверка версии Питона с назначением нового имени для функции
"""
versionPython = sys.version_info[0]    # проверка версии транслятора для правильного использования ввода в консоли
if versionPython == 2:
    ConsoleInput = raw_input
else:
    ConsoleInput = input

"""
цикл вывода вопросов, ответов, прием данных ответа
"""
while True:
    print('Вопрос:\n', question)
    userAnswer = ConsoleInput('Ваш ответ: ')
    if userAnswer == answer:
        print('правильно!')
        continue
    else:
        print('ошибочка!')
        continue

fileQA.close()
#fileQuestion.close()
