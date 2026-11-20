class Solution:
    def partitionString(self, s: str) -> int:
        n=len(s)
        p=0
        count=0
        while p<n:
            temp=set()
            i=p
            while i<n:
                if s[i] in temp:
                    count+=1
                    break         
                temp.add(s[i])
                i+=1
            p=i
        return count+1
            
            