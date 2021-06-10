class _Node():
    __slots__ = '_element','_next'

    def __init__(self,element,next):
        self._element = element
        self._next = next

class DEQueue_Arrays():

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def addFirst(self,e):
        new = _Node(e,None)
        if self.isEmpty():
            self._head = new
            self._tail = new
        else:
            new._next = self._head
            self._head = new
        self._size += 1
        return

    def addLast(self,e):
        new = _Node(e,None)
        if self.isEmpty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1
        return

    def removeFirst(self):
        if self.isEmpty():
            print("Q is empty")
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        print("removed",e)
        if self.isEmpty():
            self._tail = None
        return e

    def removeLast(self):
        if self.isEmpty():
            print("q is empty")
            return
        p = self._head
        i =1
        while i < self._size -1:
            p = p._next
            i += 1
        self._tail = p
        e = p._next._element
        p._next = None
        self._size -= 1
        print("removed",e)
        return e

    def first(self):
        if self.isEmpty():
            print("deq is empty")
            return
        return self._head._element

    def last(self):
        if self.isEmpty():
            print("deq is empty")
            return
        return self._tail._element

    def display(self):
        if self.isEmpty():
            print("deq is empty")
            return
        p = self._head
        while p:
            print(p._element,end='-->')
            p = p._next
        print()




deq = DEQueue_Arrays()
print(len(deq))
deq.addLast(10)
deq.addFirst(5)
deq.display()
deq.removeLast()
deq.removeFirst()
deq.removeLast()
deq.display()
deq.addLast(10)
deq.addFirst(5)
deq.addLast(12)
deq.addFirst(15)
deq.display()
print(deq.first())
print(deq.last())



