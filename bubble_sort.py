''' Compare the consecutive elements and shift the larger element to right.
Repeat this until all the elements are iterated through'''

def bubble_sort(A):
    n = len(A)
    for count_iter in range(n-1,0,-1):
        for i in range(0,count_iter):
            if A[i] > A[i+1]:
                temp = A[i+1]
                A[i+1] = A[i]
                A[i] = temp
            i+=1
        count_iter-=1



A=[1,3,2,5,100,25,46,54,78,987,45,65]
print(A)
bubble_sort(A)
print(A)