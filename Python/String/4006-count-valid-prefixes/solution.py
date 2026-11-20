class Solution:
    def countValidPrefixes(self, s: str) -> int:
        zeros=ones=0
        ans=0
        for i in s:
            if i=='1':
                ones+=1
            else:
                zeros+=1
            if abs(ones-zeros)<2:
                ans+=1
        return ans