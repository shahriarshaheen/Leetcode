class Solution(object):
    def asteroidCollision(self, asteroids):
        stack=[]
        i=0
        while i<len(asteroids):
            val=asteroids[i]
            if not stack or not (stack[-1]>0 and val<0):
                stack.append(val)
                i+=1
            else:
                comp=stack.pop()
                if abs(comp)==abs(val):
                    i+=1
                elif abs(comp)>abs(val):
                    stack.append(comp)
                    i+=1
                else:
                    pass
        return stack