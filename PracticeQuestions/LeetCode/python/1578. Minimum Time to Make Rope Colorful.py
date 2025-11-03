class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        previously_viewed = colors[0]
        current_neededTime = [neededTime[0]]
        total_time = 0

        for i in range(1, len(colors)):
            if colors[i] == previously_viewed:
                current_neededTime.append(neededTime[i])
            else:
                total_time += sum(current_neededTime) - max(current_neededTime)
                current_neededTime = [neededTime[i]]

            previously_viewed = colors[i]
        
        total_time += sum(current_neededTime) - max(current_neededTime)        
        return total_time
