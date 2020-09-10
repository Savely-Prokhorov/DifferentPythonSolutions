class Tree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

tr = Tree(1, Tree(2, None, None), Tree(3, None, None))
tr.left.left = Tree(4, Tree(6, None, None), Tree(7, None, None))
tr.left.right = Tree(5, None, None)

while tr is not None:
    tr = tr.left
    if tr is not None:
        print(tr.data, end='; ')
