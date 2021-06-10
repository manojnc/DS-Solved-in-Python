class _Node:
    __slots__= '_element','_next'

    def __init__(self,element,next):
        self._element = element
        self._next = next

class Stack_LinkedList():

    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        print(self._size)
        return self._size
    def IsEmpty(self):
        return self._size == 0

    def push(self,e):
        new = _Node(e,None)
        if self.IsEmpty():
            print("Stack is empty. Adding first element")
            self._top = new
        else:
            new._next = self._top
            self._top = new
        self._size += 1

    def pop(self):
        if self.IsEmpty():
            print("stack is empty. Nothing to pop")
            return
        else:
            e = self._top._element
            self._top = self._top._next
            print("removed ",e)
            return e

    def top(self):
        if self.IsEmpty():
            print("stack is empty. Nothing at the top")
            return
        else:
            print(self._top._element)
            return self._top._element

    def Display(self):
        if self.IsEmpty():
            print("Stack is empty")
            return
        else:
            p = self._top
            i=1
            while i <= self._size:
                print(p._element,end="-->")
                p = p._next
                i+=1
            print()


s=Stack_LinkedList()
s.top()