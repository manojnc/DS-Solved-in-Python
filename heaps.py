import heapq as heap
class heaps:

    def __init__(self):
        self._csize = 0
        self._maxsize = 10
        self._data = [-1] * self._maxsize

    def __len__(self):
        return self._csize

    def isEmpty(self):
        return self._csize == 0

    def insert(self,e):
        if self._csize == self._maxsize:
            print("heap is full")
            return

        self._csize += 1
        hi = self._csize
        while hi > 1 and e > self._data[hi//2]:
            self._data[hi] = self._data[hi//2]
            hi = hi//2
        self._data[hi] = e

    def deleteMax(self):
        if self.isEmpty():
            print("heap is empty")
            return

        e = self._data[1]
        self._data[1] = self._data[self._csize]
        self._data[self._csize] = -1
        self._csize -= 1
        i=1
        j=2*i
        while j <= self._csize:
            if self._data[j] > self._data[j+1]:
                j = j + 1
            if self._data[i] < self._data[j]:
                temp = self._data[i]
                self._data[i] = self._data[j]
                self._data[j] = temp
                i = j
                j = 2 * i
            else:
                break
        return e



    def max(self):
        if not self.isEmpty():
            return self._data[1]
        else:
            print("heap is empty")
            return

def main():
    s = heaps()
    s.insert(10)
    s.insert(20)
    s.insert(7)
    s.insert(68)
    s.insert(2)
    s.insert(39)
    print(s._data)
    print(s.max())
    print(s.deleteMax())
    print(s._data)

    L1 = []
    heap.heappush(L1, 10)
    heap.heappush(L1, 1)
    heap.heappush(L1, 9)
    heap.heappush(L1, 78)
    print(L1)
    print(heap.heappop(L1))
    print(L1)
    heap.heappushpop(L1, 3)
    print(L1)
    L2 = [2, 5, 6, 8, 9, 1, 7, 100]
    heap.heapify(L2)
    print(L2)
    print(heap.nsmallest(3, L2))
    print(heap.nlargest(2, L1))

if __name__ == '__main__':
    main()





