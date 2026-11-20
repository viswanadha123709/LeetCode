class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        mini = 101
        ans = -1
        
        for i in range(len(capacity)):
            if capacity[i] >= itemSize and capacity[i] < mini:
                mini = capacity[i]
                ans = i
                
        return ans
        