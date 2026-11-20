class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        temp=0
        a=encoded[0]
        b=encoded[1]
        for i in range(1,len(encoded)+2):
            temp^=i
        for i in encoded[1::2]:
            temp^=i
        

        ans=[temp]
        for i in encoded:
            ans.append(temp^i)
            temp^=i
        return ans