class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n=len(s)
        value=0
        temp=set()
        seen=set()
        ans=[]
        for i in range(n-9):
            curr=s[i:i+10]
            if curr in temp and curr not in seen:
                ans.append(curr)
                seen.add(curr)
            else:
                temp.add(curr)
        return ans


            
        
        
            
