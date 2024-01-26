class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i,j = 0,len(nums)-1
        c = 0
        while i<j and i<len(nums) and j>=0:
            val = nums[i] + nums[j]
            if  val== k:
                c += 1
                i += 1
                j -= 1
            elif val < k:
                i += 1
            else:
                j -= 1
        return c