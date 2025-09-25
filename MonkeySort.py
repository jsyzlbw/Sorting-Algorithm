#shuffle the list and try your fortune!

from typing import List
import random
def monkey_sort(arr: List) -> List:
    while True:
        random.shuffle(arr)
        count = 0
        for i in range(len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                count +=1
        if count == len(arr) - 1:
            return arr 

arr1 = [3,4,67,8,3,4,12]
print(monkey_sort(arr1))