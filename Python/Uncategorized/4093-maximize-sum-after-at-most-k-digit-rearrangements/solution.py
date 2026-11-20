from sortedcontainers import SortedList
class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        def change(n):
            temp=str(n)
            temp=''.join(sorted(temp,reverse=True))
            return int(temp)-n

        diff=[]
        for i in nums:
            diff.append(change(i))
        return sum(nums)+sum(sorted(diff,reverse=True)[:k])
        
            