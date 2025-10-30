class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # operations needed to get 0 index equal to target[0]
        operations = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                # operations needed to get to target[i] as the the array is already at target[i-1]
                operations += target[i] - target[i - 1]

        return operations
