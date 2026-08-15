class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        highest=0
        for i in candies:
            if i>highest:
                highest=i
        flag=False
        result = []
        for i in range(len(candies)):
            result.append(False)

        for i in range (len(candies)):
            candy=candies[i]
            got=extraCandies+candy
            if got>=highest:
                result[i]=True
        return result