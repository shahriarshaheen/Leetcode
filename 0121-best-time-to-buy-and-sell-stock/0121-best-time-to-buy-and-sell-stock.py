class Solution(object):
    def maxProfit(self, prices):
        if len(prices)==1:
            return 0
        profit=0
        curr_price_idx=0
        selling_price_idx=1
        while selling_price_idx<len(prices):
            if prices[selling_price_idx]<prices[curr_price_idx]:
                curr_price_idx=selling_price_idx
            else:
                diff=prices[selling_price_idx]-prices[curr_price_idx]
                if diff>profit:
                    profit=diff
            selling_price_idx+=1
        return profit
        