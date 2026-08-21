class Solution(object):
    def isPalindrome(self, s):
        import re
        s=re.sub(r'[^a-zA-Z0-9]','',s)
        s=list(s.lower())
        first=0
        end=len(s)-1
        while end>first:
            f_ch=s[first]
            l_ch=s[end]
            if f_ch!=l_ch:
                return False
            first+=1
            end-=1
        return True
        