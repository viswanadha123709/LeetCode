class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        n=len(nums)
        mini=float('inf')
        for i in range(0,n,2):
            mini=min(mini,int(str(nums[i])+str(nums[i+1])))
        return mini