class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n=len(words)
        masks=[0]*n
        for i in range(n):
            for ch in words[i]:
                masks[i]|=1<<(ord(ch)-ord('a'))
        maxi=0
        for i in range(n):
            for j in range(i+1,n):
                if (masks[i]&masks[j])==0:
                    maxi=max(maxi,len(words[i])*len(words[j]))
        return maxi
        