''' Quick sort uses the pivot to divide the Array into two set at a pivot point. This point will divide the array into
two sets, one that has elements smaller than pivot value and the other that has larger elements. This technique is recursively applied
until all the elements are in sorted position.'''

def quick_sort(A,low,high):
    if low < high:
        pivot = partition(A,low,high)
        quick_sort(A,low,pivot -1)
        quick_sort(A,pivot + 1,high)
def partition(A,low,high):
    pivot=A[low]
    i=low+1
    j=high
    while True:
        while i <= j and A[i] <= pivot:
            i+=1
        while i <= j and A[j] >= pivot:
            j-=1
        if i <=j:
            A[i],A[j] = A[j],A[i]
        else:
            break
    A[low],A[j] = A[j],A[low]
    return j



A=[1,3,2,5,100,25,46,54,78,987,45,65]
print(A)
quick_sort(A,0,len(A)-1)
print(A)
