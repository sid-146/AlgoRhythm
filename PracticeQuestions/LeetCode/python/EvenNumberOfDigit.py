"""
Given an array nums of integers, return how many of them contain an even number of digits.
"""

"""
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
"""

"""
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
"""

def findNumbers(nums:list)->int:
    counter = 0
    if not isinstance(nums, list):
        return

    if len(nums) < 1 or len(nums) > 500:
        return
 
    for num in nums:
        i = 0
        while num != 0:
            i = i + 1
            num = num // 10
        
        if i % 2 == 0:
            counter = counter + 1
    
    return counter


def findNumber(nums:list)->int:
    if not isinstance(nums,list):
        return 
    
    if len(nums) < 1 or len(nums) > 500:
        return
    counter = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            counter = counter + 1
        

    return counter


if __name__ == '__main__':
    test1 = [555,901,482,1771]
    test2 = [12,345,2,6,7896]

    assert findNumbers(test1) == 1
    print('Test 1 passed')
    assert findNumbers(test2) == 2
    print('Test 2 passed')

