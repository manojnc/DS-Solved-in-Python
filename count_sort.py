''' Count sort uses the indices of a new array that has length equal to the highest element of the original array.The
max element is evaluated and count array is created of that size. The new array called count array is initialized to zero in the begining.
 Original array is traversed from first to last and the count array is incremented at the index equivalent to the value of the original array.
 finally, the count array elements that are not zero can be used to construct the original array in sorted order'''

def count_sort(A):
    n=len(A)
    maxsize=max(A)
    count_array = [0] * (maxsize + 1)

    for i in range (0,n):
        count_array[A[i]] +=1
    i=0
    j=0
    while i < maxsize + 1 :
        if count_array[i] > 0:
            A[j]=i
            j+=1
            count_array[i]-=1
        else :
            i+=1

A=[1,3,2,5,100,25,46,54,78,987,45,65]
print(A)
count_sort(A)
print(A)
