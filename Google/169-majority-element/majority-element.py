import numpy as np
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct = {}
        if len(nums) < 2:
            return nums[0]
        for i in nums:
            if i not in dct:
                dct[i] = 1
            else:                
                dct[i] += 1
                if dct[i] > len(nums)/2:
                    return i