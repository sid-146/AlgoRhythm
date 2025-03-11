"""
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
"""

def luckyNumbers(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    lucky = list()
    m = len(matrix)  # No of Rows
    n = len(matrix[0])  # No of Columns
    for i in range(m):
        __min__ = min(matrix[i])
        __index_min__ = matrix[i].index(__min__)

        isLucky = True
        for j in range(m):
            if matrix[j][__index_min__] > __min__:
                isLucky = False
                break

        if isLucky:
            lucky.append(__min__)

    return lucky


[[3, 7, 8], [9, 11, 13], [15, 16, 17]]


if __name__ == "__main__":
    testCases = [
        ([[3, 7, 8], [9, 11, 13], [15, 16, 17]], [15]),
        ([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]], [12]),
        ([[7, 8], [1, 2]], [7]),
    ]

    for index, test in enumerate(testCases):
        ip, op = test
        assert luckyNumbers(ip) == op
        print(f"test case passed {index}")