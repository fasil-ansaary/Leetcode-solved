class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j = 0,1
        while i<len(nums):
            if nums[i] in nums[j:]:
                nums.remove(nums[i])
                i,j = i, j
            else:
                i += 1
                j = i + 1
        return len(nums)
        