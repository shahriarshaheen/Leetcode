class Solution(object):
    def pivotIndex(self, nums):
        total_sum=0
        for i in range(len(nums)):
            total_sum+=nums[i]
        for i in range(len(nums)):
            left_sum=sum(nums[0:i])
            right_sum=total_sum-left_sum-nums[i]
            if left_sum==right_sum:
                return i
        return -1
