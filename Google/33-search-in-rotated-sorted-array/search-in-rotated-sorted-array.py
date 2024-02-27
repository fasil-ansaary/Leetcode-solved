class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # l = 0
        # r = len(nums)
        # base = 0
        # while l <= r and len(nums) > 1:
        #     mid = l + (r - l) // 2
        #     checkpoint = nums[mid]
        #     if checkpoint < nums[mid+1] and checkpoint > nums[mid-1]:
        #         l = mid + 1
        #     else:
        #         if checkpoint < nums[mid-1]:
        #             base = mid
        #         else:
        #             base = mid + 1
        #     break
        # return base
        if target in nums:
            return nums.index(target)
        return -1