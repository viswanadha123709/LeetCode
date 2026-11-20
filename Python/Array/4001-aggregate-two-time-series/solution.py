class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        p1=0
        p2=0
        ans=[]
        while(p1<len(series1) and p2<len(series2)):
            if series1[p1][0]<series2[p2][0]:
                a=series1[p1][1]
                b=series2[p2][1]
                temp=series1[p1][0]
                ans.append([temp,a+b])
                p1+=1
            elif series1[p1][0]==series2[p2][0]:
                a=series1[p1][1]
                b=series2[p2][1]
                temp=series1[p1][0]
                ans.append([temp,a+b])
                p1+=1
                p2+=1
            else:
                a=series1[p1][1]
                b=series2[p2][1]
                temp=series2[p2][0]
                ans.append([temp,a+b])
                p2+=1
        while p1<len(series1):
            temp=series1[p1][0]
            ans.append([temp,series1[p1][1]])
            p1+=1
        while p2<len(series2):
            temp=series2[p2][0]
            ans.append([temp,series2[p2][1]])
            p2+=1
        return ans
        
            
                
        