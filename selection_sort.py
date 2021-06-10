def selection_sort(arr):
    n= len(arr)

    for i in range(0,n-1):
        position = i
        for j in range(i+1,n):
            if arr[j] < arr[position]:
                position=j
        temp=arr[i]
        arr[i] = arr[position]
        arr[position] = temp

A=[1,3,2,5,100,25,46,54,78,987,45,65]
print(A)
selection_sort(A)
print(A)