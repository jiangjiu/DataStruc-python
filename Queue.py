# -*- coding: utf-8 -*-


class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, elem):
        self.items.insert(0, elem)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return

    def size(self):
        return len(self.items)


q = Queue()
print q.size()

q.is_empty()

print q.enqueue('dog')
print q.size()
print q.enqueue(4)

print q.enqueue(4)


print q.enqueue('dog')
print q.enqueue(True)
print q.dequeue()
print q.dequeue()
print q.dequeue()
