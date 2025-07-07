def swap(arr, first, second):
    """
    Swap the values of two variables.

    Args:
        arr: Array or list containing the variables to swap.
        first: The first variable.
        second: The second variable.

    Returns:
        A tuple containing the swapped values.
    """
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


def selection_sort(a):
    swap_counter = 0
    for i in range(len(a)):
        min_index = i
        for j in range(i, len(a)):
            if a[j] < a[min_index]:
                min_index = j

        swap_counter += 1
        if min_index != i:
            swap(a, i, min_index)

    print(f"Total Swaps: {swap_counter}")


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Unsorted array:", arr)
    selection_sort(arr)
    print("Sorted array:", arr)
    # Output: Sorted array: [11, 12, 22, 25, 64]
