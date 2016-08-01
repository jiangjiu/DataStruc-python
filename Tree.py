# -*- coding:utf-8 -*-


# myTree = ['a', ['b', ['d', [], []], ['e', [], []]], ['c', ['f', [], []], []]]
#
#
# # 定义二叉树
# def BinaryTree(r):
#     return [r, [], []]
#
#
# # 插入左节点
# def insert_left(root, newBranch):
#     t = root.pop(1)
#     if len(t) > 1:
#         root.insert(1, [newBranch, t, []])
#     else:
#         root.insert(1, [newBranch, [], []])
#     return root
#
#
# # 插入右节点
# def insert_right(root, newBranch):
#     t = root.pop(2)
#     if len(t) > 1:
#         root.insert(2, [newBranch, [], t])
#     else:
#         root.insert(2, [newBranch, [], []])
#
#
# def get_root_val(root):
#     return root[0]
#
#
# def set_root_val(root, newVal):
#     root[0] = newVal
#
#
# def get_left_child(root):
#     return root[1]
#
#
# def get_right_child(root):
#     return root[2]


#
# r = BinaryTree(3)
# print r
# insert_left(r, 4)
# insert_left(r, 5)
# insert_right(r, 6)
# insert_right(r, 7)
# l = get_left_child(r)
# print(l)
#
# set_root_val(l, 9)
# print(r)
# insert_left(l, 11)
# print(r)
# print(get_right_child(get_right_child(r)))


class BinaryTree(object):
    def __init__(self, root_obj):
        self.key = root_obj
        self.leftChild = None
        self.rightChild = None

    def insert_left(self, new_node):
        if self.leftChild is None:
            self.leftChild = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insert_right(self, new_node):
        if self.rightChild is None:
            self.rightChild = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.leftChild = self.leftChild
            self.leftChild = t

    def get_right_child(self):
        return self.rightChild

    def get_left_child(self):
        return self.leftChild

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key


r = BinaryTree('a')
print r.get_root_val()
print r.get_left_child()

r.insert_left('b')
print r.get_left_child()
print (r.get_left_child().get_root_val())

r.insert_right('c')
print r.get_right_child()
print r.get_right_child().get_root_val()

r.get_right_child().set_root_val('hello')
print r.get_right_child().get_root_val()