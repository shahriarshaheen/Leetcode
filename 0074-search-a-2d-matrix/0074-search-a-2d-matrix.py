class Solution(object):
    def searchMatrix(self, matrix, target):
        row=len(matrix)
        col=len(matrix[0])
        low=0
        high=(row*col)-1
        while low<=high:
            mid=low+(high-low)//2
            r=mid//col
            c=mid%col
            val=matrix[r][c]

            if val==target:
                return True
            elif target>val:
                low=mid+1
            else:
                high=mid-1
            
        return False

