def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    # Sort and merge
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # No comparison as they are sorted.
    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]  # Because temp is 0-indexed


def merge_sort(arr, low, high):
    if low >= high:
        return

    mid = (low + high) // 2
    merge_sort(arr, low, mid)  # Left half
    merge_sort(arr, mid + 1, high)  # Right half
    merge(arr, low, mid, high)


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", arr)
    merge_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)

    arr = [i for i in range(10)]
    print("Unsorted array:", arr)
    merge_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
