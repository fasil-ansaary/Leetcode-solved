class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dct = {}
        for i in arr:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        if len(list(dct.values())) == len(set(list(dct.values()))):
            return True
        return False