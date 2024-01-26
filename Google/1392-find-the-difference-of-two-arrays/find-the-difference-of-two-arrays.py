class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1, nums2 = list(set(nums1)), list(set(nums2))
        lst = []
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
            else:
                lst.append(i)
        return [lst, nums2] 