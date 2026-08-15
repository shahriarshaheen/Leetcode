class Solution(object):
    def containsDuplicate(self, nums):
        check_list=set()
        for i in range(len(nums)):
            val=nums[i]
            if val in check_list:
                return True
            else:
                check_list.add(val)
        return False
        