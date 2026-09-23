class Solution(object):
    def minOperations(self, nums, x):
        sum_arr = sum(nums)
        remain = sum_arr - x
        best = -1
        
        if remain < 0:
            return -1
        s = i = 0
        for j, num in enumerate(nums):
            s += num
            while s > remain:
                s -= nums[i]
                i+= 1
            if s == remain:
                best = max(best, j - i + 1)

        if best < 0:
            return -1
        else:
            return len(nums) - best