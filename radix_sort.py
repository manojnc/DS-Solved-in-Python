'''
radix sort is another index based sorting where the intermediate array is only of size 10.
Unlike count sort, this reduces the space consumed by the algorithm. It works by taking the least/most
 significant bits of each element and puts in the intermediate array at the index location that matches
 the least significant bit. Once the entire array is parsed, the original array is reorganized according to the
 position of the elements in intermediate array. This process is repeated untill there are no more bits remaining
 in any of the elements i.e all the bit of the max element in that array is processed.
'''

def radix_sort(A):
    n = len(A)
    l=[]
    max_element = max(A)
    max_num_of_digits=len(str(max_element))
    bins=[l] * 10

    for i in range(max_num_of_digits):
        for j in range(n):
            sb = int ((A[j]/pow(10,i)) % 10)
            if len(bins[sb]) > 0:
                bins[sb].append(A[j])
            else:
                bins[sb] = [A[j]]
        k=0
        for x in range(10):
            if len(bins[x]) > 0:
                for y in range(len(bins[x])):
                    A[k] = bins[x].pop(0)
                    k = k + 1

A=[3,2,5,100,25,46,54,78,1,987,45,65,-1,0]
print(A)
radix_sort(A)
print(A)
