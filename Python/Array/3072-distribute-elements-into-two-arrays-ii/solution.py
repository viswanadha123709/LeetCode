from sortedcontainers import SortedList
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        one=[nums[0]]
        two=[nums[1]]
        os=SortedList()
        ts=SortedList()
        os.add(nums[0])
        ts.add(nums[1])

        def greatercount(arr,val):
            n=len(arr)
            return n-arr.bisect_right(val)
        
        for i in nums[2:]:
            if greatercount(os,i)>greatercount(ts,i):
                one.append(i)
                os.add(i)
            elif greatercount(os,i)<greatercount(ts,i):
                two.append(i)
                ts.add(i)
            elif len(one)<len(two):
                one.append(i)
                os.add(i)
            elif len(one)>len(two):
                two.append(i)
                ts.add(i)
            else:
                one.append(i)
                os.add(i)
        one.extend(two)
        return one

