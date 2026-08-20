class Solution(object):
    def isIsomorphic(self, s, t):
        s_dict={}
        t_dict={}
        for i in range(len(s)):
            s_val=s[i]
            t_val=t[i]
            if s_val in s_dict:
                if s_dict[s_val]!=t_val:
                    return False
            if t_val in t_dict:
                if t_dict[t_val]!=s_val:
                    return False
            s_dict[s_val]=t_val
            t_dict[t_val]=s_val

        return True