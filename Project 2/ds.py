
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.value)


class DoubleLinkedList:

    # self.root is a sentinel. self.root.next is head. self.root.prev is tail
    def __init__(self):
        self.root = Node(None)
        self.length = 0

    def append(self, value):
        node = Node(value)

        if self.length == 0:
            self.root.next = node
            self.root.prev = node
        else:
            tail = self.root.prev
            tail.next = node
            node.prev = tail
            self.root.prev = node

        self.length += 1








