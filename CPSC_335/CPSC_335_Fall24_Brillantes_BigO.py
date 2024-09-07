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
print("INSERTION SORT\nUnsorted List: ", random_num)
insertion_sort(random_num)
print("Sorted List: ", random_num, "\n")

#Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][0] < right_half[j][0]:
                arr[k] = left_half[i]
                i+=1
            else:
                arr[k] = right_half[j]
                j+=1
            k+=1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i+=1
            k+=1
            
        while j < len(right_half):
            arr[k] = right_half[j]
            j+=1
            k+=1

books = [
    ("J.K. Rowling", "Harry Potter and the Philosopher's Stone"),
    ("George Orwell", "1984"),
    ("J.K. Rowling", "Harry Potter and the Chamber of Secrets"),
    ("Harper Lee", "To Kill a Mockingbird"),
    ("George Orwell", "Animal Farm"),
    ("F. Scott Fitzgerald", "The Great Gatsby"),
    ("Xane Austen", "Pride and Prejudice"),
    ("Y.R.R. Tolkien", "The Lord of the Rings"),
    ("Agatha Christie", "Murder on the Orient Express"),
    ("W.D. Salinger", "The Catcher in the Rye"),
]

print("\nUnsorted titles:\n")
for author, title in books:
    print(f"{author}:{title}")
merge_sort(books)
print("\nSorted Books by Author's Name: ")
for author, title in books:
    print(f"{author}:{title}")
