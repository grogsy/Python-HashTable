class Node:
    '''Node'''

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        # Better using ternary operator and makes more sense to read too
        next_val = self.next.value if self.next else None
        return f"[{self.value}:{repr(next_val)}]"

    # Suppoer for iteration in controller structures
    def __iter__(self):
        return self

    def __next__(self):
        return self.next


class DoubleLinkedNode(Node):
    def __init__(self, value, prev, nxt):
        super().__init__(value, nxt)
        self.prev = prev

    def __repr__(self):
        prev_val = self.prev.value if self.prev else None
        next_val = self.next.value if self.next else None

        return f"[{prev_val}:{self.value}:{next_val}]"


class HashNode(DoubleLinkedNode):
    def __init__(self, key, **kwargs):
        super().__init__(**kwargs)
        self.key = key
