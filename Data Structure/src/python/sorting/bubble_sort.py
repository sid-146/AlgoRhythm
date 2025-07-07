def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def bubble_sort(arr):
    swap_counter = 0
    for i in range(len(arr) - 1, 1, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                swapped = True
                swap_counter += 1

        if not swapped:
            break

    print(f"Total Swaps: {swap_counter}")


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", arr)
    bubble_sort(arr)
    print("Sorted array:", arr)

    arr = [i for i in range(10)]
    print("Unsorted array:", arr)
    bubble_sort(arr)
    print("Sorted array:", arr)
