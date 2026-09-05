class Solution(object):
    def largestAltitude(self, gain):
        len_alt=1+len(gain)
        alt=[0]*len_alt
        for i in range(1,len(alt)):
            alt[i]=alt[i-1]+gain[i-1]
        max_alt=0
        for i in range(len(alt)):
            val=alt[i]
            if val>max_alt:
                max_alt=val
        return max_alt
        