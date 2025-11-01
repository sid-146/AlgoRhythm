class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        results = []

        for num in nums:
            index = abs(num) - 1 # because all are valid indexes as 1 <= num <= len(nums)
            if nums[index] < 0:
                results.append(abs(num))
            else:
                nums[index] = -nums[index] #marking seen by making it negative

        return results
