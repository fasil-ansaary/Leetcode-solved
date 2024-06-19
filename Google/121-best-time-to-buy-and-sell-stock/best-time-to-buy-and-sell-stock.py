class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_val = float('inf')
        for i in prices:
            min_val = min(i, min_val)
            if i > min_val and min_val != float('inf'):
                profit = max(profit, i-min_val)
        return profit
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] > prices[i]:
        #             profit = max(profit, prices[j]-prices[i])
        #         j += 1
        #     i += 1
        # return profit