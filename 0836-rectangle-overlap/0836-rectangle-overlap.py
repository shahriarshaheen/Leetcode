class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        left1, bottom1, right1, top1 = rec1
        left2, bottom2, right2, top2 = rec2
    
        check_1 = (left1 < right2) and (left2 < right1)
        check_2 = (bottom1 < top2) and (bottom2 < top1)
        
        if check_1 and check_2:
            return True
        return False
        