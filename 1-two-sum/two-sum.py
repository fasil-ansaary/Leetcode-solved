class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j = 0,1
        while i<len(nums):
            val = target - nums[i]
            if val in nums[j:]:
                return i, nums[j:].index(val)+j
            i += 1
            j += 1