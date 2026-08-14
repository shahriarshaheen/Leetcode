class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count_hash_s={}
        count_hash_t={}
        for i in range(len(s)):
            count_hash_s[s[i]]=1+count_hash_s.get(s[i],0)
            count_hash_t[t[i]]=1+count_hash_t.get(t[i],0)
        return count_hash_s==count_hash_t

        