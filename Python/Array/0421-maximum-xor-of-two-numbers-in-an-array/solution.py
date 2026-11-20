class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans=0
        for i in range(30,-1,-1):
            prefix=set()
            for j in nums:
                prefix.add((j>>i)<<i)
            candidate=ans|(1<<i)
            for p in prefix:
                if p^candidate in prefix:
                    ans=candidate
                    break
        return ans