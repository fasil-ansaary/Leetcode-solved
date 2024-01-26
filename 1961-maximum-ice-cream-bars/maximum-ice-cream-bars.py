class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        ovr = 0
        costs.sort()
        for i in costs:                        
            if i <= coins:
                ovr+=1
                coins-=i                            
        return ovr