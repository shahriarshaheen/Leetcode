class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums=sorted(list(set(nums)))
        hash_dict={}
        hash_dict[nums[0]]=1
        for i in range(1,len(nums)):
            val=nums[i]
            if val-1 in hash_dict:
                hash_dict[val-1]+=1
                hash_dict[val]=hash_dict.pop(val-1)
            else:
                hash_dict[val]=1
        count=float('-inf')
        for values in hash_dict.values():
            if values>count:
                count=values
        return count
        