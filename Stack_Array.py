class StacksArray :
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def IsEMpty(self):
        return len(self._data) == 0
    def push(self,e):
        self._data.append(e)
    def pop(self):
        if self.IsEMpty():
            print("stack is empty. So cannot perform pop")
            return
        else:
            return self._data.pop()

    def top(self):
        if self.IsEMpty():
            print("stack is empty")
            return
        else:
            return self._data[-1]

s = StacksArray()
s.push(5)
s.push(3)
print(s._data)
print(len(s))
print(s.pop())
print(s.top())

