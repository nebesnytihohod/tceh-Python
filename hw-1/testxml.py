import sys
import xml.etree.ElementTree as et    # вариант реализации парсинга
import xml.parsers.expat as xe
import xml.dom.minidom as md
import xml.sax as sax

fileQA = open('qa.xml', 'r')

"""
разбор через xml.etree.ElementTree
"""
treeQA = et.parse(fileQA)    # создание объекта типа ElementTree со структурой DOM
rootQA = treeQA.getroot()    # создание объекта-контейнера типа Element со списком корневых элементов
print("Type treeQA", type(treeQA))
print("treeQA", treeQA)
print("Type rootQA", type(rootQA))
print("rootQA", rootQA)
print("rootQA.tag", rootQA.tag)

child = rootQA.getchildren()
print("child", child)
child.attrib

allLinks = rootQA.findall('question')
print(allLinks)

