class Solution:
    def smallestPalindrome(self, s: str) -> str:
        mid=len(s) // 2
        first="".join(sorted(s[:mid]))

        if len(s)%2==0:
            return first+first[::-1]
        else:
            return first+s[mid]+first[::-1]