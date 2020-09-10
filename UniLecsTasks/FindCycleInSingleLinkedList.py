class Node:
    def __init__(self, data, nxt):
        self.data = data
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.len = 0

    # TODO
    def __repr__(self):
        ll = self.first
        repres = ''
        while ll is not None:
            repres += repr(ll.data) + ' -> '
            ll = ll.next
        return repres

    def add(self, x):
        if self.first is None:
            self.first = self.last = Node(x, None)  # указывают на одну и ту же область в памяти
        else:
            self.last.next = self.last = Node(x, None)
        self.len += 1

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
print(ll)
