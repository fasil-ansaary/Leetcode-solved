class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = []
        for i in nums:
            if i not in lst:
                lst.append(i)
            else:
                lst.remove(i)
        return lst.pop()