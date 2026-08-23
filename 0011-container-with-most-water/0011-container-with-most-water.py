class Solution(object):
    def maxArea(self, height):
        max_area=0
        i=0
        j=len(height)-1
        while i<j:
            width=abs(j-i)
            i_height=height[i]
            j_height=height[j]
            heights=min(i_height,j_height)
            area=heights*width
            if area>max_area:
                max_area=area
        
            if i_height>j_height:
                j-=1
            else:
                i+=1
        return max_area
        