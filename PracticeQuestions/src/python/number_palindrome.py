""" "
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-231 <= x <= 231 - 1
"""

import random
from utils.helper import timeit


@timeit
def isPalindromeUsingString(x: int) -> bool:
    """
    Checking palindrome using string
    """
    return True if str(x) == str(x)[::-1] else False


@timeit
def isPalindromeUsingMath(x: int) -> bool:
    """
    Checking palindrome using math
    """
    if x < 0:
        return False

    og = x
    rev = 0
    while x > 0:
        digit = x % 10
        rev = rev * 10 + digit
        x = x // 10

    if og == rev:
        return True
    else:
        return False


if __name__ == "__main__":
    test_cases = [
        # Small numbers
        (121, True),  # Palindrome
        (-121, False),  # Negative number
        (10, False),  # Not a palindrome
        (0, True),  # Single digit
        (1, True),  # Single digit
        # Edge cases
        (-1, False),  # Negative single digit
        (11, True),  # Smallest two-digit palindrome
        (22, True),  # Another two-digit palindrome
        (100, False),  # Ends in zero, can't be palindrome unless it's 0
        (101, True),  # Basic three-digit palindrome
        (2147447412, True),  # Large valid palindrome
        (2147483647, False),  # Max 32-bit int, not a palindrome
        (-2147483648, False),  # Min 32-bit int, negative
        # Large numbers
        (12345678987654321, True),  # Large odd-length palindrome
        (123456789987654321, True),  # Large even-length palindrome
        (123456789123456789, False),  # Large number, not a palindrome
    ]

    # Randomized test cases
    for _ in range(5):  # Generate 5 random valid test cases
        num = random.randint(0, 10**9)  # Generate a positive integer up to 10^9
        num_str = str(num)
        palindrome_num = int(num_str + num_str[::-1])  # Create a valid palindrome
        test_cases.append((palindrome_num, True))  # Palindrome test case
        test_cases.append(
            (palindrome_num + 1, False)
        )  # Slightly changed, non-palindrome

    # Loop through each test case
    for i, (x, expected) in enumerate(test_cases, 1):
        result = isPalindromeUsingMath(x)
        print(f"Target : {x} :: Expected {expected}")
        print(f"Result : {result}")
        assert (
            result == expected
        ), f"Test {i} failed: Input {x}, Expected {expected}, Got {result}"
        print(f"Test {i} passed ✅")
