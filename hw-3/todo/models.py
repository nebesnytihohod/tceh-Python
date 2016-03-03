# -*- coding: utf-8 -*-

__author__ = 'sobolevn'

from utils import get_input_function


class Storage(object):
    obj = None

    items = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
        return cls.obj


class BaseItem(object):
    def __init__(self, heading):
        self.heading = heading
        self.done = False

    def __repr__(self):
        return self.__class__

    @classmethod
    def construct(cls):
        raise NotImplemented()


class ToReadItem(BaseItem):
    def __init__(self, heading, link, due_day):
        super(ToReadItem, self).__init__(heading)
        self.link = link
        self.due_day = due_day

    def __str__(self):
        return 'ToReadItem: {} for {}: {}'.format(self.heading, self.link, self.due_day)

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        link = input_function('Input link: ')
        due_date = input_function('Input due date: ')
        return ToBuyItem(heading, link, due_date)


class ToDoItem(BaseItem):
    def __str__(self):
        return 'ToDo: {}: {}'.format(self.heading, self.done)

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        return ToDoItem(heading)


class ToBuyItem(BaseItem):
    def __init__(self, heading, price):
        super(ToBuyItem, self).__init__(heading)
        self.price = price

    def __str__(self):
        return 'ToBuy: {} for {}: {}'.format(self.heading, self.price, self.done)

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        price = input_function('Input price: ')
        return ToBuyItem(heading, price)

