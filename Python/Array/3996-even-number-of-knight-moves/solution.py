class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        temp=abs(start[0]-target[0])+abs(start[1]-target[1])
        if temp&1==0:
            return True
        else:
            return False
            