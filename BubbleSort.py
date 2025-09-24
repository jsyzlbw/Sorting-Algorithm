from typing import List
def bubble_sort(arr: List) ->List:
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

myList = [2,3,4,2,4,1,3,5,875,45,32,1,4]
print(bubble_sort(myList))