from LinkedList1 import LinkedList

class hashChaining:

    def __init__(self):
        self._hashTableSize = 10
        self._hashTable = [0] * self._hashTableSize
        for i in range(self._hashTableSize):
            self._hashTable[i] = LinkedList()

    def hashCode(self,key):
        return key % self._hashTableSize

    def insert(self,element):
        i = self.hashCode(element)
        self._hashTable[i].insertSorted(element)

    def search(self,key):
        i = self.hashCode(key)
        return self._hashTable[i].Search(key) != -1

    def display(self):
        for i in range (0,self._hashTableSize):
            p = self._hashTable[i]._head

            print("[",i,"]",end = '-->')
            self._hashTable[i].Display()
            print()

H = hashChaining()
H.insert(50)
H.insert(35)
H.insert(44)
H.insert(11)
H.insert(22)
H.insert(78)
H.insert(28)
print(H.search(35))
H.display()

