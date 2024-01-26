class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return min(height)
        i,j = 0, len(height)-1
        val = 0
        while i<j:
            pdct = (j-i)*min(height[i], height[j])
            val = max(val, pdct)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return val
        