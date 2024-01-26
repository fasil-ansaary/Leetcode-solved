class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        val = 0
        fnl = []
        for i in candies:
            if val <= i:
                val = i

        for i in candies:
            if (i+extraCandies) >= val:
                fnl.append(True)
            else:
                fnl.append(False)
        return fnl

        