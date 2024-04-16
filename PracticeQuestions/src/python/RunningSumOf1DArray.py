"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

"""

def RunningSum(arr:list) -> list:
    # ans = list()
    temp = 0
    return [temp := temp + i for i in arr]


if __name__ == '__main__':
    test1 = [1,2,3,4]
    assert RunningSum(test1) ==  [1,3,6,10]
    print('test 1 pass')
    test2 = [1,1,1,1,1]
    assert RunningSum(test2)
    print('test 2 pass')
    test3 = [3,1,2,10,1]
    assert RunningSum(test3) == [3,4,6,16,17]
    print('test 3 pass')