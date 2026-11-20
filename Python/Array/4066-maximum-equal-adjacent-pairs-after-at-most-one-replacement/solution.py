class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        d={}
        base=0
        addon=mismatch=0
        for i in range(len(nums)-1):
            a,b=nums[i],nums[i+1]
            if a==b:
                base+=1
            else:
                pair=tuple(sorted((a,b)))
                d[pair]=d.get(pair,0)+1
                mismatch+=1
        if mismatch==0:
            return base
        return base+max(d.values())