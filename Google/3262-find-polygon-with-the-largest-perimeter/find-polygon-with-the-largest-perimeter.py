class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        j = len(nums) - 1
        val = sum(nums)
        while j > -1:
            val = val - nums[j]
            if val > nums[j]:
                val += nums[j]
            j -= 1
        if val == 0:
            return -1
        return val

        