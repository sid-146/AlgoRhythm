<h1 ><a href = "https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/">2529</a> : Maximum Count of Positive Integer and Negative Integer
    </h1>

# Description

Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

### Examples

```
Input: nums = [-2,-1,-1,1,2,3]

Output: 3

Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
```

```
Input: nums = [-3,-2,-1,0,0,1,2]

Output: 3

Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
```

```
Input: nums = [5,20,66,1314]

Output: 4

Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
```

# Intuition

Since the list is sorted in non-decreasing order:

-   All negative numbers appear before zeros and positive numbers.
-   All positive numbers appear after zeros and negative numbers.

The goal is to count how many negative and positive numbers exist and return the maximum count.

# Approach

1. **Edge Cases:**

-   If the length of nums is greater than 2000, return 0 (though this seems unnecessary).
-   If the list has only one element, return 1 if it is nonzero; otherwise, return 0.

2. **Two-Pointer Technique:**

-   Use two pointers: `first` (starting from the left) and `last` (starting from the right).
-   Traverse toward the center, **counting negatives from the left** and **positives from the right**.
-   Stop when `first > last` to ensure no extra iterations.

3. **Return the Maximum Count:**

-   Return the maximum of `pos` (positive count) and `neg` (negative count).

# Complexity

-   Time complexity:

    -   You iterate through half the list $$(O(n/2) = O(n))$$, so it's $$O(n)$$

-   Space complexity:
    -   Only a few integer variables (`pos`, `neg`, `first`, `last`), so it's $$O(1)$$.

# Code

```python3 []
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
            """
            Time Complexity: `O(n/2)` => `O(N)`
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

                if first != last:
                    if nums[last] < 0:
                        neg += 1
                    elif nums[last] > 0:
                        pos += 1

                first += 1
                last -= 1

            return max(pos, neg)
```

<br>
<hr>

# Alternative Approach

Since the array is sorted, we can use binary search to efficiently count negative and positive numbers.

1. Find the first non-negative number (zero or positive) using binary search → `neg_count`
2. Find the first positive number using binary search → `pos_count`
3. Return max(`neg_count`, `pos_count`).

# Complexity

-   Time complexity:

    -   Binary Search Complexity $O(log(n))$

-   Space complexity:
    -   $O(1)$.

# Code

```python3 []
from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_count = bisect_left(nums, 0)
        pos_count = len(nums) - bisect_right(nums, 0)
        return max(neg_count, pos_count)
```

<br>
<hr>

# Comparison of both Approaches

| Approach          | Time Complexity | Space Complexity | Best for?              |
| ----------------- | --------------- | ---------------- | ---------------------- |
| **Two-Pointer**   | `O(n)`          | `O(1)`           | Small to medium arrays |
| **Binary Search** | `O(log n)`      | `O(1)`           | Large sorted arrays    |
