class Solution(object):
    def productExceptSelf(self, nums):
        res=[0]*len(nums)
        pref=[0]*len(nums)
        suf=[0]*len(nums)
        
        pref[0]=1
        for i in range(1,len(pref)):
            pref[i]=pref[i-1]*nums[i-1]
        
        suf[len(nums)-1]=1
        for i in range(len(suf)-2,-1,-1):
            suf[i]=suf[i+1]*nums[i+1]
            
        for i in range(len(res)):
            res[i]=pref[i]*suf[i]

        return res
        


        