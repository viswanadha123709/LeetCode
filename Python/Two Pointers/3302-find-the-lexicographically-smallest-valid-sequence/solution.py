class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n1,n2=len(word1),len(word2)
        last=[-1]*n2
        j=n2-1
        for i in range(n1-1,-1,-1):
            if j==-1:
                break
            if word1[i]==word2[j]:
                last[j]=i
                j-=1
        ans=[]
        j=0
        temp=False
        for i in range(n1):
            if j==n2:
                break
            if word1[i]==word2[j]:
                ans.append(i)
                j+=1
            elif not temp and (j==n2-1 or i<last[j+1]):
                ans.append(i)
                temp=True
                j+=1
        return ans if len(ans)==n2 else []
        
