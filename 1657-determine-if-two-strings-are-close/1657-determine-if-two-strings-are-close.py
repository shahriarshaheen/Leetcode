class Solution(object):
    def closeStrings(self, word1, word2):
        dict_1={}
        dict_2={}

        for char in word1:
            if char in dict_1:
                dict_1[char]+=1
            else:
                dict_1[char]=1

        for char in word2:
            if char in dict_2:
                dict_2[char]+=1
            else:
                dict_2[char]=1
        
        if set(dict_1)!=set(dict_2):
            return False
        
        if sorted(dict_1.values())==sorted(dict_2.values()):
            return True
        else:
            return False
           
        
        