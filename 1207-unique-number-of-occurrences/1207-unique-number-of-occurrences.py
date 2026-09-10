class Solution(object):
    def uniqueOccurrences(self, arr):
        unq_dict={}
        for numbers in arr:
            if numbers in unq_dict:
                unq_dict[numbers]+=1
            else:
                unq_dict[numbers]=1
        unique={}
        for val in unq_dict.values():
            if val in unique:
                return False
            else:
                unique[val]=1
        return True

        