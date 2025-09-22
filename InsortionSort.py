#general idea
#1.get the input , arr
#2.from the second (index = 1) to the last one (index = len(arr) - 1)

#3.for each one(arr[i]), check whether it is bigger then arr[i-1]
# if it's False, then the order is correct, no operation
# if it's True, then (1)swap arr[i] and arr[i-1]
# (2)after that, check whether arr[i - 1] > arr[i - 2] or not
#...
#until check arr[0] > arr[1] or not

#j = i - 1
#a[j] ?> a[j + 1]
#a[j - 1] ?> a[j]
#a[j - 2] ?> a[j - 1]
#...
#a[0] ?> a[1]
from typing import List
def insertion_sort( arr: List[int] ) -> List[int]:
    for i in range(1 , len(arr)):
        j = i - 1
        while arr[j] > arr[j+1] and j >= 0 :
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr

nums = [5,2,4,6,1,3]
print(insertion_sort(nums))

#complicity anylisis
#time complicity: O(n^2)
#space complicity: O(1)