class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i,k = 0, 1
        while k<len(nums):
            if nums[i] == 0:
                if nums[k] != 0:
                    nums[i], nums[k] = nums[k], nums[i]                    
                    i += 1                    
            else:
                i += 1
            k += 1
        print(nums)
        