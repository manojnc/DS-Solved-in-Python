class DEQueue_Arrays():

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0

    def addFirst(self,e):
        self._data.insert(0,e)

    def addLast(self,e):
        self._data.append(e)

    def removeFirst(self):
        if self.isEmpty():
            print("DEQueue is empty")
            return
        return self._data.pop(0)
    def removeLast(self):
        if self.isEmpty():
            print("DEQueue is empty")
            return
        return self._data.pop()

    def first(self):
        return self._data[0]

    def last(self):
        return self._data[-1]

    def display(self):
        print(self._data)
        return

deq = DEQueue_Arrays()
print(len(deq))
deq.addLast(10)
deq.addFirst(5)
deq.display()
deq.removeLast()
deq.removeFirst()
deq.removeLast()
deq.display()


