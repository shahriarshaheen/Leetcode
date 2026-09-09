class Solution(object):
    def countCommas(self, n):
        comm=1000
        result=0
        while comm<=n:
            result+=n-comm+1
            comm*=1000
        return result
        