class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l<=r:
            mid = (l + r)/2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if nums[r] < target:
            return r + 1
        if nums[l] < target:
            return l + 1
        if nums[l] > target:
            if l == 0:
                return 0
            return l - 1
        