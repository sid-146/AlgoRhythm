import random
from utils.helper import timeit
from bisect import bisect_left, bisect_right
from typing import List

"""
## 2529. Maximum Count of Positive Integer and Negative Integer

Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

Example 1:

Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
Example 2:

Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
Example 3:

Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.


Constraints:

1 <= nums.length <= 2000
-2000 <= nums[i] <= 2000
nums is sorted in a non-decreasing order.
"""

"""
## Approach:
1. Initalize two variables pos and neg to 0.
2. Iterate through the array.
3. If number is positive, increment pos by 1. If number is negative, increment neg by 1.
4. Return the maximum of pos and neg.
"""

"""
Self hint:
    - Mentioned Array is sorted in non-decreasing order.
    - so, they can be same or increase with the next element.
"""


@timeit
def maximumCount(nums):
    """
    Time ComplexityL `O(n/2)` => `O(N)`
    """
    pos = 0
    neg = 0

    if len(nums) > 2000:
        return 0

    if len(nums) == 1:
        # If only one element, return 1 if non zero else 0
        return 0 if nums[0] == 0 else 1

    first, last = 0, len(nums) - 1

    while first <= last:
        if nums[first] < 0:
            neg += 1
        elif nums[first] > 0:
            pos += 1

        if nums[last] < 0:
            neg += 1
        elif nums[last] > 0:
            pos += 1

        first += 1
        last -= 1

    return max(pos, neg)


def maximumCountBisect(self, nums: List[int]) -> int:
    neg_count = bisect_left(nums, 0)  # First non-negative index
    pos_count = len(nums) - bisect_right(nums, 0)  # Count of positive numbers
    return max(neg_count, pos_count)


if __name__ == "__main__":
    test_cases = [
        # Basic cases
        ([-2, -1, -1, 1, 2, 3], 3),  # Equal count of positives and negatives
        ([-3, -2, -1, 0, 0, 1, 2], 3),  # More negatives than positives
        ([5, 20, 66, 1314], 4),  # All positives, no negatives
        ([-5, -20, -66, -1314], 4),  # All negatives, no positives
        ([0, 0, 0, 0], 0),  # Only zeros, neither positive nor negative
        ([0, 1, 2, 3], 3),  # Positives and zeros
        ([-3, -2, -1, 0], 3),  # Negatives and zeros
        # Edge cases
        ([-2000], 1),  # Single negative number
        ([2000], 1),  # Single positive number
        ([0], 0),  # Single zero
        ([-1, 0, 1], 1),  # One negative, one positive, one zero
        # (
        #     list(range(-1000, 1001)),
        #     1000,
        # ),  # Range from -1000 to 1000 (equal pos/neg count)
        # Large cases
        (
            [-2000] * 1000 + [0] * 500 + [2000] * 500,
            1000,
        ),  # More negatives than positives
        (
            [-2000] * 500 + [0] * 500 + [2000] * 1000,
            1000,
        ),  # More positives than negatives
    ]

    # Randomized test cases
    for _ in range(5):  # Generate 5 random valid test cases
        size = random.randint(1, 2000)  # Random array size between 1 and 2000
        negatives = random.randint(0, size)  # Random count of negatives
        positives = size - negatives  # Remaining numbers are positives
        nums = (
            [-random.randint(1, 2000) for _ in range(negatives)]
            + [0] * random.randint(0, 10)
            + [random.randint(1, 2000) for _ in range(positives)]
        )
        nums.sort()  # Ensure non-decreasing order
        expected = max(negatives, positives)  # Max of positive and negative counts
        test_cases.append((nums, expected))

    # Loop through each test case
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = maximumCount(nums)
        assert (
            result == expected
        ), f"Test {i} failed: Input {nums}, Expected {expected}, Got {result}"
        print(f"Test {i} passed ✅")
