class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp=nums[0]
        for i in nums[1:]:
            temp^=i
        return temp