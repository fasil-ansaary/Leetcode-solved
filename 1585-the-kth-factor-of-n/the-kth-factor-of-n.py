class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factors = [1]
        for i in range(2, n+1):
            if n % i == 0:
                factors.append(i)
        if len(factors) >= k:
            return factors[k-1]
        else:
            return -1