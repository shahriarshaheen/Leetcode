class Solution(object):
    def twoSum(self, numbers, target):
        first=0
        end=len(numbers)-1
        while first<end:
            total=numbers[first]+numbers[end]
            if total==target:
                return [first+1,end+1]
            if target>total:
                first+=1
            if target<total:
                end-=1