class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        left,right=0,n-1
        while left<right:
            mid=(left+((right-left)>>1))
            if nums[left]<=nums[right]:
                return nums[left]
            if nums[mid]<=nums[right]:
                right=mid
            else:
                left=mid+1
        return nums[left]
        
        