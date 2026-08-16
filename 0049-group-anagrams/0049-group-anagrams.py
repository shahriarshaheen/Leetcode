class Solution(object):
    def groupAnagrams(self, strs):
        str_list=[]
        strsrs=sorted(strs)
        for i in range(len(strs)):
            char=sorted(strs[i])
            char=''.join(char)
            str_list.append(char)
        hash_dict={}
        for i in range(len(strs)):
            if str_list[i] in hash_dict:
                hash_dict[str_list[i]].append(strs[i])
            else:
                hash_dict[str_list[i]]=[strs[i]]
        res_list=[]
        for val in hash_dict.values():
            res_list.append(val)
        return res_list
        

        