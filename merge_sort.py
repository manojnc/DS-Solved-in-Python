''' Merge sort uses the technique of breaking down the array into smaller subsets and then merging those subsets
in sorted order to form a final piece of complete sorted array. It uses regression methood to recursively call itself until
the elements are sorted'''

def merge_sort(A,left,right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A,left,mid)
        merge_sort(A,mid+1,right)
        merge(A,left,mid,right)

def merge(A,left,mid,right):
    i=left
    j=mid+1
    k=left
    B=[0] * (right + 1)
    while i <= mid and j <= right:
        if A[i] < A[j]:
            B[k] = A[i]
            i+=1
        else:
            B[k] = A[j]
            j+=1
        k+=1
    while i <= mid:
        B[k] = A[i]
        i+=1
        k+=1
    while j <= right:
        B[k] = A[j]
        j+=1
        k+=1
    for x in range(left,right+1):
        A[x] = B[x]



A=[1,3,2,5,100,25,46,54,78,987,45,65]
print(A)
merge_sort(A,0,len(A)-1)
print(A)
