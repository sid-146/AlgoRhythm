"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
"""


def findJudge(n: int, trust: list) -> int:
    judge = -1
    votes = [0] * (n + 1)  # need +1 because people is excluding 0
    if n == 1:
        return judge

    # Calculate votes
    for a, b in trust:
        votes[a] = votes[a] - 1
        votes[b] = votes[b] + 1

    for i in range(
        1, n + 1
    ):  # iterating from 1 to n+1 because 0 is excluding in people list
        if votes[i] == n - 1:

            judge = i
            return judge

    return judge


if __name__ == "__main__":
    testCases = [
        ((2, [[1, 2]]), 2),
        ((3, [[1, 3], [2, 3]]), 3),
        ((3, [[1, 3], [2, 3], [3, 1]]), -1),
        ((4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]), 3),
    ]
    for index, test in enumerate(testCases):
        ip, op = test
        assert findJudge(ip[0], ip[1]) == op
        print("Test case : {} passed".format(index))
