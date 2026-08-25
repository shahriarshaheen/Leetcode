class Solution(object):
    def moveZeroes(self, nums):
        i=0
        k=len(nums)-1
        while i<k:
            j=i+1
            val=nums[i]
            if val==0:
                nums[i]=nums[j]
                while j<k:
                    nums[j]=nums[j+1]
                    j+=1
                nums[k]=0
                k-=1
            else:
                i+=1
        return nums
            