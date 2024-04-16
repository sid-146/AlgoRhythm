"""
    An integer divisible by the sum of its digits is said to be a Harshad number. 
    You are given an integer x. Return the sum of the digits of x if x is a Harshad number, 
    otherwise, return -1.
"""

"""
Input: x = 18
Output: 9
Explanation:
The sum of digits of x is 9. 18 is divisible by 9. So 18 is a Harshad number and the answer is 9.
"""

"""
Input: x = 23
Output: -1
Explanation:
The sum of digits of x is 5. 23 is not divisible by 5. So 23 is not a Harshad number and the answer is -1.
"""


def harshadNumber(x: int):
    sum = 0
    t = x
    if not isinstance(x, int):
        return -1

    if x < 1 or x > 100:
        return -1

    # conditions = [isinstance(x, int), x > 0 , x < 101]

    # if not all(conditions):
    # return -1

    while t != 0:
        sum = sum + (t % 10)
        t = t // 10

    if (x % sum) != 0:
        return -1
    return sum


if __name__ == "__main__":
    assert harshadNumber(18) == 9
    print("Test 1 pass")
    assert harshadNumber(23) == -1
    print("Test 2 pass")
