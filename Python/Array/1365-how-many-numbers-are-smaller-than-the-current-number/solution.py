class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp=sorted(nums)
        d={}
        for i in range(len(nums)):
            if temp[i] not in d:
                d[temp[i]]=i
        ans=[]
        for i in nums:
            ans.append(d[i])
        return ans