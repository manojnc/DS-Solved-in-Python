class _Node():
    __slots__ = '_element','_next'

    def __init__(self,element,next):
        self._element = element
        self._next = next

class queue_LinkedList():

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def enQueue(self,e):
        new = _Node(e,None)
        if self.isEmpty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1

    def deQueue(self):
        if self.isEmpty():
            print("queue is empty. Cannot perform deQueue")
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.isEmpty():
            self._tail = None
        return e

    def first(self):
        if self.isEmpty():
            print("queue is empty")
            return
        print(self._head._element)
        return self._head._element

    def display(self):
        p = self._head
        while p:
            print(p._element,end='-->')
            p = p._next
        print()

def main():
    q = queue_LinkedList()
    print(q.isEmpty())
    q.enQueue(1)
    q.enQueue(10)
    q.first()
    q.deQueue()
    print(len(q))
    q.enQueue(99)
    q.display()

if __name__ == '__main__':
    main()


