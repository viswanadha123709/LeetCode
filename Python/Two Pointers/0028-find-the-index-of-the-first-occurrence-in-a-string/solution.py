class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i]==needle[0]:
                p=0
                while(p<len(needle)):
                    if haystack[i+p]==needle[p]:
                        p+=1
                    else:
                        break
                if p==len(needle):
                    return i

        return -1
        