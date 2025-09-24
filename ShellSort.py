from typing import List

def shell_sort(arr: List) -> List:
    n = len(arr)    #arr=[8,5,3,7,6,2,4,1]
    gap = n // 2  #initial gap

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

myList = [8,5,3,7,6,2,4,1]
print(shell_sort(myList))