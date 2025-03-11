"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything.
"""

"""
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
"""

"""
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
"""
import random
from utils.helper import timeit


@timeit
def duplicateZeroBruteForce(nums: list[int]) -> None:
    """
    Array is fixed length.

    Steps:
    1. Iterate over all elements
    2. If element is 0 then add 0 on next index and move each element
    3. If element is not 0 then move on to next element
    """
    _len = len(nums)
    for i in range(_len):
        if nums[i] != 0:
            continue
        else:  # means element is 0
            while i <= _len:
                j = i + 1
                holder = nums[j]
                nums[j] = 0


@timeit
def withoutUsingBuiltIn():
    return


if __name__ == "__main__":
    ...
