class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        h,m,s=map(int,startTime.split(":"))
        h2,m2,s2=map(int,endTime.split(":"))
        one=(h*3600)+(m*60)+(s)
        two=(h2*3600)+(m2*60)+s2
        return two-one