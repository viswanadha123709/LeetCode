class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor=0
        summ=0
        for i in nums:
            xor^=i
            summ+=i
        if xor!=0:
            return len(nums)
        if summ:
            return len(nums)-1
        
        return 0