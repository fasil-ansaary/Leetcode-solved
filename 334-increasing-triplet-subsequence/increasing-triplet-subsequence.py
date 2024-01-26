class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False
        j,k = float('inf'), float('inf')
        for i in nums:
            if i<=j:
                j = i
            elif i<=k:
                k = i
            else:
                return True
        return False
