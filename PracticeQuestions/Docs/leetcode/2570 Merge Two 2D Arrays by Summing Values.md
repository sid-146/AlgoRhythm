<h1><a href="https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/">2570</a>: Merge Two 2D Arrays by Summing Values</h1>

# Intuition

The problem involves merging two 2D arrays where each element consists of an ID and a value. If an ID appears in both arrays, their values should be summed. The result should be sorted by ID.  
A dictionary can be used to efficiently store and sum values for each unique ID.

# Approach

1. Use a dictionary to store values corresponding to each unique ID.
2. Iterate over `nums1` and `nums2`, updating the dictionary by summing values for duplicate IDs.
3. Convert the dictionary back into a sorted list of `[id, value]` pairs.
4. Return the sorted result.

# Complexity

-   **Time complexity:**

    -   Iterating over `nums1` and `nums2` takes $$O(n + m)$$, where `n` and `m` are the sizes of the input lists.
    -   Constructing and sorting the result list takes $$O(k log k)$$, where `k` is the number of unique IDs.
    -   The overall time complexity is $$O((n + m) + k log k)$$.

-   **Space complexity:**
    -   We use a dictionary to store `k` unique IDs, requiring $$O(k)$$ space.
    -   The output list also requires $$O(k)$$ space.
    -   The overall space complexity is $$O(k)$$.

# Code

```python3 []
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums_dict = {}

        def merge(arr: list[int], nums_dict: dict):
            for i in range(len(arr)):
                key, value = arr[i]
                exist = nums_dict.get(key, 0)
                nums_dict[key] = exist + value

            return nums_dict

        nums_dict = merge(nums1, nums_dict)
        nums_dict = merge(nums2, nums_dict)

        result = [[k, v] for k, v in nums_dict.items()]
        result.sort(key=lambda x: x[0])

        return result
```
