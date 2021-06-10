''' start from second element and compare it with elements on its left. Keep swapping this element with those on left if
they are found to be larger. '''

def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        cvalue=A[i]
        position=i
        print("within for loop pos={0} and cvalue={1}".format(position,cvalue))
        while position > 0 and cvalue <  A[position-1]:
            A[position] = A[position -1]
            position = position -1
            print("within while loop position = ",position,"Array is ", A )

        A[position] = cvalue
        print("arrya after {0} iteration is {1}".format(i,A))



A=[1,3,2,5,100,25,46,54,78,987,45,65]
print(A)
insertion_sort(A)
print(A)