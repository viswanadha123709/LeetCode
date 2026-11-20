class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        ans=[]
        temp=set(nums)
        i=lower
        while i<=upper:
            if i not in temp:
                j=i
                while j not in temp and j<=upper:
                    j+=1
                ans.append([i,j-1])
                i=j+1
            else:
                i+=1
        return ans
        