class Solution(object):
    def twoSum(self, nums, target):
        hash_dict={}
        for index,val in enumerate(nums):
            difference=target-nums[index]
            if difference in hash_dict:
                return [hash_dict[difference],index]
            hash_dict[val]=index
        return
