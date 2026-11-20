class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n=len(nums)
        result=[]
        
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                low=j+1
                high=n-1
                require=target-(nums[i]+nums[j])
                while(low<high):
                    if nums[low]+nums[high]==require:
                        temp=[nums[i],nums[j],nums[low],nums[high]]
                        result.append(temp)
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1

                        low += 1
                        high -= 1
                    elif nums[low]+nums[high]<require:
                        low+=1
                    else:
                        high-=1
        return result
        
        

        