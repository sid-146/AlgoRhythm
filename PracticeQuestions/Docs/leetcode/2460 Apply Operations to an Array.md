<h1 ><a href = "https://leetcode.com/problems/apply-operations-to-an-array/description/">2460</a> : Apply Operations to an Array </h1>

# Intuition

The problem involves modifying an array based on specific operations:

1. If two consecutive elements are the same, double the first one and set the second to zero.
2. Shift all zeros to the right while maintaining the relative order of non-zero elements.

# Approach

1. Iterate through the list and check consecutive elements. If they are equal, update the first one to double its value and set the second one to zero.
2. Iterate again to move all zeros to the right while maintaining the order of non-zero elements. This is achieved using a swap function to exchange values.

# Complexity

-   Time complexity:

    -   The first loop runs in $$O(n)$$ time to modify the list.
    -   The second loop runs in $$O(n^2)$$ time to shift the zeros.
    -   The overall complexity is $$O(n^2)$$.

-   Space complexity:
    -   The algorithm modifies the input list in place, using only a few extra variables.
    -   Therefore, the space complexity is $$O(1)$$.

# Code

```python
from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
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
                while j < n and nums[j] == 0:  # Find the first next non-zero element
                    j += 1

                nums[i], nums[j] = swap(nums[i], nums[j])

        return nums
```

# Alternate Method

# Approach

1. Iterate through the list and check consecutive elements. If they are equal, update the first one to double its value and set the second one to zero.
2. Iterate again on elements and replace non zero with the zero holding index.

# Complexity

-   Time Complexity

    -   The first loop runs in $$O(n)$$ time to modify the list.
    -   The second loop runs in $$O(n)$$ time to shift the zeros.
    -   The overall complexity is $$O(n)$$.

-   Space complexity:
    -   The algorithm modifies the input list in place, using only a few extra variables.
    -   Therefore, the space complexity is $$O(1)$$.

```python
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
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

        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[j] = swap(nums[i], nums[j])
                j += 1

        return nums
```
