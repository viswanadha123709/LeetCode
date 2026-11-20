class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        nums.sort()
        for i in range(len(nums)-2):
            p1=i
            p2=i+1
            p3=len(nums)-1

            while(p2<p3):
                curr=nums[p2]+nums[p3]

                if curr== -1*nums[p1]:
                    temp=[nums[p1],nums[p2],nums[p3]]
                    if temp not in ans:
                        ans.append(temp)
                    p2+=1
                    p3-=1
                elif curr+nums[p1]>0:
                    p3-=1
                else:
                    p2+=1
        return ans
        



