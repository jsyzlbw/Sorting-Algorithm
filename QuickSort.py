#Divide and Conqure

#general idea
#1.choose the last number as the pivot
#2.place all the elements <= pivot before pivot, all the elements > pivot after pivot
#3.then we have two sub list, and then we repeat what we had done

from typing import List

def quick_sort( arr: List , left: int , right: int ) -> None:
    if left < right:
        partition_index = partition(arr , left , right)
        quick_sort(arr , left , partition_index - 1)
        quick_sort(arr , partition_index + 1 , right)

#1.get the rightest element as pivot
#2.put all the smaller one to the left, all the larger to the right
def partition( arr: List , left: int , right: int ) -> int:     #partition the array form left to right

    pivot = arr[right]  #let the rightest be the pivot
    i = left - 1    #i: boundary pointer, everything to the left of (and including) i is always guaranteed to be <= pivot
                    #   at the beginning, i = left - 1, means there are no element <= pivot

    for j in range(left , right):   #j: boundary pointer, used to traverse the array and check 
                                    #whether the current element should go to the left
        if arr[j] <= pivot:
            i += 1
            arr[j] , arr[i] = arr[i] , arr[j]

    arr[i + 1] , arr[right] = arr[right] , arr[i + 1]
    #if i == -1:
    #   means arr[j] <= pivot is always False, the pivot is the smallest, so it should be placed at arr[0]
    #if i == 0:
    #   means arr[j] <= pivot is True for once, the pivot is the second smallest, so it should be placed at arr[1]
    #etc...
    return i + 1    #return the position of pivot

nums = [ 3 , 6 , 8 , 10 , 1 , 2 , 1 ]
quick_sort( nums , 0 , len(nums)-1 )
print(nums)