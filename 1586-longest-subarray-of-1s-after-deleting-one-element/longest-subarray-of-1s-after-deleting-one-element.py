class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        else:
            i,j = 0,1
            total = nums[0]
            check = total
            while j<len(nums):
                check = check + nums[j]
                validity = len(nums[i:j+1]) - check
                if validity >= 2:
                    check = check - nums[i]
                    i += 1
                if validity < 2:
                    total = max(total, check)
                    j += 1
            if len(nums) == total:
                return total - 1
            return total

        