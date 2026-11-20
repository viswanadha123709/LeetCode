class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        maxnum=max(nums)
        spf=list(range(maxnum+1))
        if maxnum>=1:
            spf[1]=1
        for i in range(2,int(maxnum**0.5)+1):
            if spf[i]==i:
                for j in range(i*i,maxnum+1,i):
                    if spf[j]==j:
                        spf[j]=i




        
        d={}
        n=len(nums)
        left=0
        ans=0
        def factors(num):
            temp=[]
            while num>1:
                p=spf[num]
                temp.append(p)
                while num%p==0:
                    num//=p
            return temp

        fac=[factors(x) for x in nums]
        freq={}
        left=0
        ans=0
        for i in range(len(nums)):
            for p in fac[i]:
                freq[p]=freq.get(p,0)+1

            while len(freq)>k:
                for p in fac[left]:
                    freq[p]-=1

                    if freq[p]==0:
                        del freq[p]

                left+=1
            ans=max(ans,i-left+1)

        return ans
                
            
                
            

        
            
                        
                















        
        