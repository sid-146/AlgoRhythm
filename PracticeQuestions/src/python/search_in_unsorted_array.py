from helper import timeit
import random


@timeit
def search(arr: list, x: int) -> int:
    n = len(arr)
    if n == 1:
        if arr[0] == x:
            return 0
        else:
            return -1

    back = n - 1
    front = 0
    while front <= back:
        if arr[front] == x:
            return front

        if arr[back] == x:
            return back

        front += 1
        back -= 1

    return -1


if __name__ == "__main__":
    # Define test cases as a list of tuples (array, element_to_search, expected_index)
    test_cases = [
        # Small test cases
        ([1, 2, 3, 4], 3, 2),  # Element present
        ([10, 8, 30, 4, 5], 5, 4),  # Element present
        ([10, 8, 30], 6, -1),  # Element absent
        # Edge cases
        ([1], 1, 0),  # Single element, present
        ([1], 2, -1),  # Single element, absent
        ([10, 10, 10, 10], 10, 0),  # All elements identical, present
        ([10, 10, 10, 10], 5, -1),  # All elements identical, absent
        # Larger arrays
        (list(range(1, 10001)), 10000, 9999),  # Large array, last element
        (list(range(1, 10001)), 0, -1),  # Large array, element absent
        # Randomized cases
        (
            random.sample(range(1, 100001), 100000),
            50000,
            -1,
        ),  # Random array, element likely absent
        (
            random.sample(range(1, 100001), 100000) + [50000],
            50000,
            100000,
        ),  # Random array, element present at the end
    ]

    # Loop through each test case
    for i, (arr, x, expected) in enumerate(test_cases, 1):
        # Replace this with the actual function to find the element
        result = search(arr, x)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed\n")
        # break
