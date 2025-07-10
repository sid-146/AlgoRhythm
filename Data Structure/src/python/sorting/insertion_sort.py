def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", arr)
    insertion_sort(arr)
    print("Sorted array:", arr)

    arr = [i for i in range(10)]
    print("Unsorted array:", arr)
    insertion_sort(arr)
    print("Sorted array:", arr)
