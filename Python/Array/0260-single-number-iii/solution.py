class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        for i in nums:
            xor^=i
        buck1=[]
        buck2=[]
        idx=xor&-xor
        
        for i in nums:
            if i&idx:
                buck1.append(i)
            else:
                buck2.append(i)
        first=0
        second=0
        for i in buck1:
            first^=i
        for j in buck2:
            second^=j
        return [first,second]

            
