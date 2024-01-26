class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == k:
            return float(sum(nums))/float(k)
        
        initial_val = float(sum(nums[0:k]))
        val = initial_val
        print(val)
        i,j = 0,k
        while j<len(nums):
            val = val - float(nums[i]) + float(nums[j])
            initial_val = max(initial_val, val)
            i += 1
            j += 1
        return initial_val/float(k)