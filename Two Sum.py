class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict={}

        for index,val in enumerate(nums):
            difference=target-nums[index]
            if difference in hash_dict:
                return [hash_dict[difference],index]
            hash_dict[val]=index
        return


                    



