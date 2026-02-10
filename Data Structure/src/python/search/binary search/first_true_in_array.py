def first_true_in_arr(arr, x=True):
    left, right = 0, len(arr)
    first_true_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            right = mid - 1
            first_true_index = mid
        else:
            left = mid + 1

    return first_true_index


arr = [False, False, True, True, True]
op = 2
print(f"Actual : {op} :: Result : {first_true_in_arr(arr)}")
