class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        n=len(intervals)
        ans=0
        for i in range(n-1):
            for j in range(i+1,n):
                if intervals[j][0]<=intervals[i][1]:
                    ans+=1
                else:
                    break
        return ans