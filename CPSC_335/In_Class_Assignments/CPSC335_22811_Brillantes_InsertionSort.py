import random

#Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

random_num = [random.randint(1, 100) for _ in  range(10)]
print("\nINSERTION SORT\nUnsorted List: ", random_num)
insertion_sort(random_num)
print("Sorted List: ", random_num, "\n")
