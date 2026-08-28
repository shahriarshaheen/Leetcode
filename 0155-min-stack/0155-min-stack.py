class MinStack(object):
    def __init__(self):
   
        self.main_stack=[]
        self.min_stack=[]
        

    def push(self, value):
            val=value
            self.main_stack.append(val)
            if len(self.min_stack)==0 or val<=self.min_stack[-1]:
                self.min_stack.append(val)
        
    def pop(self):
            if len(self.main_stack)!=0:
                val=self.main_stack.pop()
                if val==self.min_stack[-1]:
                    self.min_stack.pop()
        
    def top(self):
            if len(self.main_stack)!=0:
                return self.main_stack[-1]
            else:
                return -1
        
    def getMin(self):
            if len(self.min_stack)!=0:
                return self.min_stack[-1]
            else:
                return -1
        

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()