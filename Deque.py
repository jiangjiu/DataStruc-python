# -*- coding:utf-8 -*-


class Deque(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_rear(self, elem):
        self.items.insert(0, elem)

    def add_front(self, elem):
        self.items.append(elem)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        return

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        return

    def size(self):
        return len(self.items)


d = Deque()
print(d.is_empty())
d.add_rear(4)
d.add_rear('dog')
d.add_front('cat')
d.add_front(True)
print(d.size())
print(d.is_empty())
d.add_rear(8.4)
print(d.remove_rear())
print(d.remove_front())
