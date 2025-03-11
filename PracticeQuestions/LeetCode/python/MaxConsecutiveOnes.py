"""Given a binary array nums, return the maximum number of consecutive 1's in the array."""

"""
Input: nums = [1,1,0,1,1,1]
Output: 3
"""

# nums = [1,1,1,0,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1]

def maxConsecutive(nums: list) -> int:
    high = 0
    counter = 0
    if not isinstance(nums, list):
        return
    
    if len(nums) < 1:
        return

    # [1,1,0,1,1,1]
    for num in nums:
        if num == 0:
            counter = 0
        elif num == 1:
            counter = counter + 1
            if counter > high:
                high = counter
        else:
            return
    return high


if __name__ == '__main__':
    test1 = [1,1,0,1,1,1]
    test2 = [1,0,1,1,0,1]
    test3 = [1,1,1,0,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1]

    assert maxConsecutive(test1) == 3
    print('Test 1 passed')
    assert maxConsecutive(test2) == 2
    print('Test 2 passed')
    assert maxConsecutive(test3) == 8
    print('Test 3 passed')