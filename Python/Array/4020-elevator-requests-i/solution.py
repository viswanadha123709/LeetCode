class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        time=0
        curr=0
        for i in requests:
            if curr!=i:
                time+=abs(curr-i)
            curr=i
        return time