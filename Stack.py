# -*- coding: utf-8 -*-


class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, elem):
        self.items.append(elem)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


s = Stack()

print s.is_empty()

print s.pop()

s.push(4)
s.push('dog')
print s.peek()

s.push(True)
print(s.size())
print(s.is_empty())

s.push(8.4)
print(s.pop())
print(s.pop())

print (s.size())
