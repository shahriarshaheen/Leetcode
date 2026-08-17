class Solution(object):
    def topKFrequent(self, nums, k):
        hash_dict={}
        for i in range(len(nums)):
            val=nums[i]
            if val not in hash_dict:
                hash_dict[val]=1
            else:
                hash_dict[val]+=1
        sorted_items=sorted(hash_dict.items(),key=lambda x:x[1],reverse=True )
        res_list=[]
        for key, val in sorted_items[:k]:
            res_list.append(key)
            
        return res_list
        