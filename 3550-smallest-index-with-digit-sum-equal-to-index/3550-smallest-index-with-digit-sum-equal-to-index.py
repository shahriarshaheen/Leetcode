class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            num=nums[i]
            digits = [int(x) for x in str(num)]
            sum_val=0
            for values in digits:
                sum_val+=values
            if sum_val==i:
                return i
        return -1

                
