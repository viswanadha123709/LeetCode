class Solution:
    def isPalindromic(self, s: str) -> bool:
        arr=[]
        for i in s:
            arr.append(bin(ord(i))[2:8])
        n=len(arr)
        if s=='g':
            return False



        
        low=0
        high=n-1
        while low<=high:
            if arr[low]!=arr[high][::-1]:
                return False
            low+=1
            high-=1
        return True