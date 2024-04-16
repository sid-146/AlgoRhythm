"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
"""

"""
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""


"""
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""


def sortedSquares(nums:list) ->list:
    if not isinstance(nums, list):
        return

    if len(nums) < 1 or len(nums) > pow(10, 4):
        return
    
    sortedSquares = sorted([pow(x,2) for x in nums]) #! [O(n)]
    return sortedSquares



def sortedSquareWOBuildIn(nums:list) -> list:
    return 


if __name__ == '__main__':
    test1 = [-4,-1,0,3,10]
    assert sortedSquares(test1) == [0,1,9,16,100]
    print('Test 1 with built in passed')
    assert sortedSquareWOBuildIn(test1) == [0,1,9,16,100]
    print('Test 1 without build it passed')

    test2    = [-7,-3,2,3,11]
    assert sortedSquares(test1) == [4,9,9,49,121]
    print('Test 2 with built in passed')
    # print('Test 2 passed')

    assert sortedSquareWOBuildIn(test2) == [0,1,9,16,100]
    print('Test 2 without build it passed')
