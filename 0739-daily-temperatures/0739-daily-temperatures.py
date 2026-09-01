class Solution(object):
    def dailyTemperatures(self, temperatures):
        res=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            temp=temperatures[i]
            while stack and temp>temperatures[stack[-1]]:
                prev_idx=stack.pop()
                res[prev_idx]=i-prev_idx

            stack.append(i)
        return res