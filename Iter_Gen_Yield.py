# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:38:16 2023

@author: nikolaicev_na

"""
import types


class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def get_new_list(self):
        l = iter(self.list_of_lists)
        l_new = []
        flag = 0
        while True:
            try:
                a = next(l)
                if type(a) is list:
                    l_new.extend(a)
                    flag = 1
                else:
                    l_new.append(a)
            except StopIteration:
                if flag == 1:
                    self.list_of_lists = l_new
                    self.list_of_lists = self.get_new_list()
                return self.list_of_lists

    def __iter__(self):
        self.couter = -1
        self.new_list = self.get_new_list()
        return self

    def __next__(self):
        if self.couter < len(self.new_list) - 1:
            self.couter += 1
            return self.new_list[self.couter]
        else:
            raise StopIteration


def flat_generator(list_of_lists):
    new_list = FlatIterator(list_of_lists).get_new_list()
    for i in new_list:
        yield i


def check_script(flat_list, check_list, task):
    if task in [1, 3]:
        list_items = FlatIterator(flat_list)
    else:
        list_items = flat_generator(flat_list)

    for flat_iterator_item, check_item in zip(list_items, check_list):
        print(flat_iterator_item, check_item)
        assert flat_iterator_item == check_item

    assert list(FlatIterator(flat_list)) == check_list
    assert list(flat_generator(flat_list)) == check_list
    assert isinstance(flat_generator(flat_list), types.GeneratorType)


def task():
    # data lists for task 1 and task 2
    list_of_list_1 = [["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]]
    list_of_list_2 = [
        [["a"], ["b", "c"]],
        ["d", "e", [["f"], "h"], False],
        [1, 2, None, [[[[["!"]]]]], []],
    ]

    # check lists for task 3 and task 4
    check_list_1 = ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None]
    check_list_2 = ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None, "!"]

    tasks = [1, 2, 3, 4]
    for i in tasks:
        if i in [1, 2]:
            check_script(list_of_list_1, check_list_1, task=i)
        else:
            check_script(list_of_list_2, check_list_2, task=i)


if __name__ == "__main__":
    task()
