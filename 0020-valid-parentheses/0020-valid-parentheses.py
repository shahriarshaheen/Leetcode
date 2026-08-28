class Solution(object):
    def isValid(self, s):
        matching_dict={')':'(','}':'{',']':'['}
        stack=[]
        for chars in s:
            if chars in matching_dict:
                if len(stack)!=0:
                    val=stack[-1]
                    if val==matching_dict[chars]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(chars)
        if len(stack)!=0:
            return False
        else:
            return True

        