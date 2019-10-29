
from nodes import DoubleLinkedNode


class LinkedList:
    def __init__(self):
        self._node = DoubleLinkedNode
        self.head = self.tail = None

    def _reset(self):
        self.head = self.tail = None

    def _init_insert(self, value):
        self.head = self.tail = self._node(value, prev=None, nxt=None)

    def push(self, value):
        if not self.head:
            self._init_insert(value)
        else:
            self.tail = self._node(value, prev=self.tail, nxt=None)
            self.tail.prev.next = self.tail

    def pop(self):
        node = self.tail
        self.tail = node.prev
        try:
            self.tail.next = None
        except AttributeError:
            self._reset()

    def unshift(self):
        node = self.head
        self.head = node.next
        try:
            self.head.prev = None
        except AttributeError:
            self._reset()

    def get(self, obj):
        for node in self:
            if obj == node.value:
                return node.value
        return None

    def remove(self, obj):
        for node in self:
            if node.value == obj:
                if node is self.head:
                    self.unshift()
                elif node is self.tail:
                    self.pop()
                else:
                    prev_node, next_node = node.prev, node.next
                    prev_node.next, next_node.prev = next_node, prev_node
                break
        return None

    @property
    def count(self):
        i = 0
        for node in self:
            i += 1
        return i

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = next(node)
        return

    def __len__(self):
        return self.count

    def __bool__(self):
        return bool(len(self))
