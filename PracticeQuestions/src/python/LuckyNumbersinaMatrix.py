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