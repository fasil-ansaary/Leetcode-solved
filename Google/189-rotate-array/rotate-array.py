class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k <= len(nums):
            temp = nums[:len(nums)-k]
            del nums[:len(nums)-k]
            nums += temp
            return nums
        while k > 0:
            temp = nums.pop()
            nums.insert(0, temp)
            k -= 1
        return nums