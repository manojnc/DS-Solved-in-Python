from queue_LinkedList import queue_LinkedList as Queue


class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, e, left=None, right=None):
        self._element = e
        self._left = left
        self._right = right


class BinaryTree:
    countOfElements = 0

    def __init__(self):
        self._root = None

    def __len__(self):
        return BinaryTree.countOfElements

    def makeTree(self, e, left, right):
        self._root = _Node(e, left._root, right._root)
        BinaryTree.countOfElements += 1
        return

    def inOrder(self, troot):
        if troot:
            self.inOrder(troot._left)
            print(troot._element, end=' ')
            self.inOrder(troot._right)
        return

    def preOrder(self, troot):
        if troot:
            print(troot._element, end=' ')
            self.preOrder(troot._left)
            self.preOrder(troot._right)
        return

    def postOrder(self, troot):
        if troot:
            self.postOrder(troot._left)
            self.postOrder(troot._right)
            print(troot._element, end=' ')
        return

    def levelOrder(self):
        t = self._root
        print(t._left)
        Q = Queue()
        print(t._element, end=" ")
        Q.enQueue(t)
        while not Q.isEmpty():
            t = Q.deQueue()
            if t._left:
                print(t._left._element, end=" ")
                Q.enQueue(t._left)
            if t._right:
                print(t._right._element, end=" ")
                Q.enQueue(t._right)
        return

    def count(self, troot):
        if troot:
            x = self.count(troot._left)
            y = self.count(troot._right)
            return x + y + 1
        return 0

    def level(self, troot):
        if troot:
            x = self.height(troot._left)
            y = self.height(troot._right)

            if x > y:
                return x + 1
            else:
                return y + 1
        return 0

    def height(self,troot):
        count=self.level(troot)
#        count = count - 1
        return count


x = BinaryTree()
emt = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()

x.makeTree(10, emt, emt)
y.makeTree(20, emt, emt)
z.makeTree(30, x, y)
s.makeTree(50, emt, emt)
r.makeTree(40, z, s)

print("r._left = ", r._root._left)

r.inOrder(r._root)
print("in order traversal")
r.postOrder(r._root)
print("post order traversal")
r.preOrder(r._root)
print("pre order traversal")
r.levelOrder()
print("level order traversal")
print(r.count(r._root), len(r))
print(r.height(r._root))
