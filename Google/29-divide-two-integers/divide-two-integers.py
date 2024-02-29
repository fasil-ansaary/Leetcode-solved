class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        c, r = 0, 0
        if dividend < 0:
            dividend *= -1
            c = 1
        if divisor < 0:
            divisor *= -1
            r = 1
        val = int(dividend/divisor)
        if r == 1:
            val *= -1
        if c == 1:
             val *= -1
        if val > math.pow(2,31) -1:
            return int(math.pow(2, 31) - 1)
        if val < math.pow(-2, 31):
            return int(math.pow(-2, 31))
        return val
        

        