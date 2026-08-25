class Solution(object):
    def isSubsequence(self, s, t):
        s_p=0
        t_p=0
        while t_p<len(t) and s_p<len(s):
            if s[s_p]==t[t_p]:
                s_p+=1
            t_p+=1
        if s_p==len(s):
            return True
        else:
            return False


        