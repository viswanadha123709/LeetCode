class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-ord("a")]+=1
            key=tuple(count)
            if key not in hm:
                hm[key]=[i]
            else:
                hm[key].append(i)
        return list(hm.values())