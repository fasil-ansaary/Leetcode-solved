class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct = {}
        for i in nums:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i] = 2
        keys = list(dct.keys())
        vals = list(dct.values())
        return keys[vals.index(1)]