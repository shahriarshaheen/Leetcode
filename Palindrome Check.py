class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        val_list=list(x)
        i=0
        j=len(val_list)-1
        is_pal=True
        for i in range(len(val_list)//2):
            if val_list[i]!=val_list[j]:
                is_pal=False
                break
            j-=1
        return is_pal
        