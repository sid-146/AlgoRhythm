inputs = (
    ([1, 3, 3, 3, 3, 6, 10, 10, 10, 100], 3, 1), 
    ([2, 3, 5, 7, 11, 13, 17, 19], 6, -1)
)


def first_occurrence(arr, x):
    left, right = 0, len(arr)
    first_occ_index = -1
    while left <= right:
        mid = (right + left) // 2
        
        if arr[mid] == x:
            right = mid - 1
            first_occ_index = mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return first_occ_index



for arr, x, actual in inputs:
    result = first_occurrence(arr, x)
    if result == actual:
        print(f'Passed for : Actual {actual} :: result : {result}')
    else:
        print(f"Failed for : Actual {actual} :: result : {result}")
