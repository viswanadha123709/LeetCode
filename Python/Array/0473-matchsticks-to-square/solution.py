class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        summ=sum(matchsticks)
        if summ%4!=0:
            return False
        target=summ//4
        matchsticks.sort(reverse=True)
        n=len(matchsticks)
        visited=[False]*n
        def backtrack(side,idx,curr):
            if side==3:
                return True
            
            if curr==target:
               return backtrack(side+1,0,0)
    
            for i in range(idx,n):
                if curr+matchsticks[i]<=target:
                    if not visited[i]:
                        visited[i]=True
                        if backtrack(side,i+1,curr+matchsticks[i]):
                            return True
                        visited[i]=False

            return False
                    
        return backtrack(0,0,0)
        