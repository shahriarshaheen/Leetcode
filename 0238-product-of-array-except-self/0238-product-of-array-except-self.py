class Solution(object):
    def productExceptSelf(self, nums):
        res=[0]*len(nums)
        res[0]=1
        for i in range(1,len(res)):
            res[i]=res[i-1]*nums[i-1]
        
        right=1
        for i in range(len(res)-1,-1,-1):
            res[i]=res[i]*right
            right*=nums[i]
            
        return res
        


        