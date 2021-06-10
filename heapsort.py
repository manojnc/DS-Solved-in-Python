from heaps import heaps

def heapsort(A):
    n = len(A)
    H = heaps()

    for i in range(n):
        H.insert(A[i])

    k = n - 1
    for i in range(H._csize):
        A[k] = H.deleteMax()
        k -= 1

A=[100,6,3,8,3,9,18]
print(A)
heapsort(A)
print(A)