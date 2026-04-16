class Solution(object):
    def containsDuplicate(self, nums):
        hash_list=set()
        for val in nums:
            if val in hash_list:
                return True
            hash_list.add(val)
        return False
        
        