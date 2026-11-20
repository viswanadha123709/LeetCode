class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        ans=len(nums)+1
        low=1
        high=len(nums)
        while(low<=high):
            mid=(low+high)>>1
            window=nums[:mid]
            total=sum(window)
            found=False
            if total>=target:
                ans=mid
                high=mid-1
                found=True
            else:
                for i in range(mid,len(nums)):
                    total-=nums[i-mid]
                    total+=nums[i]
                    if total>=target:
                        ans=mid
                        high=mid-1
                        found=True
            if not found:
                low=mid+1  
        if ans==len(nums)+1:
            return 0
        else:
            return ans
            

                

        