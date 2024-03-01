class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = [int(i) for i in s]
        lst.sort(reverse = True)
        fnl_str = str(lst[0])
        val = ''.join([str(elem) for elem in lst[1:]])
        val += fnl_str
        return val
        