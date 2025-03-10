"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

`2 <= nums.length <= 104`
`-109 <= nums[i] <= 109`
`-109 <= target <= 109`

Only one valid answer exists.

"""

from typing import List
import random
from utils.helper import timeit


@timeit
def two_sum_brute_force(nums, target):
    # This is brute force
    _len = len(nums)
    if _len < 2 or _len > pow(10, 4):
        return []

    for i in range(_len):
        for j in range(1, _len):
            _sum = nums[i] + nums[j]
            if _sum == target:
                return [i, j]


@timeit
def two_sum(nums, target):
    # Optimized Solution according to me
    """
    Using hashmap
    {
        "value":"index"
    }
    Algorithm
    Iterate for each element in the array
    calculate difference
    check if difference is in the hashmap already
    if not present then store difference as key and index as value
    if present then return the index and current index
    """

    hash = {}
    _len = len(nums)
    if _len < 2 or _len > pow(10, 4):
        return []

    for index, num in enumerate(nums):
        diff = target - num
        present = hash.get(diff, "NA")
        if present != "NA":
            return [present, index]
        else:
            hash[num] = index

    return [-1, -1]


if __name__ == "__main__":
    # Define test cases as a list of tuples (array, target, expected_output)
    test_cases = [
        # Small test cases
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        # Edge cases
        ([1, 2], 3, [0, 1]),  # Smallest array possible
        ([-3, 4, 3, 90], 0, [0, 2]),  # Includes negative numbers
        ([10, -10, 20, -20], 0, [0, 1]),  # Pair sum to zero
        ([10, -10, 20, -20], 10, [1, 2]),  # Pair sum to 10
        ([10**9, -(10**9), 5, 15], 20, [2, 3]),  # Large numbers,  # Large numbers
        # Large dataset cases
        (list(range(1, 10001)), 19999, [9998, 9999]),  # Large array, last two elements
    ]

    # Randomized test cases
    for _ in range(5):  # Run 5 randomized cases
        size = random.randint(2, 1000)  # Random array size between 2 and 1000
        nums = random.sample(range(-(10**9), 10**9), size)  # Unique random numbers
        i, j = random.sample(range(size), 2)  # Select two distinct indices
        target = nums[i] + nums[j]
        expected = sorted([i, j])  # Indices should be in any order
        test_cases.append((nums, target, expected))

    # Loop through each test case
    for i, (arr, target, expected) in enumerate(test_cases, 1):
        result = two_sum_brute_force(arr, target)
        print(f"Target : {target} :: Expected {expected}")
        print(f"Result : {result}")
        assert (
            sorted(result) == expected
        ), f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed ✅")
