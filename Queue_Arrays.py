class Queue_Arrays :

    def __init__(self):
        self._data = []
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def enQueue(self,e):
        self._data.append(e)
        self._size += 1

    def deQueue(self):
        if self.isEmpty():
            print("stack is empty. Cannot perform deQueue operation")
            return
        else:
            print("removed {0} from queue".format(self._data[0]))
            self._data.pop(0)
            self._size -= 1
        return

    def display(self):
        print(self._data)
        return

    def first(self):
        if self.isEmpty():
            print("queue is empty")
            return
        else:
            print(self._data[0])
            return self._data[0]

q = Queue_Arrays()
q.deQueue()
q.first()
q.enQueue(4)
q.enQueue(2)
q.enQueue(10)
q.display()
q.deQueue()
q.display()
q.first()
print(len(q))