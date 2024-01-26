class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        fnl = []
        i = 0
        fnl.append(1)
        for i in range(1, len(nums)):
            val = fnl[i-1] * nums[i-1]
            fnl.append(val)
        suff = 1
        for i in range(len(nums)-1,-1,-1):
            fnl[i] *= suff
            suff *= nums[i]
        return fnl

