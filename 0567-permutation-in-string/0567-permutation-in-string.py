class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        s1=sorted(s1)
        k=len(s1)
        for i in range(len(s2)-k+1):
            val=sorted(s2[i:i+k])
            if val==s1:
                return True
        return False