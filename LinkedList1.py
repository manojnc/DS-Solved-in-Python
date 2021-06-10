class _Node:
    __slots__ = "_element","_next"

    def __init__(self,element,next):
        self._element=element
        self._next=next

class LinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def IsEmpty(self):
        return self._size == 0

    def AddLast(self,e):
        new = _Node(e,None)
        print("head and tail before adding an element",self._head,self._tail)
        if self.IsEmpty():
            self._head = new
            print("head and tail after adding first element",self._head,self._tail)
            print(dir(self._head))
        else :
            self._tail._next = new
            print("head and tail after adding 2 element onwards", self._head, self._tail)
        self._tail = new
        self._size += 1

    def Display(self):
        p = self._head
        while p:
            print(p._element,end=' --> ')
            p= p._next
        print()

    def Search(self,key):
        p=self._head
        index=0
        while p:
            if p._element == key:
                print("found")
                return index
            else:
                p = p._next
                index += 1
        return -1

    def AddAtBegining(self,e):
        new = _Node(e,None)
        if self.IsEmpty():
            head = new
            tail = new
        else :
            new._next = self._head
            self._head = new
        self._size += 1

    def InsertAny(self,e,pos):
        new = _Node(e,None)
        p = self._head
        i=1
        while i < pos -1:
            p = p._next
            i += 1
        new._next = p._next
        p._next = new
        self._size += 1

    def RemoveAtBegining(self):
        if self.IsEmpty():
            print("List is empty. So nothing to remove")
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.IsEmpty():
            self._tail = None
        print("element removed is : ",e)

    def RemoveAtEnd(self):
        if self.IsEmpty():
            print("list is empty, nothin to delete")
            return
        i = 1
        p  = self._head
        print(len(self))
        print(self._head,self._tail)
        while i < len(self) - 1:
            print(i,p._element,p._next)
            p = p._next
            i += 1
        self._tail = p
        e=p._next._element
        self._tail._next = None
        self._size -+ 1
        print("element removed at the end is : ", e)
        self.Display()

    def RemoveAnywhere(self,pos):
        if self.IsEmpty():
            print("list is empty")
            return
        p = self._head
        i=1
        while i < pos -1 :
            p = p._next
            i += 1
        e = p._next._element
        p._next = p._next._next
        self._size -+ 1
        print ("element {0} removed at pos {1}".format(e,pos,))
        self.Display()

    def insertSorted(self,e):
        new = _Node(e,None)
        if self.IsEmpty():
            self._head = new
            #self._size +=1 --> a common increment is included at the end.
        else:
            p = self._head
            q = self._head

            while p and e > p._element:
                q = p
                p = p._next
            if p == q :
                new._next = self._head
                self._head = new
            else :
                new._next = q._next
                q._next = new
        self._size += 1



def main():
    L = LinkedList()
    L.AddLast(7)
    L.AddLast(1)
    L.AddLast(8)
    print('Size:',len(L))
    res=L.Search(10)
    print(res)
    if res > 0 :
        print("number found at node : ",res)
    else :
        print("number not found")

    L.AddAtBegining(100)
    L.Display()
    L.InsertAny(50,3)
    L.Display()
    L.RemoveAtBegining()
    L.Display()
    L.RemoveAtEnd()
    L.RemoveAnywhere(2)

    H = LinkedList()
    H.insertSorted(50)
    H.insertSorted(20)
    H.insertSorted(0)
    H.insertSorted(5)
    H.Display()
    p = H._head
    while p :
        print(p._element)
        p = p._next

if __name__ == '__main__':
    main()
