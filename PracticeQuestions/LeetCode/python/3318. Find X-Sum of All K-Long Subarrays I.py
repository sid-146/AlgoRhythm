class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answers = []
        for i in range(0, len(nums) - k + 1):
            j = i + k
            sub_array = nums[i:j]
            counter = {}
            for m in sub_array:
                counter[m] = counter.get(m, 0) + 1

            counter = sorted(
                counter.items(),
                key=lambda item: (item[1], item[0]),
                reverse=True,
            )[:x]

            answers.append(sum(key * value for key, value in counter))

        return answers
