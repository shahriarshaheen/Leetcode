class Solution(object):
    def maxOperations(self, nums, k):
        if len(nums)==1:
            return 0
        nums=sorted(nums)
        op=0
        i=0
        j=len(nums)-1
        while i<j:
            totals=nums[i]+nums[j]
            if totals==k:
                op+=1
                i+=1
                j-=1
            elif totals>k:
                j-=1
            else:
                i+=1
        

        return op