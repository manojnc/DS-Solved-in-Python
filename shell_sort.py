''' take n/2 as gap number. Compare the element with number at index +gap and -gap. If the number at index+ gap
is greater than swap that number. Compare the swapped number with element at index - gap. If the swapped number is smaller
then swap it again with larger number. Move to next element until gap crosses beyond array'''

def shell_sort(A):
    n = len(A)
    gap = n//2
    while gap > 0:
        i=gap
        while i < n:
            temp=A[i]
            j = i - gap
            while j >= 0 and A[j] > temp:
                A[j + gap] = A[j]
                j = j - gap
            A[j + gap] = temp
            i+=1
        gap= gap//2


A=[1,3,2,5,100,25,46,54,78,987,45,65]
print(A)
shell_sort(A)
print(A)