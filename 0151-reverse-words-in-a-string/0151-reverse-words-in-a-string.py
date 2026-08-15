class Solution(object):
    def reverseWords(self, s):
        list_1=s.strip().split()
        list_2=[]
        for i in range(len(list_1)-1,-1,-1):
            list_2.append(list_1[i])
        return ' '.join(list_2)
        