class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        n=len(intervals)
        starts=[i[0] for i in intervals]
        ans=0
        for i in range(n):
            idx=bisect_right(starts,intervals[i][1])
            ans+=(idx-i-1)
        return ans
            
            
            