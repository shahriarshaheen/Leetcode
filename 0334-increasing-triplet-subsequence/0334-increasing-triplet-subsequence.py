class Solution(object):
    def increasingTriplet(self, nums):
        first_val=float('inf')
        second_val=float('inf')

        for n in nums:
            if n<=first_val:
                first_val=n
            elif n<=second_val:
                second_val=n
            else:
                return True
        return False



        