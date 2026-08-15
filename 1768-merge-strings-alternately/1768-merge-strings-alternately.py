class Solution(object):
    def mergeAlternately(self, word1, word2):
        self.word1=word1
        self.word2=word2
        len_w1=len(self.word1)
        len_w2=len(self.word2)
        merged_word=""
        if len_w1==len_w2:
            for i in range(len_w1):
                first_c=self.word1[i]
                second_c=self.word2[i]
                merged_word+=first_c+second_c
            return merged_word
        elif len_w1>len_w2:
            largest_word=self.word1
            total_len=len_w2
            for i in range(total_len):
                first_c=self.word1[i]
                second_c=self.word2[i]
                merged_word+=first_c+second_c
            for i in range(total_len,len_w1):
                word=self.word1[i]
                merged_word+=word
            return merged_word
        else:
            largest_word=self.word2
            total_len=len_w1
            for i in range(total_len):
                first_c=self.word1[i]
                second_c=self.word2[i]
                merged_word+=first_c+second_c
            for i in range(total_len,len_w2):
                word=self.word2[i]
                merged_word+=word
            return merged_word



        