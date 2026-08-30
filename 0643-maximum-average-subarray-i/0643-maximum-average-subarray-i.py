class Solution(object):
    def findMaxAverage(self, nums, k):
        curr_sum=float(sum(nums[:k]))
        max_sum=curr_sum
        for i in range(k,len(nums)):
            last_val=nums[i]
            first_val=nums[i-k]
            curr_sum=curr_sum+last_val
            curr_sum=curr_sum-first_val
            if curr_sum>max_sum:
                max_sum=curr_sum
        return float(max_sum/k)
