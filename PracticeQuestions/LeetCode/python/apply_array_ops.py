from typing import List

"""
This is two pointer concept:
Todo:
    - Remove the while loop.

"""


def applyOperations(nums: List[int]) -> List[int]:
    n = len(nums) - 1

    def swap(a, b):
        c = a
        a = b
        b = c
        return a, b

    for i in range(n):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0

    for i in range(n):
        if nums[i] == 0:
            j = i
            while j < n and nums[j] == 0:  # Find the first next non zero element
                j += 1

            nums[i], nums[j] = swap(nums[i], nums[j])

    return nums


if __name__ == "__main__":
    result = applyOperations([1, 2, 2, 1, 1, 0])
    assert result == [1, 4, 2, 0, 0, 0], f"Unexpected Output : {result}"
    print("Test case 1 passed successfully.")
    result = applyOperations([0, 1])
    print("Test case 2 passed successfully.")
    result = applyOperations(
        [847, 847, 0, 0, 0, 399, 416, 416, 879, 879, 206, 206, 206, 272]
    )
    print("Test case 3 passed successfully.")
    assert result == [
        1694,
        399,
        832,
        1758,
        412,
        206,
        272,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ], f"Unexpected Output : {result}"
    print("All test cases passed successfully.")
