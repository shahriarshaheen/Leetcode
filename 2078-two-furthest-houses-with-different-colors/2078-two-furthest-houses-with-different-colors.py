class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist=0
        for i in range(len(colors)):
            col_dist=i
            for j in range(i+1,len(colors)):
                if colors[j]==colors[i]:
                    continue
                else:
                    dist=j-col_dist
                    max_dist=max(dist,max_dist)
        return max_dist

        