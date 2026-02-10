import time
import random

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took time : {time.time() - start:.22f}")

        return result

    return wrapper


@timeit
def binary_search(arr, x):
    left = 0
    right = len(arr)

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            right = mid
        else:
            left = mid + 1
    return -1


@timeit
def recursive_binary_search(arr, x, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    if arr[mid] < x:
        left = mid + 1
        return recursive_binary_search(arr, x, left, right)
    else:
        right = mid
        return recursive_binary_search(arr, x, left, mid)

for i in (10, 100, 1000, 1_0000, 100_000, 100_000_0):
    print(f"Running : {i}")
    arr = list(range(i))
    x = random.choice(arr)
    result = binary_search(arr, x)
    if x == result:
        print(f"Passed :Actual {x} : Found {result}")
    else:
        print(f"actual : {x} :: found : {result}")
