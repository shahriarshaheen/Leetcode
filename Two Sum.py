class Solution(object):
    def twoSum(self, nums, target):
        arr_list=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                num_1=nums[i]
                num_2=nums[j]
                sum_val=num_1+num_2
                if num_1+num_2==target:
                    arr_list.append(i)
                    arr_list.append(j)
                    return arr_list
                



            

    

        
        