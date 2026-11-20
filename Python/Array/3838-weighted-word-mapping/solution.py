class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""
        count=0
        for i in words:
            for j in i:
                count+=weights[ord(j)-ord("a")]
            count=count%26
            ans+=str(chr(26-count+96))
            count=0
        return ans
        