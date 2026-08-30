class Solution(object):
    def evalRPN(self, tokens):
        if len(tokens)==1:
            return int(tokens[0])
        stack=[]
        res=0
        for i in range(len(tokens)):
            val=tokens[i]
            if val=="+":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(a+b)
            elif val=="-":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(b-a)
            elif val=="*":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(a*b)
            elif val=="/":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(float(b)/a))
            else:
                val=int(val)
                stack.append(val)
        return stack[0]