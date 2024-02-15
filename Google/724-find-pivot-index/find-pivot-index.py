class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        lft = 0
        i = 0
        while i < len(nums):
            if total - nums[i] == lft:
                return i
            total -= nums[i]
            lft += nums[i]
            i += 1
        return -1