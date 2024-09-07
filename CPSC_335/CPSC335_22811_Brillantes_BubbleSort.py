import random

#Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1): #running for any value that has been unsorted.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] #swap

random_num = [random.randint(1, 100) for _ in  range(10)]
print("\nBUBBLE SORT\nUnsorted List: ", random_num)
bubble_sort(random_num)
print("Sorted List: ", random_num, "\n")
