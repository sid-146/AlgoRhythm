"""

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""


def lengthOfLastWord(s: str) -> int:
    if not isinstance(s, str):
        return

    return len(s.strip().split(" ")[-1])


if __name__ == "__main__":
    assert lengthOfLastWord("Hello World") == 5
    print("Test 1 passed")

    assert lengthOfLastWord("   fly me   to   the moon  ") == 4
    print("test 2 passed")

    assert lengthOfLastWord("luffy is still joyboy") == 6
    print("test 3 passed")

    assert lengthOfLastWord("Single   ") == 6
    print("test 4 passed")
