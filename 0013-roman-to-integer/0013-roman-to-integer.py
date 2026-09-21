class Solution(object):
    def romanToInt(self, s):
        list_char={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        val=0

        for i in range(len(s)):
            curr=list_char[s[i]]
            if i+1<len(s):
                next_val=list_char[s[i+1]]
            else:
                next_val=0
            
            if curr<next_val:
                val-=curr
            else:
                val+=curr
        return val
        
        