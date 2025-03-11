from PracticeQuestions.src.python.utils.helper import timeit


@timeit
def peekElement(arr):
    if len(arr) == 1:
        return 0

    if len(arr) == 2:
        if arr[0] > arr[1]:
            return 0
        else:
            return 1

    peek = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[peek]:
            peek = i

    return peek


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], 2),  # Last element is the peak
        ([1, 1, 1, 2, 1, 1, 1], [0, 1, 3, 5, 6]),  # Multiple peaks
        ([1, 1, 1], [0, 1, 2]),  # All equal elements
        ([3, 2, 1], 0),  # First element is the peak
        ([5], 0),  # Only element is the peak
        ([10, 20, 15, 2, 23, 90, 67], [1, 5]),  # Larger array with multiple peaks
        ([5, 3, 1, 4, 6], [0, 4]),  # Peaks at edges
    ]

    for i, (test, expected) in enumerate(test_cases, 1):
        result = peekElement(test)
        assert result in (expected if isinstance(expected, list) else [expected])
        print(f"test {i} pass\n")
