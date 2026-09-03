class Solution(object):
    def maxVowels(self, s, k):
        vowel={'a','e','i','o','u'}
        max_vowel=0
        v_count=0
        for i in range (k):
            char=s[i]
            if char in vowel:
                v_count+=1
        max_vowel=v_count
        
        for i in range(k,len(s)):

            if s[i] in vowel:
                v_count+=1
            if s[i-k] in vowel:
                v_count-=1
            max_vowel=max(max_vowel,v_count)
        return max_vowel
        

                

        